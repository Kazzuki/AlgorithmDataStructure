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
    
    def search(self, key: Any) -> Any:
        """キーkeyを持つ要素の探索(値の返却)"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return None
    
    def add(self, key: Any, value: Any) -> bool:
        """キーがkeyで値がvalueの要素の追加(真偽を返却)"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key: Any) -> bool:
        """キーがkeyで値がvalueの要素を削除(真偽を返却)"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        """ハッシュ表をダンプ"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})',end='')
                p = p.next
            print()
