import pygame
#import twophase.solver as sv
import copy
import random

pygame.display.init()
bgsize = (830, 630)
bg = pygame.display.set_mode(bgsize, 0)
bg.fill('black')

sol = ''

ollcasefile = open('ollcases.txt', 'r')
ollcaselist = ollcasefile.read().splitlines()
ollalgfile = open('ollalgs.txt', 'r')
ollalglist = ollalgfile.read().splitlines()

pllcasefile = open('pllcases.txt', 'r')
pllcaselist = pllcasefile.read().splitlines()
pllalgfile = open('pllalgs.txt', 'r')
pllalglist = pllalgfile.read().splitlines()

f2lcasefile = open('f2lcases.txt', 'r')
f2lcaselist = f2lcasefile.read().splitlines()
f2lalgfile = open('f2lalgs.txt', 'r')
f2lalglist = f2lalgfile.read().splitlines()

crosscasefile = open('crosscases.txt', 'r')
crosscaselist = crosscasefile.read().splitlines()
crossalgfile = open('crossalgs.txt', 'r')
crossalglist = crossalgfile.read().splitlines()

permutations = [
    [1, 2, 3, 0],
    [1, 2, 0, 3],
    [1, 3, 2, 0],
    [1, 3, 0, 2],
    [1, 0, 2, 3],
    [1, 0, 3, 2],
    [2, 1, 3, 0],
    [2, 1, 0, 3],
    [2, 3, 1, 0],
    [2, 3, 0, 1],
    [2, 0, 1, 3],
    [2, 0, 3, 1],
    [3, 1, 2, 0],
    [3, 1, 0, 2],
    [3, 2, 1, 0],
    [3, 2, 0, 1],
    [3, 0, 1, 2],
    [3, 0, 2, 1],
    [0, 1, 2, 3],
    [0, 1, 3, 2],
    [0, 2, 1, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2],
    [0, 3, 2, 1]
]

facelets = [
    [
    ['U', 'U', 'U'],
    ['U', 'U', 'U'],
    ['U', 'U', 'U']
],[
    ['R', 'R', 'R'],
    ['R', 'R', 'R'],
    ['R', 'R', 'R']
],[
    ['F', 'F', 'F'],
    ['F', 'F', 'F'],
    ['F', 'F', 'F']
],[
    ['D', 'D', 'D'],
    ['D', 'D', 'D'],
    ['D', 'D', 'D']
],[
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L']
],[
    ['B', 'B', 'B'],
    ['B', 'B', 'B'],
    ['B', 'B', 'B']
]
]

pieces = [
    [
    [13, 14, 15],
    [16, 26, 17],
    [18, 19, 20]
],[
    [20, 17, 15],
    [6, 23, 8],
    [5, 2, 7]
],[
    [18, 19, 20],
    [12, 21, 6],
    [11, 1, 5]
],[
    [11, 1, 5],
    [4, 25, 2],
    [9, 3, 7]
],[
    [13, 16, 18],
    [10, 24, 12],
    [9, 4, 11]
],[
    [15, 14, 13],
    [8, 22, 10],
    [7, 3, 9]
]
]

solvedfacelets = copy.deepcopy(facelets)

