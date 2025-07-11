import numpy as np
import pygame
import twophase.solver as sv

pygame.display.init()
bgsize = (830, 630)
bg = pygame.display.set_mode(bgsize, 0)
bg.fill('black')

sol = ''

facelets = np.array([
    white:=[
    ['U', 'U', 'U'],
    ['U', 'U', 'U'],
    ['U', 'U', 'U']
],red:=[
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
],green:=[
    ['F', 'F', 'F'],
    ['F', 'F', 'F'],
    ['F', 'F', 'F']
],yellow:=[
    ['D', 'D', 'D'],
    ['D', 'D', 'D'],
    ['D', 'D', 'D']
],orange:=[
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L']
],blue:=[
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
]
])

pieces = np.array([
    up:=[
    [11, 3, 9],
    [4, 25, 2],
    [5, 1, 7]
],right:=[
    [7, 2, 9],
    [8, 23, 10],
    [15, 17, 20]
],front:=[
    [5, 1, 7],
    [6, 21, 8],
    [13, 14, 15]
],down:=[
    [13, 14, 15],
    [16, 26, 17],
    [18, 19, 20]
],left:=[
    [11, 4, 5],
    [12, 24, 6],
    [18, 16, 13]
],back:=[
    [9, 3, 11],
    [10, 22, 12],
    [20, 19, 18]
]
])

def u():
    global facelets
    global pieces
    global white
    global up
    global sol

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

    pieces = np.array([up, right, front, down, left, back])
    facelets = np.array([white, red, green, yellow, orange, blue])
    sol += 'u'

def r():
    global facelets
    global pieces
    global red
    global right
    global sol

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

    pieces = np.array([up, right, front, down, left, back])
    facelets = np.array([white, red, green, yellow, orange, blue])
    sol += 'r'

def f():
    global facelets
    global pieces
    global green
    global front
    global sol

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

    pieces = np.array([up, right, front, down, left, back])
    facelets = np.array([white, red, green, yellow, orange, blue])
    sol += 'f'

def d():
    global facelets
    global pieces
    global yellow
    global down
    global sol

    yellow = np.rot90(yellow, -1)
    temp1, temp2, temp3 = green[2][0], green[2][1], green[2][2]
    green[2][0], green[2][1], green[2][2] = orange[2][0], orange[2][1], orange[2][2]
    orange[2][0], orange[2][1], orange[2][2] = blue[2][0], blue[2][1], blue[2][2]
    blue[2][0], blue[2][1], blue[2][2] = red[2][0], red[2][1], red[2][2]
    red[2][0], red[2][1], red[2][2] = temp1, temp2, temp3

    down = np.rot90(down, -1)
    temp1, temp2, temp3 = front[2][0], front[2][1], front[2][2]
    front[2][0], front[2][1], front[2][2] = left[2][0], left[2][1], left[2][2]
    left[2][0], left[2][1], left[2][2] = back[2][0], back[2][1], back[2][2]
    back[2][0], back[2][1], back[2][2] = right[2][0], right[2][1], right[2][2]
    right[2][0], right[2][1], right[2][2] = temp1, temp2, temp3

    pieces = np.array([up, right, front, down, left, back])
    facelets = np.array([white, red, green, yellow, orange, blue])
    sol += 'd'

def l():
    global facelets
    global pieces
    global orange
    global left
    global sol

    orange = np.rot90(orange, -1)
    temp1, temp2, temp3 = green[0][0], green[1][0], green[2][0]
    green[0][0], green[1][0], green[2][0] = white[0][0], white[1][0], white[2][0]
    white[0][0], white[1][0], white[2][0] = blue[2][2], blue[1][2], blue[0][2]
    blue[2][2], blue[1][2], blue[0][2] = yellow[0][0], yellow[1][0], yellow[2][0]
    yellow[0][0], yellow[1][0], yellow[2][0] = temp1, temp2, temp3

    left = np.rot90(left, -1)
    temp1, temp2, temp3 = front[0][0], front[1][0], front[2][0]
    front[0][0], front[1][0], front[2][0] = up[0][0], up[1][0], up[2][0]
    up[0][0], up[1][0], up[2][0] = back[2][2], back[1][2], back[0][2]
    back[2][2], back[1][2], back[0][2] = down[0][0], down[1][0], down[2][0]
    down[0][0], down[1][0], down[2][0] = temp1, temp2, temp3

    pieces = np.array([up, right, front, down, left, back])
    facelets = np.array([white, red, green, yellow, orange, blue])
    sol += 'l'

def b():
    global facelets
    global pieces
    global blue
    global back
    global sol

    blue = np.rot90(blue, -1)
    temp1, temp2, temp3 = orange[0][0], orange[1][0], orange[2][0]
    orange[0][0], orange[1][0], orange[2][0] = white[0][2], white[0][1], white[0][0]
    white[0][2], white[0][1], white[0][0] = red[2][2], red[1][2], red[0][2]
    red[2][2], red[1][2], red[0][2] = yellow[2][0], yellow[2][1], yellow[2][2]
    yellow[2][0], yellow[2][1], yellow[2][2] = temp1, temp2, temp3

    back = np.rot90(back, -1)
    temp1, temp2, temp3 = left[0][0], left[1][0], left[2][0]
    left[0][0], left[1][0], left[2][0] = up[0][2], up[0][1], up[0][0]
    up[0][2], up[0][1], up[0][0] = right[2][2], right[1][2], right[0][2]
    right[2][2], right[1][2], right[0][2] = down[2][0], down[2][1], down[2][2]
    down[2][0], down[2][1], down[2][2] = temp1, temp2, temp3

    pieces = np.array([up, right, front, down, left, back])
    facelets = np.array([white, red, green, yellow, orange, blue])
    sol += 'b'

