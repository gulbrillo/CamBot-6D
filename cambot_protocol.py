"""
CamBot-6D Custom UDP Dual-PC Protocol
Pure Python (stdlib only): hashlib, hmac, secrets, struct, time
"""

import hashlib
import hmac
import secrets
import struct
import time

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROTOCOL_VERSION = 1

MSG_AXES      = 0x01
MSG_HELLO     = 0x10
MSG_HELLO_ACK = 0x11

# Packet sizes (computed once)
_AXES_FMT          = '!BBIffffffI'
_AXES_PAYLOAD_SIZE = struct.calcsize(_AXES_FMT)   # 34 bytes
_HMAC_SIZE         = 32

AXES_PACKET_SIZE   = _AXES_PAYLOAD_SIZE + _HMAC_SIZE   # 66 bytes
HELLO_SIZE         = 18   # 1 + 1 + 16
HELLO_ACK_SIZE     = 50   # 1 + 1 + 16 + 32


# ---------------------------------------------------------------------------
# Key derivation
# ---------------------------------------------------------------------------

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 32-byte key from a plain-text password using PBKDF2-HMAC-SHA256."""
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _sign(payload: bytes, key: bytes) -> bytes:
    return hmac.new(key, payload, hashlib.sha256).digest()


# ---------------------------------------------------------------------------
# Packing (sender side)
# ---------------------------------------------------------------------------

def pack_axes(seq: int,
              x: float, y: float, z: float,
              yaw: float, pitch: float, roll: float,
              key: bytes,
              ts_ms: int = 0) -> bytes:
    """Pack a 66-byte axes packet (payload + HMAC)."""
    if ts_ms == 0:
        ts_ms = int(time.monotonic() * 1000) & 0xFFFFFFFF
    payload = struct.pack(
        _AXES_FMT,
        PROTOCOL_VERSION, MSG_AXES,
        seq & 0xFFFFFFFF,
        x, y, z, yaw, pitch, roll,
        ts_ms & 0xFFFFFFFF,
    )
    return payload + _sign(payload, key)


def pack_hello(nonce: bytes = None) -> bytes:
    """Pack an 18-byte MSG_HELLO challenge (no HMAC — nonce is the challenge)."""
    if nonce is None:
        nonce = secrets.token_bytes(16)
    return struct.pack('!BB', PROTOCOL_VERSION, MSG_HELLO) + nonce


def pack_hello_ack(nonce: bytes, key: bytes) -> bytes:
    """Pack a 50-byte MSG_HELLO_ACK response: nonce_echo + HMAC(key, nonce)."""
    header = struct.pack('!BB', PROTOCOL_VERSION, MSG_HELLO_ACK)
    mac = _sign(nonce, key)
    return header + nonce + mac


# ---------------------------------------------------------------------------
# Verification (receiver side)
# ---------------------------------------------------------------------------

def verify_hello_ack(data: bytes, expected_nonce: bytes, key: bytes) -> bool:
    """
    Verify a MSG_HELLO_ACK packet received from the controller.
    Returns True only if the nonce echo and HMAC are both correct.
    """
    if len(data) != HELLO_ACK_SIZE:
        return False
    if data[1] != MSG_HELLO_ACK:
        return False
    nonce_echo = data[2:18]
    mac        = data[18:50]
    if not hmac.compare_digest(nonce_echo, expected_nonce):
        return False
    expected_mac = _sign(expected_nonce, key)
    return hmac.compare_digest(mac, expected_mac)


def verify_and_unpack(data: bytes, key: bytes,
                      last_seq_map: dict, sender_ip: str):
    """
    Verify and unpack a received UDP datagram.

    Returns a dict on success:
      {'type': MSG_AXES,      'seq': int, 'x': float, ...}
      {'type': MSG_HELLO,     'nonce': bytes}       <- no HMAC on HELLO
      {'type': MSG_HELLO_ACK, 'raw': bytes}         <- caller uses verify_hello_ack

    Returns None on:
      - bad / missing HMAC
      - wrong packet size
      - replay (seq <= last seen for this IP)
    """
    if len(data) < 2:
        return None

    msg_type = data[1]

    if msg_type == MSG_AXES:
        if len(data) != AXES_PACKET_SIZE:
            return None
        payload = data[:_AXES_PAYLOAD_SIZE]
        mac     = data[_AXES_PAYLOAD_SIZE:]
        if not hmac.compare_digest(_sign(payload, key), mac):
            return None
        fields = struct.unpack(_AXES_FMT, payload)
        seq = fields[2]
        last = last_seq_map.get(sender_ip, -1)
        if seq <= last:
            return None
        last_seq_map[sender_ip] = seq
        return {
            'type':   MSG_AXES,
            'seq':    seq,
            'x':      fields[3],
            'y':      fields[4],
            'z':      fields[5],
            'yaw':    fields[6],
            'pitch':  fields[7],
            'roll':   fields[8],
            'ts_ms':  fields[9],
        }

    elif msg_type == MSG_HELLO:
        # No HMAC on HELLO — it is merely a challenge nonce
        if len(data) != HELLO_SIZE:
            return None
        nonce = data[2:18]
        return {'type': MSG_HELLO, 'nonce': nonce}

    elif msg_type == MSG_HELLO_ACK:
        # Caller should call verify_hello_ack() with the pending nonce
        return {'type': MSG_HELLO_ACK, 'raw': data}

    return None
