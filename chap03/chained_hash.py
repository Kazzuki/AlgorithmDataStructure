from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """hashを構成するノード"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """initialize"""
        # キー
        self.key = key
        # 値
        self.value = value
        # 後続nodeへの参照
        self.next = next

class CahinedHash:
    """チェイン法を実現するハッシュクラス"""
    def __init__(self, capacity: int) -> None:
        """initialize"""
        # hash tableの容量
        self.capacity = capacity
        # hash table(リスト)
        self.table = [None] * self.capacity
    
    def hash_value(self, key: Any) -> int:
        """ハッシュ値を求める"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
