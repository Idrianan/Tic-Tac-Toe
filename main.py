import tkinter as tk
from tkinter import ttk

def find_current_symbol(counter):
    if counter%2==0:
        return 'X'
    else:
        return 'Y'

def find_another(symbol):
    if symbol=="X":
        return "Y"
    else:
        return "X"

def check_if_draw(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]==None:
                return False
    return True

def check_symbol(field,place):
    x,y = place[0],place[1]
    if check_if_draw(field):
        return 1
    elif check_win(field,"X") or check_win(field,"Y"):
        return 2
    elif field[x][y]!=None:
        return 3
    else:
        return 0

def do_turn(x,field,counter):
    current_turn = find_current_symbol(counter)
    a,b = x//3,x%3
    if not(set_symbol(field,current_turn,(a,b),button_dict[x],counter)):
        return 0
    print(field)
    if check_win(field,current_turn):
        global is_won
        is_won = 1
        win_label["text"] = "Player " + current_turn + " wins!"
    if counter==9:
        win_label["text"] = "Draw"
    return 1


def field_reset():
    global field
    global button_dict
    global win_label
    global counter
    global is_won
    is_won = 0
    counter = 0
    field = [[None]*3 for i in range(3)]
    for i in range(9):
        button_dict[i]['text'] = ""
    win_label["text"] = ""

def horizontal_won_check(field,symbol): 
    size = len(field)
    for i in range(size):
        is_won = True
        for j in range(size):
            if field[i][j]!=symbol:
                is_won = False
                break
        if is_won:
            return True
    return False

def vertical_won_check(field,symbol):
    size = len(field)
    for i in range(size):
        is_won = True
        for j in range(size):
            if field[j][i]!=symbol:
                is_won = False
                break
        if is_won:
            return True
    return False

def diagonal_won_check(field,symbol):
    size = len(field)
    for i in (0,size-1):
        for j in range(size):
            is_won = True
            if field[abs(i-j)][j]!=symbol:
                is_won = False
                break
        if is_won:
            return True
    return False

def check_win(field,symbol):
    return vertical_won_check(field,symbol) or horizontal_won_check(field,symbol) or diagonal_won_check(field,symbol)

def set_symbol(field,symbol,place,curr_button,counter):
    return_code = check_symbol(field,place) 
    if symbol=="X":
        another = "Y"
    else:
        another="X"
    if return_code == 1:
        counter-=1
        win_label["text"]="Game ended in draw"
        return 0
    elif return_code == 2:
        counter-=1
        win_label["text"] = "Player " + another + " is already won"
        return 0
    elif return_code == 3:
        win_label["text"]="You can't place your symbol here"
        counter -= 1
        return 0
    a,b = place[0],place[1]
    field[a][b] = symbol
    curr_button['text'] = symbol
    return 1



field = [[None]*3 for i in range(3)]
button_dict={}
option = list(range(0,9))



root = tk.Tk()
for i in option:
    def func(x=i):
        global counter
        if do_turn(x,field,counter):
            counter+=1
        return 0        

    button_dict[i]=tk.Button(root, text='', command= func, font = "Times 40",width = 8,height = 3)
    win_label = ttk.Label(text="", compound="top",font = "Times 20")
    win_label.grid(row=3)
    reset_button = ttk.Button(root, text = 'Reset', command = field_reset, width=30)
    reset_button.grid(row = 4, column = 2)
    button_dict[i].grid(row = i//3, column = i%3)
    counter = 0

root.mainloop()
