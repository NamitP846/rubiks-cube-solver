import pygame
#import twophase.solver as sv
import copy

pygame.display.init()
bgsize = (830, 630)
bg = pygame.display.set_mode(bgsize, 0)
bg.fill('black')

sol = ''

ollcasefile = open('ollcases.txt', 'r')
ollcaselist = ollcasefile.read().splitlines()
ollalgfile = open('ollalgs.txt', 'r')
ollalglist = ollalgfile.read().splitlines()

facelets = [
    yellow:=[
    ['U', 'U', 'U'],
    ['U', 'U', 'U'],
    ['U', 'U', 'U']
],orange:=[
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
],green:=[
    ['F', 'F', 'F'],
    ['F', 'F', 'F'],
    ['F', 'F', 'F']
],white:=[
    ['D', 'D', 'D'],
    ['D', 'D', 'D'],
    ['D', 'D', 'D']
],red:=[
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L']
],blue:=[
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
]
]

pieces = [
    up:=[
    [13, 14, 15],
    [16, 26, 17],
    [18, 19, 20]
],right:=[
    [20, 17, 15],
    [6, 23, 8],
    [5, 2, 7]
],front:=[
    [18, 19, 20],
    [12, 21, 6],
    [11, 1, 5]
],down:=[
    [11, 1, 5],
    [4, 25, 2],
    [9, 3, 7]
],left:=[
    [13, 16, 18],
    [10, 24, 12],
    [9, 4, 11]
],back:=[
    [15, 14, 13],
    [8, 22, 10],
    [7, 3, 9]
]
]

def u():
    global facelets
    global pieces
    global yellow
    global up
    global sol

    yellow = rotate(yellow)
    temp1, temp2, temp3 = green[0][0], green[0][1], green[0][2]
    green[0][0], green[0][1], green[0][2] = orange[0][0], orange[0][1], orange[0][2]
    orange[0][0], orange[0][1], orange[0][2] = blue[0][0], blue[0][1], blue[0][2]
    blue[0][0], blue[0][1], blue[0][2] = red[0][0], red[0][1], red[0][2]
    red[0][0], red[0][1], red[0][2] = temp1, temp2, temp3

    up = rotate(up)
    temp1, temp2, temp3 = front[0][0], front[0][1], front[0][2]
    front[0][0], front[0][1], front[0][2] = right[0][0], right[0][1], right[0][2]
    right[0][0], right[0][1], right[0][2] = back[0][0], back[0][1], back[0][2]
    back[0][0], back[0][1], back[0][2] = left[0][0], left[0][1], left[0][2]
    left[0][0], left[0][1], left[0][2] = temp1, temp2, temp3

    pieces = [up, right, front, down, left, back]
    facelets = [yellow, orange, green, white, red, blue]
    sol += 'U'

def r():
    global facelets
    global pieces
    global orange
    global right
    global sol

    orange = rotate(orange)
    temp1, temp2, temp3 = green[0][2], green[1][2], green[2][2]
    green[0][2], green[1][2], green[2][2] = white[0][2], white[1][2], white[2][2]
    white[0][2], white[1][2], white[2][2] = blue[2][0], blue[1][0], blue[0][0]
    blue[2][0], blue[1][0], blue[0][0] = yellow[0][2], yellow[1][2], yellow[2][2]
    yellow[0][2], yellow[1][2], yellow[2][2] = temp1, temp2, temp3

    right = rotate(right)
    temp1, temp2, temp3 = front[0][2], front[1][2], front[2][2]
    front[0][2], front[1][2], front[2][2] = down[0][2], down[1][2], down[2][2]
    down[0][2], down[1][2], down[2][2] = back[2][0], back[1][0], back[0][0]
    back[2][0], back[1][0], back[0][0] = up[0][2], up[1][2], up[2][2]
    up[0][2], up[1][2], up[2][2] = temp1, temp2, temp3

    pieces = [up, right, front, down, left, back]
    facelets = [yellow, orange, green, white, red, blue]
    sol += 'R'