def u(cubefacelets, cubepieces):
    cubefacelets[0] = rotate(cubefacelets[0])
    temp1, temp2, temp3 = cubefacelets[2][0][0], cubefacelets[2][0][1], cubefacelets[2][0][2]
    cubefacelets[2][0][0], cubefacelets[2][0][1], cubefacelets[2][0][2] = cubefacelets[1][0][0], cubefacelets[1][0][1], cubefacelets[1][0][2]
    cubefacelets[1][0][0], cubefacelets[1][0][1], cubefacelets[1][0][2] = cubefacelets[5][0][0], cubefacelets[5][0][1], cubefacelets[5][0][2]
    cubefacelets[5][0][0], cubefacelets[5][0][1], cubefacelets[5][0][2] = cubefacelets[4][0][0], cubefacelets[4][0][1], cubefacelets[4][0][2]
    cubefacelets[4][0][0], cubefacelets[4][0][1], cubefacelets[4][0][2] = temp1, temp2, temp3

    cubepieces[0] = rotate(cubepieces[0])
    temp1, temp2, temp3 = cubepieces[2][0][0], cubepieces[2][0][1], cubepieces[2][0][2]
    cubepieces[2][0][0], cubepieces[2][0][1], cubepieces[2][0][2] = cubepieces[1][0][0], cubepieces[1][0][1], cubepieces[1][0][2]
    cubepieces[1][0][0], cubepieces[1][0][1], cubepieces[1][0][2] = cubepieces[5][0][0], cubepieces[5][0][1], cubepieces[5][0][2]
    cubepieces[5][0][0], cubepieces[5][0][1], cubepieces[5][0][2] = cubepieces[4][0][0], cubepieces[4][0][1], cubepieces[4][0][2]
    cubepieces[4][0][0], cubepieces[4][0][1], cubepieces[4][0][2] = temp1, temp2, temp3

    return cubefacelets, cubepieces

def r(cubefacelets, cubepieces):
    cubefacelets[1] = rotate(cubefacelets[1])
    temp1, temp2, temp3 = cubefacelets[2][0][2], cubefacelets[2][1][2], cubefacelets[2][2][2]
    cubefacelets[2][0][2], cubefacelets[2][1][2], cubefacelets[2][2][2] = cubefacelets[3][0][2], cubefacelets[3][1][2], cubefacelets[3][2][2]
    cubefacelets[3][0][2], cubefacelets[3][1][2], cubefacelets[3][2][2] = cubefacelets[5][2][0], cubefacelets[5][1][0], cubefacelets[5][0][0]
    cubefacelets[5][2][0], cubefacelets[5][1][0], cubefacelets[5][0][0] = cubefacelets[0][0][2], cubefacelets[0][1][2], cubefacelets[0][2][2]
    cubefacelets[0][0][2], cubefacelets[0][1][2], cubefacelets[0][2][2] = temp1, temp2, temp3

    cubepieces[1] = rotate(cubepieces[1])
    temp1, temp2, temp3 = cubepieces[2][0][2], cubepieces[2][1][2], cubepieces[2][2][2]
    cubepieces[2][0][2], cubepieces[2][1][2], cubepieces[2][2][2] = cubepieces[3][0][2], cubepieces[3][1][2], cubepieces[3][2][2]
    cubepieces[3][0][2], cubepieces[3][1][2], cubepieces[3][2][2] = cubepieces[5][2][0], cubepieces[5][1][0], cubepieces[5][0][0]
    cubepieces[5][2][0], cubepieces[5][1][0], cubepieces[5][0][0] = cubepieces[0][0][2], cubepieces[0][1][2], cubepieces[0][2][2]
    cubepieces[0][0][2], cubepieces[0][1][2], cubepieces[0][2][2] = temp1, temp2, temp3

    return cubefacelets, cubepieces

def f(cubefacelets, cubepieces):
    cubefacelets[2] = rotate(cubefacelets[2])
    temp1, temp2, temp3 = cubefacelets[3][0][0], cubefacelets[3][0][1], cubefacelets[3][0][2]
    cubefacelets[3][0][0], cubefacelets[3][0][1], cubefacelets[3][0][2] = cubefacelets[1][2][0], cubefacelets[1][1][0], cubefacelets[1][0][0]
    cubefacelets[1][2][0], cubefacelets[1][1][0], cubefacelets[1][0][0] = cubefacelets[0][2][2], cubefacelets[0][2][1], cubefacelets[0][2][0]
    cubefacelets[0][2][2], cubefacelets[0][2][1], cubefacelets[0][2][0] = cubefacelets[4][0][2], cubefacelets[4][1][2], cubefacelets[4][2][2]
    cubefacelets[4][0][2], cubefacelets[4][1][2], cubefacelets[4][2][2] = temp1, temp2, temp3

    cubepieces[2] = rotate(cubepieces[2])
    temp1, temp2, temp3 = cubepieces[3][0][0], cubepieces[3][0][1], cubepieces[3][0][2]
    cubepieces[3][0][0], cubepieces[3][0][1], cubepieces[3][0][2] = cubepieces[1][2][0], cubepieces[1][1][0], cubepieces[1][0][0]
    cubepieces[1][2][0], cubepieces[1][1][0], cubepieces[1][0][0] = cubepieces[0][2][2], cubepieces[0][2][1], cubepieces[0][2][0]
    cubepieces[0][2][2], cubepieces[0][2][1], cubepieces[0][2][0] = cubepieces[4][0][2], cubepieces[4][1][2], cubepieces[4][2][2]
    cubepieces[4][0][2], cubepieces[4][1][2], cubepieces[4][2][2] = temp1, temp2, temp3

    return cubefacelets, cubepieces

