# open addressing hashes

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# attributes of the bucket
class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket(object):
    """The buckets that make up the hash"""
    def __init__(self, key: Any = None,
                value: Any = None,
                stat: Status = Status.EMPTY) -> None:
        """initialization"""
        self.key = key
        self.value = value
        self.stat = stat
    
    def set(self, key: Any, value: Any, stat: Status) -> None:
        """set values for all fields"""
        self.key = key
        self.value = value
        self.stat = stat
    
    def set_status(self, stat: Status) -> None:
        """set atrributes"""
        self.stat = stat

class OpenHash(object):
    "Hash Class that implemetns the open addressing method"

    def __init__(self, capacity: int) -> None:
        """initialization"""
        self.capcity = capacity
        self.table = [Bucket()] * self.capcity

    def hssh_value(self, key: Any) -> int:
        """generate a hash value"""