def f():
    global facelets
    global pieces
    global green
    global front
    global sol

    green = rotate(green)
    temp1, temp2, temp3 = white[0][0], white[0][1], white[0][2]
    white[0][0], white[0][1], white[0][2] = orange[2][0], orange[1][0], orange[0][0]
    orange[2][0], orange[1][0], orange[0][0] = yellow[2][2], yellow[2][1], yellow[2][0]
    yellow[2][2], yellow[2][1], yellow[2][0] = red[0][2], red[1][2], red[2][2]
    red[0][2], red[1][2], red[2][2] = temp1, temp2, temp3

    front = rotate(front)
    temp1, temp2, temp3 = down[0][0], down[0][1], down[0][2]
    down[0][0], down[0][1], down[0][2] = right[2][0], right[1][0], right[0][0]
    right[2][0], right[1][0], right[0][0] = up[2][2], up[2][1], up[2][0]
    up[2][2], up[2][1], up[2][0] = left[0][2], left[1][2], left[2][2]
    left[0][2], left[1][2], left[2][2] = temp1, temp2, temp3

    pieces = [up, right, front, down, left, back]
    facelets = [yellow, orange, green, white, red, blue]
    sol += 'F'

def d():
    global facelets
    global pieces
    global white
    global down
    global sol

    white = rotate(white)
    temp1, temp2, temp3 = green[2][0], green[2][1], green[2][2]
    green[2][0], green[2][1], green[2][2] = red[2][0], red[2][1], red[2][2]
    red[2][0], red[2][1], red[2][2] = blue[2][0], blue[2][1], blue[2][2]
    blue[2][0], blue[2][1], blue[2][2] = orange[2][0], orange[2][1], orange[2][2]
    orange[2][0], orange[2][1], orange[2][2] = temp1, temp2, temp3

    down = rotate(down)
    temp1, temp2, temp3 = front[2][0], front[2][1], front[2][2]
    front[2][0], front[2][1], front[2][2] = left[2][0], left[2][1], left[2][2]
    left[2][0], left[2][1], left[2][2] = back[2][0], back[2][1], back[2][2]
    back[2][0], back[2][1], back[2][2] = right[2][0], right[2][1], right[2][2]
    right[2][0], right[2][1], right[2][2] = temp1, temp2, temp3

    pieces = [up, right, front, down, left, back]
    facelets = [yellow, orange, green, white, red, blue]
    sol += 'D'

def l():
    global facelets
    global pieces
    global red
    global left
    global sol

    red = rotate(red)
    temp1, temp2, temp3 = green[0][0], green[1][0], green[2][0]
    green[0][0], green[1][0], green[2][0] = yellow[0][0], yellow[1][0], yellow[2][0]
    yellow[0][0], yellow[1][0], yellow[2][0] = blue[2][2], blue[1][2], blue[0][2]
    blue[2][2], blue[1][2], blue[0][2] = white[0][0], white[1][0], white[2][0]
    white[0][0], white[1][0], white[2][0] = temp1, temp2, temp3

    left = rotate(left)
    temp1, temp2, temp3 = front[0][0], front[1][0], front[2][0]
    front[0][0], front[1][0], front[2][0] = up[0][0], up[1][0], up[2][0]
    up[0][0], up[1][0], up[2][0] = back[2][2], back[1][2], back[0][2]
    back[2][2], back[1][2], back[0][2] = down[0][0], down[1][0], down[2][0]
    down[0][0], down[1][0], down[2][0] = temp1, temp2, temp3

    pieces = [up, right, front, down, left, back]
    facelets = [yellow, orange, green, white, red, blue]
    sol += 'L'