def d(cubefacelets, cubepieces):
    cubefacelets[3] = rotate(cubefacelets[3])
    temp1, temp2, temp3 = cubefacelets[2][2][0], cubefacelets[2][2][1], cubefacelets[2][2][2]
    cubefacelets[2][2][0], cubefacelets[2][2][1], cubefacelets[2][2][2] = cubefacelets[4][2][0], cubefacelets[4][2][1], cubefacelets[4][2][2]
    cubefacelets[4][2][0], cubefacelets[4][2][1], cubefacelets[4][2][2] = cubefacelets[5][2][0], cubefacelets[5][2][1], cubefacelets[5][2][2]
    cubefacelets[5][2][0], cubefacelets[5][2][1], cubefacelets[5][2][2] = cubefacelets[1][2][0], cubefacelets[1][2][1], cubefacelets[1][2][2]
    cubefacelets[1][2][0], cubefacelets[1][2][1], cubefacelets[1][2][2] = temp1, temp2, temp3

    cubepieces[3] = rotate(cubepieces[3])
    temp1, temp2, temp3 = cubepieces[2][2][0], cubepieces[2][2][1], cubepieces[2][2][2]
    cubepieces[2][2][0], cubepieces[2][2][1], cubepieces[2][2][2] = cubepieces[4][2][0], cubepieces[4][2][1], cubepieces[4][2][2]
    cubepieces[4][2][0], cubepieces[4][2][1], cubepieces[4][2][2] = cubepieces[5][2][0], cubepieces[5][2][1], cubepieces[5][2][2]
    cubepieces[5][2][0], cubepieces[5][2][1], cubepieces[5][2][2] = cubepieces[1][2][0], cubepieces[1][2][1], cubepieces[1][2][2]
    cubepieces[1][2][0], cubepieces[1][2][1], cubepieces[1][2][2] = temp1, temp2, temp3

    return cubefacelets, cubepieces

def l(cubefacelets, cubepieces):
    cubefacelets[4] = rotate(cubefacelets[4])
    temp1, temp2, temp3 = cubefacelets[2][0][0], cubefacelets[2][1][0], cubefacelets[2][2][0]
    cubefacelets[2][0][0], cubefacelets[2][1][0], cubefacelets[2][2][0] = cubefacelets[0][0][0], cubefacelets[0][1][0], cubefacelets[0][2][0]
    cubefacelets[0][0][0], cubefacelets[0][1][0], cubefacelets[0][2][0] = cubefacelets[5][2][2], cubefacelets[5][1][2], cubefacelets[5][0][2]
    cubefacelets[5][2][2], cubefacelets[5][1][2], cubefacelets[5][0][2] = cubefacelets[3][0][0], cubefacelets[3][1][0], cubefacelets[3][2][0]
    cubefacelets[3][0][0], cubefacelets[3][1][0], cubefacelets[3][2][0] = temp1, temp2, temp3

    cubepieces[4] = rotate(cubepieces[4])
    temp1, temp2, temp3 = cubepieces[2][0][0], cubepieces[2][1][0], cubepieces[2][2][0]
    cubepieces[2][0][0], cubepieces[2][1][0], cubepieces[2][2][0] = cubepieces[0][0][0], cubepieces[0][1][0], cubepieces[0][2][0]
    cubepieces[0][0][0], cubepieces[0][1][0], cubepieces[0][2][0] = cubepieces[5][2][2], cubepieces[5][1][2], cubepieces[5][0][2]
    cubepieces[5][2][2], cubepieces[5][1][2], cubepieces[5][0][2] = cubepieces[3][0][0], cubepieces[3][1][0], cubepieces[3][2][0]
    cubepieces[3][0][0], cubepieces[3][1][0], cubepieces[3][2][0] = temp1, temp2, temp3

    return cubefacelets, cubepieces

