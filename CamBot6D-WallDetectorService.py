import mmap
from dataclasses import dataclass
import struct
import time

@dataclass
class FT_SharedMem:
    DataID: int
    CamWidth: int
    CamHeight: int
    Yaw: float
    Pitch: float
    Roll: float
    X: float
    Y: float
    Z: float
    RawYaw: float
    RawPitch: float
    RawRoll: float
    RawX: float
    RawY: float
    RawZ: float
    X1: float
    Y1: float
    X2: float
    Y2: float
    X3: float
    Y3: float
    X4: float
    Y4: float

#len(TFreeTrackData) == 92
bytes = 92

with mmap.mmap(-1, bytes, 'FT_SharedMem') as mmap_obj:

    while True:
        data = struct.unpack('iiiffffffffffffffffffff', mmap_obj)
        TFreeTrackData = FT_SharedMem(*data)
        print(TFreeTrackData.X, TFreeTrackData.Y, TFreeTrackData.Z)
        time.sleep(0.1)
