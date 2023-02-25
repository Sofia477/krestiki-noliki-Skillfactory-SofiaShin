def greet ():
    print("Крестики нолики")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def ask():
    x= int(input("enter X"))
    y= int(input("enter y"))
    if x<0 or y<0 or x>2 or y>2:
        print("error - x,y must be 0,1,2")
    return x,y

def step(s):
    if s=="X":
     print("Ходит крестик!")
    else:
        print("Ходит нолик!")
    x, y = ask()
    if field[x][y]==" ":
      field[x][y] =s
      show()
    else:
        print("Занята")
        step(s)


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


# main program begins
greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    print(f'Count: {count}')
    if count == 9:
        print(" Ничья!")
        break

    count += 1
    step("X")
    if check_win():
        break

    count += 1
    step("0")
    if check_win():
        break