def b():
    global facelets
    global pieces
    global blue
    global back
    global sol

    blue = rotate(blue)
    temp1, temp2, temp3 = red[0][0], red[1][0], red[2][0]
    red[0][0], red[1][0], red[2][0] = yellow[0][2], yellow[0][1], yellow[0][0]
    yellow[0][2], yellow[0][1], yellow[0][0] = orange[2][2], orange[1][2], orange[0][2]
    orange[2][2], orange[1][2], orange[0][2] = white[2][0], white[2][1], white[2][2]
    white[2][0], white[2][1], white[2][2] = temp1, temp2, temp3

    back = rotate(back)
    temp1, temp2, temp3 = left[0][0], left[1][0], left[2][0]
    left[0][0], left[1][0], left[2][0] = up[0][2], up[0][1], up[0][0]
    up[0][2], up[0][1], up[0][0] = right[2][2], right[1][2], right[0][2]
    right[2][2], right[1][2], right[0][2] = down[2][0], down[2][1], down[2][2]
    down[2][0], down[2][1], down[2][2] = temp1, temp2, temp3

    pieces = [up, right, front, down, left, back]
    facelets = [yellow, orange, green, white, red, blue]
    sol += 'B'

def move(str, rot = 0, scr = False):
    str = list(str)
    moves = ['F', 'R', 'B', 'L']
    for i, let in enumerate(str):
        rep = 1
        if let == 'F' or let == 'R' or let == 'B' or let == 'L':
            moves.index(let)
            let = moves[(moves.index(let) + rot)%4]
        if let.isalpha() and i != len(str)-1:
            if str[i+1] == ' ':
                rep = 1
            elif str[i+1] == '2':
                rep = 2
            elif str[i+1] == "'":
                rep = 3
        if let == 'U':
            if scr:
                for x in range(rep):
                    d()
            else:
                for x in range(rep):
                    u()
        elif let == 'R':
            if scr:
                for x in range(rep):
                    l()
            else:
                for x in range(rep):
                    r()
        elif let == 'F':
            for x in range(rep):
                f()
        elif let == 'D':
            if scr:
                for x in range(rep):
                    u()
            else:
                for x in range(rep):
                    d()
        elif let == 'L':
            if scr:
                for x in range(rep):
                    r()
            else:
                for x in range(rep):
                    l()
        elif let == 'B':
            for x in range(rep):
                b()

def rotate(face):
    rotatedface = [[face[2][0], face[1][0], face[0][0]],
                   [face[2][1], face[1][1], face[0][1]],
                   [face[2][2], face[1][2], face[0][2]]
    ]
    return(rotatedface)

def find(face, piecenum):
    for x, row in enumerate(face):
        for y, piece in enumerate(row):
            if piece == piecenum:
                return(x, y)
    print(sol)

def inface(face, piecenum):
    for row in face:
        for piece in row:
            if piece == piecenum:
                return(True)
    return(False)

def solvecross():
    global sol
    sol = ''
    # move cross pieces to yellow layer
    while inface(front[1:3], 1) or inface(front[1:3], 2) or inface(front[1:3], 3) or inface(front[1:3], 4):
        while 1 == front[0][1] or 2 == front[0][1] or 3 == front[0][1] or 4 == front[0][1]:
            u()
        while front[0][1] != 1 and 2 != front[0][1] and 3 != front[0][1] and 4 != front[0][1]:
            f()

    while inface(back[1:3], 1) or inface(back[1:3], 2) or inface(back[1:3], 3) or inface(back[1:3], 4):
        while 1 == back[0][1] or 2 == back[0][1] or 3 == back[0][1] or 4 == back[0][1]:
            u()
        while back[0][1] != 1 and back[0][1] != 2 and back[0][1] != 3 and back[0][1] != 4:
            b()

    while right[2][1] == 1 or right[2][1] == 2 or right[2][1] == 3 or right [2][1] == 4:
        while 1 == right[0][1] or 2 == right[0][1] or 3 == right[0][1] or 4 == right[0][1]:
            u()
        r()
        r()

    while left[2][1] == 1 or left[2][1] == 2 or left[2][1] == 3 or left[2][1] == 4:
        while 1 == left[0][1] or 2 == left[0][1] or 3 == left[0][1] or 4 == left[0][1]:
            u()
        l()
        l()

    gwi, gwj = find(up, 1)
    if yellow[gwi][gwj] == 'D':
        while up[2][1] != 1:
            u()
        f()
        f()
    else:
        while up[1][2] != 1:
            u()
        r()
        r()
        r()
        f()
        r()

    owi, owj = find(up, 2)
    if yellow[owi][owj] == 'D':
        while up[1][2] != 2:
            u()
        r()
        r()
    else:
        while up[0][1] != 2:
            u()
        b()
        b()
        b()
        r()
        b()

    bwi, bwj = find(up, 3)
    if yellow[bwi][bwj] == 'D':
        while up[0][1] != 3:
            u()
        b()
        b()
    else:
        while up[1][0] != 3:
            u()
        l()
        l()
        l()
        b()
        l()

    rwi, rwj = find(up, 4)
    if yellow[rwi][rwj] == 'D':
        while up[1][0] != 4:
            u()
        l()
        l()
    else:
        while up[2][1] != 4:
            u()
        f()
        f()
        f()
        l()
        f()

