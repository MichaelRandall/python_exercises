#! /usr/bin/python

import random

#a list of tuples
CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS) # start is also known as player

    #clever - if any match, recall the function, if no match, return takes you out
    if monster == door or monster == start or door == start:
        return get_locations()

    return monster, door, start


def move_player(player, move):
    # player = (x,y)
    x, y = player

    if move == "LEFT":
        y -= 1
    elif move == "RIGHT":
        y += 1
    elif move == "UP":
        x -= 1
    elif move == "DOWN":
        x += 1
        
    #get the player's currrent local
    #if move is LEFT, y - 1
    #if move is RIGHT, y + 1
    #if move is UP, x - 1
    #if move is DOWN, x + 1

    return x, y

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    #player is equal to (x,y)

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')

    #if players y is 0, remove LEFT
    #if players x is 0, remove UP
    #if players y is 2, remove RIGHT
    #if players x is 2, remove DOWN

    return moves

def draw_map(player):
    print(' _ _ _ ')
    tile = "|{}"

    for idx, cell in enumerate(CELLS):
        if idx in [0,1,3,4,6,7]:
            if cell == player:
                print(tile.format("X"),end="")
            else:
                print(tile.format('_'),end="")
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))


monster, door, player = get_locations()
print("Welcome to the dungeon")

while True:
    moves = get_moves(player)
    
    print("You are currently in room {}".format(player)) # fill in with player/start position
    draw_map(player)
    print("You can move {}".format(moves)) # fill in with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    if move in moves:
        player = move_player(player, move)
    else:
        print("Walls are hard, watch out!")
        continue

    if player == door:
        print("You escaped")
        break
    elif player == monster:
        print("You were eaten")
        break
    
print(get_locations())