def b(cubefacelets, cubepieces):
    cubefacelets[5] = rotate(cubefacelets[5])
    temp1, temp2, temp3 = cubefacelets[4][0][0], cubefacelets[4][1][0], cubefacelets[4][2][0]
    cubefacelets[4][0][0], cubefacelets[4][1][0], cubefacelets[4][2][0] = cubefacelets[0][0][2], cubefacelets[0][0][1], cubefacelets[0][0][0]
    cubefacelets[0][0][2], cubefacelets[0][0][1], cubefacelets[0][0][0] = cubefacelets[1][2][2], cubefacelets[1][1][2], cubefacelets[1][0][2]
    cubefacelets[1][2][2], cubefacelets[1][1][2], cubefacelets[1][0][2] = cubefacelets[3][2][0], cubefacelets[3][2][1], cubefacelets[3][2][2]
    cubefacelets[3][2][0], cubefacelets[3][2][1], cubefacelets[3][2][2] = temp1, temp2, temp3

    cubepieces[5] = rotate(cubepieces[5])
    temp1, temp2, temp3 = cubepieces[4][0][0], cubepieces[4][1][0], cubepieces[4][2][0]
    cubepieces[4][0][0], cubepieces[4][1][0], cubepieces[4][2][0] = cubepieces[0][0][2], cubepieces[0][0][1], cubepieces[0][0][0]
    cubepieces[0][0][2], cubepieces[0][0][1], cubepieces[0][0][0] = cubepieces[1][2][2], cubepieces[1][1][2], cubepieces[1][0][2]
    cubepieces[1][2][2], cubepieces[1][1][2], cubepieces[1][0][2] = cubepieces[3][2][0], cubepieces[3][2][1], cubepieces[3][2][2]
    cubepieces[3][2][0], cubepieces[3][2][1], cubepieces[3][2][2] = temp1, temp2, temp3
    
    return cubefacelets, cubepieces

def move(cubefacelets, cubepieces, movestr, rotation = 0, scr = False):
    global sol
    movestr = list(movestr)
    moves = ['F', 'R', 'B', 'L']
    for i, let in enumerate(movestr):
        rep = 1
        movelet = let
        if let == 'F' or let == 'R' or let == 'B' or let == 'L':
            movelet = moves[(moves.index(let) + rotation)%4]
        if let.isalpha():
            rep = int(movestr[i+1])
            sol = f'{sol}{movelet}{rep} '
        if movelet == 'U':
            if scr:
                for x in range(rep):
                    cubefacelets, cubepieces = d(cubefacelets, cubepieces)
            else:
                for x in range(rep):
                    cubefacelets, cubepieces = u(cubefacelets, cubepieces)
        elif movelet == 'R':
            if scr:
                for x in range(rep):
                    cubefacelets, cubepieces = l(cubefacelets, cubepieces)
            else:
                for x in range(rep):
                    cubefacelets, cubepieces = r(cubefacelets, cubepieces)
        elif movelet == 'F':
            for x in range(rep):
                cubefacelets, cubepieces = f(cubefacelets, cubepieces)
        elif movelet == 'D':
            if scr:
                for x in range(rep):
                    cubefacelets, cubepieces = u(cubefacelets, cubepieces)
            else:
                for x in range(rep):
                    cubefacelets, cubepieces = d(cubefacelets, cubepieces)
        elif movelet == 'L':
            if scr:
                for x in range(rep):
                    cubefacelets, cubepieces = r(cubefacelets, cubepieces)
            else:
                for x in range(rep):
                    cubefacelets, cubepieces = l(cubefacelets, cubepieces)
        elif movelet == 'B':
            for x in range(rep):
                cubefacelets, cubepieces = b(cubefacelets, cubepieces)
    rotation = 0

