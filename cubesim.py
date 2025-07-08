import numpy as np
import pygame

pygame.display.init()
bgsize = (1000, 250)
bg = pygame.display.set_mode(bgsize, 0)
bg.fill('black')

faces = np.array([
    green:=[
    ['F', 'F', 'F'],
    ['F', 'F', 'F'],
    ['F', 'F', 'F']
],blue:=[
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
],red:=[
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
],orange:=[
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L']
],white:=[
    ['U', 'U', 'U'],
    ['U', 'U', 'U'],
    ['U', 'U', 'U']
],yellow:=[
    ['D', 'D', 'D'],
    ['D', 'D', 'D'],
    ['D', 'D', 'D']
]
])

pieces = np.array([
    front:=[
    [5, 1, 7],
    [6, 21, 8],
    [13, 14, 15]
],back:=[
    [9, 3, 11],
    [10, 22, 12],
    [20, 19, 18]
],right:=[
    [7, 2, 9],
    [8, 23, 10],
    [15, 17, 20]
],left:=[
    [11, 4, 5],
    [12, 24, 6],
    [18, 16, 13]
],up:=[
    [11, 3, 9],
    [4, 25, 2],
    [5, 1, 7]
],down:=[
    [13, 14, 15],
    [16, 26, 17],
    [18, 19, 20]
]
])



def u():
    global faces
    global pieces
    global white
    global up

    white = np.rot90(white, -1)
    temp1, temp2, temp3 = green[0][0], green[0][1], green[0][2]
    green[0][0], green[0][1], green[0][2] = red[0][0], red[0][1], red[0][2]
    red[0][0], red[0][1], red[0][2] = blue[0][0], blue[0][1], blue[0][2]
    blue[0][0], blue[0][1], blue[0][2] = orange[0][0], orange[0][1], orange[0][2]
    orange[0][0], orange[0][1], orange[0][2] = temp1, temp2, temp3

    up = np.rot90(up, -1)
    temp1, temp2, temp3 = front[0][0], front[0][1], front[0][2]
    front[0][0], front[0][1], front[0][2] = right[0][0], right[0][1], right[0][2]
    right[0][0], right[0][1], right[0][2] = back[0][0], back[0][1], back[0][2]
    back[0][0], back[0][1], back[0][2] = left[0][0], left[0][1], left[0][2]
    left[0][0], left[0][1], left[0][2] = temp1, temp2, temp3

    pieces = np.array([front, back, right, left, up, down])
    faces = np.array([green, blue, red, orange, white, yellow])

def r():
    global faces
    global pieces
    global red
    global right

    red = np.rot90(red, -1)
    temp1, temp2, temp3 = green[0][2], green[1][2], green[2][2]
    green[0][2], green[1][2], green[2][2] = yellow[0][2], yellow[1][2], yellow[2][2]
    yellow[0][2], yellow[1][2], yellow[2][2] = blue[2][0], blue[1][0], blue[0][0]
    blue[2][0], blue[1][0], blue[0][0] = white[0][2], white[1][2], white[2][2]
    white[0][2], white[1][2], white[2][2] = temp1, temp2, temp3

    right = np.rot90(right, -1)
    temp1, temp2, temp3 = front[0][2], front[1][2], front[2][2]
    front[0][2], front[1][2], front[2][2] = down[0][2], down[1][2], down[2][2]
    down[0][2], down[1][2], down[2][2] = back[2][0], back[1][0], back[0][0]
    back[2][0], back[1][0], back[0][0] = up[0][2], up[1][2], up[2][2]
    up[0][2], up[1][2], up[2][2] = temp1, temp2, temp3

    pieces = np.array([front, back, right, left, up, down])
    faces = np.array([green, blue, red, orange, white, yellow])

def f():
    global faces
    global pieces
    global green
    global front

    green = np.rot90(green, -1)
    temp1, temp2, temp3 = yellow[0][0], yellow[0][1], yellow[0][2]
    yellow[0][0], yellow[0][1], yellow[0][2] = red[2][0], red[1][0], red[0][0]
    red[2][0], red[1][0], red[0][0] = white[2][2], white[2][1], white[2][0]
    white[2][2], white[2][1], white[2][0] = orange[0][2], orange[1][2], orange[2][2]
    orange[0][2], orange[1][2], orange[2][2] = temp1, temp2, temp3

    front = np.rot90(front, -1)
    temp1, temp2, temp3 = down[0][0], down[0][1], down[0][2]
    down[0][0], down[0][1], down[0][2] = right[2][0], right[1][0], right[0][0]
    right[2][0], right[1][0], right[0][0] = up[2][2], up[2][1], up[2][0]
    up[2][2], up[2][1], up[2][0] = left[0][2], left[1][2], left[2][2]
    left[0][2], left[1][2], left[2][2] = temp1, temp2, temp3

    pieces = np.array([front, back, right, left, up, down])
    faces = np.array([green, blue, red, orange, white, yellow])



while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'r':
                r()
            elif event.unicode == 'f':
                f()
            elif event.unicode == 'u':
                u()
            
        if event.type == pygame.QUIT:
            quit()

    disp = np.ndarray.tolist(faces)
    for x,face in enumerate(disp):
        for y,row in enumerate(face):
            for z,piece in enumerate(row):
                if disp[x][y][z] == 'R':
                    disp[x][y][z] = 'red'
                if disp[x][y][z] == 'L':
                    disp[x][y][z] = 'orange'
                if disp[x][y][z] == 'B':
                    disp[x][y][z] = 'blue'
                if disp[x][y][z] == 'F':
                    disp[x][y][z] = 'green'
                if disp[x][y][z] == 'D':
                    disp[x][y][z] = 'yellow'
                if disp[x][y][z] == 'U':
                    disp[x][y][z] = 'white'

    for x in range(6):
        for y in range(3):
            for z,piece in enumerate(disp[x][y]):
                pygame.draw.rect(bg, piece, (25+x*150 + z*40, 25+y*40, 35,35), width=0)

    pygame.display.update()