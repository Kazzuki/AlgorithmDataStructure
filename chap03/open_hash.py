# open addressing hashes

from __future__ import annotations
from typing import Any
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

    def hash_value(self, key: Any) -> int:
        """generate a hash value"""
        if isinstance(key, int):
            return key % self.capcity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16))

    def rehash_value(self, key: Any) -> int:
        """Generate re-hashed values"""
        return (self.hash_value(key) + 1) % self.capcity
    
    def search_node(self, key: Any) -> Any:
        """Search for Buckets"""
        hash = self.hash_value(key)
        p = self.table[hash]
        for _ in range(self.capcity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None
    
    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]
        for _ in range(self.capcity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        # hash table is full
        return False

    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        """dunp the hash table"""
        for i in range(self.capcity):
            print(f"{i:2} ", end="")
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key}（{self.table[i].value}）')
            elif self.table[i].stat == Status.EMPTY:
                print('--　未登録　--')
            elif self.table[i].stat == Status.DELETED:
                print('--　削除ずみ　--')
                