def solvecross():
    global sol
    sol = ''
    
    # move cross pieces to bottom layer
    if 1 in front[0:2] or 2 in front[0:2] or 3 in front[0:2] or 4 in front[0:2]:
        while 1 == front[2][1] or 2 == front[2][1] or 3 == front[2][1] or 4 == front[2][1]:
            d()
        while not 1 == front[2][1] and not 2 == front[2][1] and not 3 == front[2][1] and not 4 == front[2][1]:
            f()

    if 1 in right[0:2] or 2 in right[0:2] or 3 in right[0:2] or 4 in right[0:2]:
        while 1 == right[2][1] or 2 == right[2][1] or 3 == right[2][1] or 4 == right[2][1]:
            d()
        while not 1 == right[2][1] and not 2 == right[2][1] and not 3 == right[2][1] and not 4 == right[2][1]:
            r()

    if 1 in back[0:2] or 2 in back[0:2] or 3 in back[0:2] or 4 in back[0:2]:
        while 1 == back[2][1] or 2 == back[2][1] or 3 == back[2][1] or 4 == back[2][1]:
            d()
        while back[2][1] != 1 and back[2][1] != 2 and back[2][1] != 3 and back[2][1] != 4:
            b()

    if 1 in left[0:2] or 2 in left[0:2] or 3 in left[0:2] or 4 in left[0:2]:
        while 1 == left[2][1] or 2 == left[2][1] or 3 == left[2][1] or 4 == left[2][1]:
            d()
            print(sol)
        while left[2][1] != 1 and left[2][1] != 2 and left[2][1] != 3 and left[2][1] != 4:
            l()

# solve cross pieces
    gwloc = np.where(down == 1)
    gwi, gwj= int(gwloc[0].item()), int(gwloc[1].item())
    if yellow[gwi][gwj] == 'U':
        while front[2][1] != 1:
            d()
        f()
        f()
    else:
        while down[1][0] != 1:
            d()
        l()
        l()
        l()
        f()
        l()
    
    rwloc = np.where(down == 2)
    rwi, rwj= int(rwloc[0].item()), int(rwloc[1].item())
    print(down)
    print(yellow)
    if yellow[rwi][rwj] == 'U':
        while right[2][1] != 2:
            d()
        r()
        r()
    else:
        while down[0][1] != 2:
            d()
        f()
        f()
        f()
        r()
        f()

    bwloc = np.where(down == 3)
    bwi, bwj= int(bwloc[0].item()), int(bwloc[1].item())
    print(down)
    print(yellow)
    if yellow[bwi][bwj] == 'U':
        while back[2][1] != 3:
            d()
        b()
        b()
    else:
        while down[1][2] != 3:
            d()
        r()
        r()
        r()
        b()
        r()

    owloc = np.where(down == 4)
    owi, owj= int(owloc[0].item()), int(owloc[1].item())
    print(down)
    print(yellow)
    if yellow[owi][owj] == 'U':
        while left[2][1] != 4:
            d()
        l()
        l()
    else:
        while down[2][1] != 4:
            d()
        b()
        b()
        b()
        l()
        b()

    print(sol)

# test scramble
r()
d()
d()
r()
r()
b()
b()
d()
d()
f()
f()
d()
d()
d()
b()
b()
u()
b()
b()
u()
u()
u()
b()
b()
r()
r()
r()
u()
u()
u()
r()
r()
f()
f()
f()
l()
b()
b()
b()
l()
l()
u()
u()



while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'u':
                u()
            elif event.unicode == 'r':
                r()
            elif event.unicode == 'f':
                f()
            elif event.unicode == 'd':
                d()
            elif event.unicode == 'l':
                l()
            elif event.unicode == 'b':
                b()
            elif event.unicode == 'p':
                print(pieces)
            elif event.unicode == 't':
                list = []
                for i in facelets:
                    for j in i:
                        for k in j:
                            list.append(k)
                cubestring = ''.join(list)
                print(sv.solve(cubestring, 19, 3))
            elif event.unicode == 's':
                solvecross()

        if event.type == pygame.QUIT:
            quit()



    wx, wy = 230, 30
    yx, yy = 230, 430
    ox, oy = 30, 230

    disp = facelets.tolist()
    for i, face in enumerate(disp):
        for j, layer in enumerate(face):
            for k, facelet in enumerate(layer):
                if facelet == 'U':
                    disp[i][j][k] = 'white'
                elif facelet == 'R':
                    disp[i][j][k] = 'red'
                elif facelet == 'F':
                    disp[i][j][k] = 'green'
                elif facelet == 'D':
                    disp[i][j][k] = 'yellow'
                elif facelet == 'L':
                    disp[i][j][k] = 'orange'
                elif facelet == 'B':
                    disp[i][j][k] = 'blue'



    for i,layer in enumerate(disp[0]):
        for j, facelet in enumerate(layer):
            pygame.draw.rect(bg, facelet, (wx + j*60, wy + i*60, 50, 50), width=0)
    for i, face in enumerate([disp[4], disp[2], disp[1], disp[5]]):
        for j,layer in enumerate(face):
            for k, facelet in enumerate(layer):
                pygame.draw.rect(bg, facelet, (ox + k*60 + 200*i, oy + j*60, 50, 50), width=0)
    for i,layer in enumerate(disp[3]):
        for j, facelet in enumerate(layer):
            pygame.draw.rect(bg, facelet, (yx + j*60, yy + i*60, 50, 50), width=0)

    pygame.display.update()