def solvef2l():
    global sol

    if 5 == back[0][0]:
        move("R D R'")
    elif 5 == back[0][2]:
        move("L' D L")
    elif 5 == front[0][2]:
        move("R' D R")
    if inface(down, 5):
        while front[2][0] != 5:
            d()
        if green[2][0] == "F":
            move("L D L'")
        elif green[2][0] == "L":
            move("L D2 L' D' L D L'")
        else:
            move("F' D' F")
    else:
        if green[0][0] == "U":
            move("F' D' F D F' D' F")
        elif green[0][0] == "L":
            move("L D L' D' L D L'")


    if 7 == back[0][0]:
        move("R D R'")
    elif 7 == back[0][2]:
        move("L' D L")
    if inface(down, 7):
        while front[2][2] != 7:
            d()
        if green[2][2] == "F":
            move("R' D' R")
        elif green[2][2] == "R":
            move("R' D2 R D R' D' R")
        else:
            move("F D F'")
    else:
        if green[0][2] == "U":
            move("F D F' D' F D F'")
        elif green[0][2] == "L":
            move("R' D' R D R' D' R")


    if 9 == back[0][2]:
        move("L' D L")
    if inface(down, 9):
        while back[2][0] != 9:
            d()
        if blue[2][0] == "B":
            move("R D R'")
        elif blue[2][0] == "R":
            move("R D2 R' D' R D R'")
        else:
            move("B' D' B")
    else:
        if blue[0][0] == "U":
            move("B' D' B D B' D' B")
        elif blue[0][0] == "R":
            move("R D R' D' R D R'")


    if inface(down, 11):
        while back[2][2] != 11:
            d()
        if blue[2][2] == "B":
            move("L' D' L")
        elif blue[2][2] == "L":
            move("L' D2 L D L' D' L")
        else:
            move("B D B'")
    else:
        if blue[0][0] == "U":
            move("B D B' D' B D B'")
        elif blue[0][0] == "L":
            move("L' D' L D L' D' L")



    if front[1][0] == 6 and green[1][0] == "G":
        pass
    else:
        if front[1][0] == 6:
            move("L D L' D' F' D' F")
        elif front[1][2] == 6:
            move("R' D' R D F D F'")
        elif back[1][0] == 6:
            move("R D R' D' B' D' B")
        elif back[1][2] == 6:
            move("L' D' L D B D B'")
        ogi, ogj = find(down, 6)
        if yellow[ogi][ogj] == "L":
            while down[1][2] != 6:
                d()
            move("L D' L' F L' F' L")
        else:
            while down[2][1] != 6:
                d()
            move("F' D F L' F L F'")


    if front[1][2] == 8 and green[1][2] == "G":
        pass
    else:
        if front[1][2] == 8:
            move("R' D' R D F D F'")
        elif back[1][0] == 8:
            move("R D R' D' B' D' B")
        elif back[1][2] == 8:
            move("L' D' L D B D B'")
        rgi, rgj = find(down, 8)
        if yellow[rgi][rgj] == "R":
            while down[1][0] != 8:
                d()
            move("R' D R F' R F R'")
        else:
            while down[2][1] != 8:
                d()
            move("F D' F' R F' R' F")


    if back[1][0] == 10 and blue[1][0] == "B":
        pass
    else:
        if back[1][0] == 10:
            move("R D R' D' B' D' B")
        elif back[1][2] == 10:
            move("L' D' L D B D B'")
        rbi, rbj = find(down, 10)
        if yellow[rbi][rbj] == "R":
            while down[1][0] != 10:
                d()
            move("R D' R' B R' B' R")
        else:
            while down[0][1] != 10:
                d()
            move("B' D B R' B R B'")


    if back[1][2] == 12 and blue[1][2] == "B":
        pass
    else:
        if back[1][2] == 12:
            move("L' D' L D B D B'")
        obi, obj = find(down, 12)
        if yellow[obi][obj] == "L":
            while down[1][2] != 12:
                d()
            move("L' D L B' L B L'")
        else:
            while down[0][1] != 12:
                d()
            move("B D' B' L B' L' B")

