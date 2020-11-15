from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Memu', ['push', 'pop', 'peek', 'search', 'dump', 'END'])

def select_nemu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True:
    print(f'現在のデータ数：{len(s)}/{s.capacity}')
    menu = select_nemu()

    if menu == Menu.push:
        x = int(input('キー：　'))
        try:
            s.push(x)
        except FixedStack.FullError:
            print("can't push because stack is full!")
    
    elif menu == Menu.pop:
        try:
            x = s.pop()
            print(f'data is {x}')
        except FixedStack.EmptyError:
            print("can't pop because stack is empty!")

    elif menu == Menu.peek:
        try:
            x = s.peek()
            print(f"peeked date is {x}!")
        except FixedStack.EmptyError:
            print("can't push because stack is empty!")

    elif menu == Menu.search:
        x = int(input('値：'))
        if x in s:
            print(f'{s.count(x)} numbers in the stack. first data place {s.find(x)}')
        else:
            print("This data isn't include in the stack")

    elif menu == Menu.dump:
        s.dump()
    else:
        print('see you again!!')
        break