import struct

def X(a: int, b: int) -> int:
    packed_a = struct.pack('>h', a)
    packed_b = struct.pack('>h', b)
    
    val_a = struct.unpack('>h', packed_a)[0]
    val_b = struct.unpack('>h', packed_b)[0]
    
    return max(val_a, val_b)