def rev(revstr):
    revstr = revstr.split()
    revstr.reverse()
    revstr = ' '.join(revstr)
    revstr = list(revstr)
    for i, x in enumerate(revstr):
        if x.isalpha() and i != len(revstr) - 1:
            if revstr[i+1] == "'":
                revstr[i+1] = ' '
            elif revstr[i+1] == ' ':
                revstr[i+1] = "'"
        elif x.isalpha() and i == len(revstr) - 1:
            revstr.append("'")
    revstr = ''.join(revstr)
    return(revstr)

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

def solvecrosspiece(cubefacelets, cubepieces, rot):
    global sol
    edge = rot + 1
    edgeloc = ''

    faceletfaces = [cubefacelets[2], cubefacelets[1], cubefacelets[5], cubefacelets[4]]
    piecenumfaces = [cubepieces[2], cubepieces[1], cubepieces[5], cubepieces[4]]

    if inface(piecenumfaces[rot], edge):
        edgeloc += 'F'
    elif inface(piecenumfaces[(rot+2)%4], edge):
        edgeloc += 'B'
    if inface(cubepieces[0], edge):
        edgeloc += 'U'
        edgei, edgej = find(cubepieces[0], edge)
        if cubefacelets[0][edgei][edgej] == 'D':
            edgeorientation = 'G'
        else:
            edgeorientation = 'B'
    elif inface(cubepieces[3], edge):
        edgeloc += 'D'
        edgei, edgej = find(cubepieces[3], edge)
        if cubefacelets[3][edgei][edgej] == 'D':
            edgeorientation = 'G'
        else:
            edgeorientation = 'B'
    if inface(piecenumfaces[(rot+1)%4], edge):
        edgeloc += 'R'
        edgei, edgej = find(piecenumfaces[(rot+1)%4], edge)
        if faceletfaces[(rot+1)%4][edgei][edgej] == 'D':
            edgeorientation = 'B'
        else:
            edgeorientation = 'G'
    elif inface(piecenumfaces[(rot+3)%4], edge):
        edgei, edgej = find(piecenumfaces[(rot+3)%4], edge)
        if faceletfaces[(rot+3)%4][edgei][edgej] == 'D':
            edgeorientation = 'B'
        else:
            edgeorientation = 'G'
        edgeloc += 'L'
    
    edgecase = f'{edgeloc}{edgeorientation}'
    for k, crosscase in enumerate(crosscaselist):
        if ''.join(edgecase) == crosscase:
            move(cubefacelets, cubepieces, crossalglist[k], rotation = rot)
            print(f'Cross Piece {rot} Solved - {sol}')
            return
    

