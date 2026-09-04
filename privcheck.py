"""Unix permission analysis helpers."""

def parse_mode(mode):
    value = str(mode).strip()
    if value.startswith("0o"):
        value = value[2:]
    if len(value) != 3 or any(c not in "01234567" for c in value):
        raise ValueError("mode must be a three-digit octal permission")
    return int(value, 8)

def is_world_writable(mode):
    return bool(parse_mode(mode) & 0o002)

def summary(mode):
    value = parse_mode(mode)
    return {"owner": (value >> 6) & 7, "group": (value >> 3) & 7, "other": value & 7, "world_writable": bool(value & 2)}