def solveoll():
    oll = green[0] + orange[0] + blue[0] + red[0]
    for i in range(4):
        for j, facelet in enumerate(oll):
            if facelet != 'U':
                oll[j] = 'N'
        for k, ollcase in enumerate(ollcaselist):
            if ''.join(oll) == ollcase:
                move(ollalglist[k], rot = i)
                return
        oll = oll[3:] + oll[0:3]


# test scramble
#scramble = input("Scramble: ")
scramble = "B D2 B' D2 F D2 F' D2 L2 U F2 L' F L U' L2"
move(scramble)

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
            elif event.unicode == 's':
                sol = ''
#                cubestring = []
#                for i in facelets:
#                    for j in i:
#                        for k in j:
#                            cubestring.append(k)
#                cubestring = ''.join(cubestring)
#                optsol = sv.solve(cubestring, 20, 1)
#                optsol = list(optsol)
#                scramble = []
#                for i in optsol:
#                    if i.isnumeric():
#                        i = str(4-int(i))
#                    scramble.append(i)
#                scramble.reverse()
#                print('Scramble:', ''.join(scramble[6:]))
#                print('Optimal Sol:', ''.join(optsol))
                #solvecross()
                #solvef2l()
                asdf = solveoll()
                print(asdf)
                sol = list(sol)
                solstring = []
                j = 1
                movecount = 1
                for i, turn in enumerate(sol[0:-1]):
                    if sol[i] == sol[i+1]:
                        sol[i] = ' '
                        j += 1
                    else:
                        j = j % 4
                        if j == 3:
                            j = "'"
                        elif j == 1:
                            j = ' '
                        solstring.append(turn)
                        solstring.append(str(j))
                        solstring.append(' ')
                        movecount += 1
                        j = 1
                solstring.append(sol[-1])
                j = j % 4
                if j == 3:
                    j = "'"
                elif j == 1:
                    j = ' '
                solstring.append(str(j))
                solstring.append(' ')
                solstring = ''.join(solstring)
                print(solstring)
                print('movecount: ', movecount)

        if event.type == pygame.QUIT:
            quit()



    wx, wy = 230, 30
    yx, yy = 230, 430
    ox, oy = 30, 230

    disp = copy.deepcopy(facelets)
    for i, face in enumerate(disp):
        for j, layer in enumerate(face):
            for k, facelet in enumerate(layer):
                if facelet == 'U':
                    disp[i][j][k] = 'yellow'
                elif facelet == 'R':
                    disp[i][j][k] = 'orange'
                elif facelet == 'F':
                    disp[i][j][k] = 'green'
                elif facelet == 'D':
                    disp[i][j][k] = 'white'
                elif facelet == 'L':
                    disp[i][j][k] = 'red'
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