def solvef2lpair(cubefacelets, cubepieces, rot):
    corner, edge = rot*2+5, rot*2+6
    colors = ['F', 'R', 'B', 'L']
    faceletfaces = [cubefacelets[2], cubefacelets[1], cubefacelets[5], cubefacelets[4]]
    piecenumfaces = [cubepieces[2], cubepieces[1], cubepieces[5], cubepieces[4]]

    if piecenumfaces[rot][2][2] == corner:
        cornerloc = 'D'
        if faceletfaces[rot][2][2] == 'D':
            cornerorientation = 'W'
        elif faceletfaces[rot][2][2] == colors[rot]:
            cornerorientation = 'F'
        else:
            cornerorientation = 'R'
    else:
        cornerloc = 'U'
        if inface(cubepieces[0], corner):
            while piecenumfaces[rot][0][2] != corner:
                move(cubefacelets, cubepieces, "U1 ")
        elif piecenumfaces[rot][2][0] == corner:
            move(cubefacelets, cubepieces, "L3 U3 L1 ", rot)
        elif piecenumfaces[(rot+2)%4][2][0] == corner:
            move(cubefacelets, cubepieces, "R3 U1 R1 U1 ", rot)
        elif piecenumfaces[(rot+2)%4][2][2] == corner:
            move(cubefacelets, cubepieces, "L1 U2 L3 ", rot)
        if faceletfaces[rot][0][2] == 'D':
            cornerorientation = 'W'
        elif faceletfaces[rot][0][2] == colors[rot]:
            cornerorientation = 'F'
        else:
            cornerorientation = 'R'

    faceletfaces = [cubefacelets[2], cubefacelets[1], cubefacelets[5], cubefacelets[4]]
    piecenumfaces = [cubepieces[2], cubepieces[1], cubepieces[5], cubepieces[4]]

    if inface(piecenumfaces[rot], edge):
        edgei, edgej = find(piecenumfaces[rot], edge)
        if edgei == 0:
            edgeloc = 4
            if faceletfaces[rot][edgei][edgej] == colors[rot]:
                edgeorientation = 'B'
            else:
                edgeorientation = 'G'
        else:
            if faceletfaces[rot][edgei][edgej] == colors[rot]:
                edgeorientation = 'G'
            else:
                edgeorientation = 'B'
            if edgej == 0:
                edgeloc = 8
            else:
                edgeloc = 5
    elif inface(piecenumfaces[(rot+2)%4], edge):
        edgei, edgej = find(piecenumfaces[(rot+2)%4], edge)
        if edgei == 0:
            edgeloc = 2
            if faceletfaces[(rot+2)%4][edgei][edgej] == colors[rot]:
                edgeorientation = 'B'
            else:
                edgeorientation = 'G'
        else:
            if faceletfaces[(rot+2)%4][edgei][edgej] == colors[rot]:
                edgeorientation = 'G'
            else:
                edgeorientation = 'B'
            if edgej == 0:
                edgeloc = 6
            else:
                edgeloc = 7
    elif inface(piecenumfaces[(rot+1)%4], edge):
        edgeloc = 1
        if faceletfaces[(rot+1)%4][0][1] == colors[rot]:
            edgeorientation = 'B'
        else:
            edgeorientation = 'G'
    elif inface(piecenumfaces[(rot-1)%4], edge):
        edgeloc = 3
        if faceletfaces[(rot-1)%4][0][1] == colors[rot]:
            edgeorientation = 'B'
        else:
            edgeorientation = 'G'
    else:
        print(sol)
        print('edge', edge, 'not found')
        print(pieces)
        print(facelets)
    
    f2l = cornerloc + cornerorientation + ' ' + str(edgeloc) + edgeorientation
    for k, f2lcase in enumerate(f2lcaselist):
        if ''.join(f2l) == f2lcase:
            move(cubefacelets, cubepieces, f2lalglist[k], rotation = rot)
            print(f'Pair {rot} solved ({f2lcaselist[k]}) - {sol}')
            return

def solveoll(cubefacelets, cubepieces):
    global sol
    oll = cubefacelets[2][0] + cubefacelets[1][0] + cubefacelets[5][0] + cubefacelets[4][0]
    for j, facelet in enumerate(oll):
        if facelet != 'U':
            oll[j] = 'N'
    for i in range(4):
        for k, ollcase in enumerate(ollcaselist):
            if ''.join(oll) == ollcase:
                move(cubefacelets, cubepieces, ollalglist[k], rotation = i)
                print('oll solved -', sol)
                return
        oll = oll[3:] + oll[0:3]

def solvepll(cubefacelets, cubepieces):
    pll = cubefacelets[2][0] + cubefacelets[1][0] + cubefacelets[5][0] + cubefacelets[4][0]
    colors = ['F', 'R', 'B', 'L']
    for i in range(4):
        for j in range(4):
            for k, pllcase in enumerate(pllcaselist):
                if ''.join(pll) == pllcase:
                    move(cubefacelets, cubepieces, pllalglist[k], rotation = j)
                    print('pll solved -', sol)
                    return
            pll = pll[3:] + pll[0:3]
        for l, facelet in enumerate(pll):
            colors.index(facelet)
            pll[l] = colors[(colors.index(facelet) + 1)%4]

def auf(cubefacelets, cubepieces):
    while cubefacelets[2][0][0] != 'F':
        move(cubefacelets, cubepieces, "U1 ")

