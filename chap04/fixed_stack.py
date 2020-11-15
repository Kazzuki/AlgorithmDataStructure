# Fixed-Length Stack Class
from typing import Any

class FixedStack:
    """Fixed-Length Stack Class"""

    class EmptyError(Exception):
        """Exceptions raised when a pop() or peek() is called on an empty fixedstack"""
        pass
    class FullError(Exception):
        """Exceptions raised when a push() is called on a full fixedstack"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """initialization"""
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self) -> int:
        """Returns the number of data in the stack"""
        return self.ptr

    def is_empty(self) -> bool:
        """Determining if the stack is empty"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """Determining if the stack is full"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """Push value to the stack"""
        if self.is_full():
            raise FixedStack.FullError
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> Any:
        """Pop date from the stack"""
        if self.is_empty():
            raise FixedStack.EmptyError
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """Peek date from the stack"""
        if self.is_empty():
            raise FixedStack.EmptyError
        return self.stk[self.ptr - 1]
    
    def clear(self) -> None:
        """Empty the stack"""
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """Finds value in the stack and returns a subscript"""
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value: Any) -> int:
        """Returns the number of values in the stack"""
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    
    def __contains__(self, value: Any) -> bool:
        """Determining if the stack has value"""
        return bool(self.count(value))

    def dump(self) -> None:
        """View the entire stack"""
        if self.is_empty():
            print('stack is empty')
        else:
            print(self.stk[:self.ptr])
    
