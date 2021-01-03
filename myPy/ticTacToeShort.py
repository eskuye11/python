import numpy as np
from itertools import cycle
#              The shortest Tic Tac Toe !    50 lines only, so far ...

game = np.array([['_','_','_'], ['_','_','_'], ['_','_','_']], dtype=str)
gameKey = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1],
           6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
players, win = {1: 'X', 2: 'O'}, False
func1 = lambda items: items == players[turn]


def checkWining():
    global win
    for column in game:
        if all(map(func1, (game[0, 0], game[0, 1], game[0, 2]))):  win = True
        elif all(map(func1, (game[1, 0], game[1, 1], game[1, 2]))):  win = True
        elif all(map(func1, (game[2, 0], game[2, 1], game[2, 2]))):  win = True
        elif all(map(func1, (game[0, 0], game[1, 0], game[2, 0]))):  win = True
        elif all(map(func1, (game[0, 1], game[1, 1], game[2, 1]))):  win = True
        elif all(map(func1, (game[0, 2], game[1, 2], game[2, 2]))):  win = True
        elif all(map(func1, (game[0, 0], game[1, 1], game[2, 2]))):  win = True
        elif all(map(func1, (game[2, 0], game[1, 1], game[0, 2]))):  win = True
        else: win = False
    if win:
        print()
        print(game)
        print(f'\n      You Win !, player {turn}\n')
    return win


def updateBoard(choice):
    x, y = gameKey[choice]
    if turn == 1:
        game[x][y] = 'X'
    else:
        game[x][y] = 'O'


while not win:
    for turn in cycle('12'):
        turn = int(turn)
        if not bool([sub for sub in game if any((e == '_') for e in sub)]):
            print('\n    Game Draw  !  \n    Try  Again !')
            break
        print(game)
        choices = int(input(f'Chose (1-9), ( {players[turn]} ) player {turn} : '))
        xx, yy = gameKey[choices]
        if game[xx][yy] == '_':
            updateBoard(choices)
            if checkWining(): break
        else: print(f"   Please try another spot, Mr. '{players[turn]}' !")