def genrandscramble():
    scr = ''
    moves = ['R', 'U', 'F', 'L', 'B', 'D']
    reps = ['1', '2', '3']
    for i in range(20):
        scr += random.choice(moves)
        scr += random.choice(reps)
        scr += ' '
    return scr

# test scramble
#scramble = ""
#move(facelets, pieces, scramble, scr=True)

totalmoves = 0

for x in range(100):
    randomscramble = genrandscramble()
    print(randomscramble)
    move(facelets, pieces, "L3 U1 R2 U2 R2 B2 L3 U2 B2 L3 D2 B1 D1 F1 R2 B2 L3 R1", scr=True)
    sol = ''
    solvecrosspiece(facelets, pieces, 0)
    solvecrosspiece(facelets, pieces, 1)
    solvecrosspiece(facelets, pieces, 2)
    solvecrosspiece(facelets, pieces, 3)
    solvef2lpair(facelets, pieces, 0)
    solvef2lpair(facelets, pieces, 1)
    solvef2lpair(facelets, pieces, 2)
    solvef2lpair(facelets, pieces, 3)
    solveoll(facelets, pieces)
    solvepll(facelets, pieces)
    auf(facelets, pieces)
    if facelets != solvedfacelets:
        print('solving error')
    solmoves = list(sol[0::3])
    solnums = list(sol[1::3])
    for i, y in enumerate(solmoves[0:-1]):
        if y == solmoves[i+1]:
            solmoves[i]  = ' '
            solnums[i+1] = (int(solnums[i]) + int(solnums[i+1]))%4
            solnums[i] = ' '
        if solnums[i+1] == 0:
            solnums[i+1] = ' '
            solmoves[i+1] = ' '
    solnums = [i for i in solnums if i != ' ']
    solmoves = [i for i in solmoves if i != ' ']

    sol = ''
    for i in range(len(solmoves)):
        sol += solmoves[i]
        sol += str(solnums[i])
        sol += ' '
    print(f'{sol}\n')
    movecount = len(sol)/3
    totalmoves += movecount
    sol = ''

print(totalmoves/100)
'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'u':
                u(facelets, pieces)
            elif event.unicode == 'r':
                r(facelets, pieces)
            elif event.unicode == 'f':
                f(facelets, pieces)
            elif event.unicode == 'd':
                d(facelets, pieces)
            elif event.unicode == 'l':
                l(facelets, pieces)
            elif event.unicode == 'b':
                b(facelets, pieces)
            elif event.unicode == 'g':
                randomscramble = genrandscramble()
                move(facelets, pieces, randomscramble, scr=True)
                print('Scramble:', randomscramble)
            elif event.unicode == 'p':
                print(pieces)
            elif event.unicode == 's':
                sol = ''
                solvecrosspiece(facelets, pieces, 0)
                solvecrosspiece(facelets, pieces, 1)
                solvecrosspiece(facelets, pieces, 2)
                solvecrosspiece(facelets, pieces, 3)
                solvef2lpair(facelets, pieces, 1)
                solvef2lpair(facelets, pieces, 2)
                solvef2lpair(facelets, pieces, 3)
                solvef2lpair(facelets, pieces, 0)
                solveoll(facelets, pieces)
                solvepll(facelets, pieces)
                auf(facelets, pieces)
                solmoves = list(sol[0::3])
                solnums = list(sol[1::3])
                for i, y in enumerate(solmoves[0:-1]):
                    if y == solmoves[i+1]:
                        solmoves[i]  = ' '
                        solnums[i+1] = (int(solnums[i]) + int(solnums[i+1]))%4
                        solnums[i] = ' '
                    if solnums[i+1] == 0:
                        solnums[i+1] = ' '
                        solmoves[i+1] = ' '
                solnums = [i for i in solnums if i != ' ']
                solmoves = [i for i in solmoves if i != ' ']

                sol = ''
                for i in range(len(solmoves)):
                    sol += solmoves[i]
                    sol += str(solnums[i])
                    sol += ' '
                print(sol)
                movecount = len(sol)/3
                print(f'Movecount: {movecount}\n')
                sol = ''
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
 '''