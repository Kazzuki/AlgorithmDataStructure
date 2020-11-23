from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Memu', ['enque', 'deque', 'peek', 'search', 'dump', 'END'])

def select_nemu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'現在のデータ数：{len(q)}/{q.capacity}')
    menu = select_nemu()

    if menu == Menu.enque:
        x = int(input('キー：　'))
        try:
            q.enque(x)
        except FixedQueue.FullError:
            print("can't enque because queue is full!")
    
    elif menu == Menu.deque:
        try:
            x = q.deque()
            print(f'data is {x}')
        except FixedQueue.EmptyError:
            print("can't deque because queue is empty!")

    elif menu == Menu.peek:
        try:
            x = q.peek()
            print(f"peeked date is {x}!")
        except FixedQueue.EmptyError:
            print("can't enque because queue is empty!")

    elif menu == Menu.search:
        x = int(input('値：'))
        if x in q:
            print(f'{q.count(x)} numbers in the queue. first data place {q.find(x)}')
        else:
            print("This data isn't include in the queue")

    elif menu == Menu.dump:
        q.dump()
    else:
        print('see you again!!')
        break