from enum import Enum
from chained_hash import CahinedHash

Menu = Enum('Memu', ['add', 'remove', 'search', 'dump', 'END'])

def select_nemu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = CahinedHash(13)

while True:
    menu = select_nemu()

    if menu == Menu.add:
        key = int(input('キー：　'))
        val = input('値：')
        if not hash.add(key, val):
            print("can't add!")
    
    elif menu == Menu.remove:
        key = int(input('キー：　'))
        if not hash.remove(key):
            print("can't remove!")
    
    elif menu == Menu.search:
        key = int(input('キー：　'))
        t = hash.search(key)
        if t is not None:
            print(f"value is <{t}>")
        else:
            print("cna't find it!")
            
    elif menu == Menu.dump:
        hash.dump()
    else:
        print('see you again!!')
        break