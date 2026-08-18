from __future__ import annotations

import struct, zlib

PNG_SIG = b"\x89PNG\r\n\x1a\n"
PNG_DEFAULT_REMOVE = {b"tEXt", b"zTXt", b"iTXt", b"eXIf", b"caBX"}


def parse_png(data: bytes):
    if not data.startswith(PNG_SIG):
        raise ValueError("not a PNG")
    pos = len(PNG_SIG)
    chunks = []
    while pos + 12 <= len(data):
        length = struct.unpack(">I", data[pos:pos+4])[0]
        ctype = data[pos+4:pos+8]
        end = pos + 12 + length
        if end > len(data):
            raise ValueError("truncated PNG")
        chunks.append((ctype, data[pos:end]))
        pos = end
        if ctype == b"IEND":
            break
    return chunks


def clean_png(data: bytes):
    chunks = parse_png(data)
    removed = []
    out = bytearray(PNG_SIG)
    for ctype, raw in chunks:
        if ctype in PNG_DEFAULT_REMOVE:
            removed.append(ctype.decode("latin1"))
            continue
        out += raw
    return bytes(out), removed


def parse_jpeg_segments(data: bytes):
    if not data.startswith(b"\xff\xd8"):
        raise ValueError("not a JPEG")
    pos = 2
    segments = []
    while pos < len(data):
        if data[pos] != 0xFF:
            break
        while pos < len(data) and data[pos] == 0xFF:
            pos += 1
        if pos >= len(data):
            break
        marker = data[pos]
        start = pos - 1
        pos += 1
        if marker in (0xD9, 0xDA):
            segments.append((marker, data[start:]))
            break
        if marker in range(0xD0, 0xD8) or marker == 0x01:
            segments.append((marker, data[start:pos]))
            continue
        if pos + 2 > len(data):
            raise ValueError("truncated JPEG")
        length = struct.unpack(">H", data[pos:pos+2])[0]
        end = pos + length
        if end > len(data):
            raise ValueError("truncated JPEG segment")
        segments.append((marker, data[start:end]))
        pos = end
    return segments


def jpeg_label(marker: int, raw: bytes):
    payload = raw[4:] if len(raw) >= 4 else b""
    if marker == 0xE1:
        if payload.startswith(b"Exif\x00\x00"):
            return "APP1-EXIF"
        if b"http://ns.adobe.com/xap/1.0/" in payload[:128]:
            return "APP1-XMP"
        return "APP1"
    if marker == 0xEB:
        return "APP11-JUMBF/C2PA-candidate"
    if marker == 0xE2:
        return "APP2"
    if marker == 0xFE:
        return "COM"
    return f"MARKER-FF{marker:02X}"


def clean_jpeg(data: bytes, strict_privacy: bool = False):
    segs = parse_jpeg_segments(data)
    out = bytearray(b"\xff\xd8")
    removed = []
    for marker, raw in segs:
        if raw.startswith(b"\xff\xd8"):
            raw = raw[2:]
        label = jpeg_label(marker, raw)
        remove = False
        if marker == 0xE1:
            payload = raw[4:] if len(raw) >= 4 else b""
            remove = payload.startswith(b"Exif\x00\x00") or b"http://ns.adobe.com/xap/1.0/" in payload[:128]
        elif marker == 0xEB:
            remove = True
        elif strict_privacy and marker in (0xE2, 0xFE):
            remove = True
        if remove:
            removed.append(label)
        else:
            out += raw
    return bytes(out), removed
