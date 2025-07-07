import numpy as np
import pygame

pygame.display.init()
bgsize = (1000, 250)
bg = pygame.display.set_mode(bgsize, 0)
bg.fill('black')

faces = np.array([
    green:=[
    ['g', 'g', 'g'],
    ['g', 'g', 'g'],
    ['g', 'g', 'g']
],blue:=[
    ['b', 'b', 'b'],
    ['b', 'b', 'b'],
    ['b', 'b', 'b']
],white:=[
    ['w', 'w', 'w'],
    ['w', 'w', 'w'],
    ['w', 'w', 'w']
],yellow:=[
    ['y', 'y', 'y'],
    ['y', 'y', 'y'],
    ['y', 'y', 'y']
],orange:=[
    ['o', 'o', 'o'],
    ['o', 'o', 'o'],
    ['o', 'o', 'o']
],red:=[
    ['r', 'r', 'r'],
    ['r', 'r', 'r'],
    ['r', 'r', 'r']
]
])

def forward(x):
    x.insert(0, x[len(x)-1])
    x.__delitem__(len(x)-1)

def u():
    global faces
    global yellow
    yellow = np.rot90(yellow)
    layer = []
    affected = [green, red, blue, orange]
    for face in affected:
        z = []
        z.extend(face[0])
        if face[1][1] == 'g' or face[1][1] == 'b':
            z.reverse()
        layer.extend(z)
    for x in range(3):
        forward(layer)
    for face in affected:
        face[0] = layer[0:3]
        for x in range(3):
            layer.__delitem__(0)
    faces = np.array([green, blue, white, yellow, orange, red])

def r():
    global faces
    global orange
    orange = np.rot90(orange, -1)
    layer = []
    affected = [green, yellow, blue, white]
    for face in affected:
        z = []
        for x in range(len(face)):
            z.extend(face[x][2])
        if face[1][1] == 'g' or face[1][1] == 'b':
            z.reverse()
        layer.extend(z)
    for x in range(3):
        forward(layer)
    for face in affected:
        for x in range(3):
            face[x][2] = layer[0]
            layer.__delitem__(0)
    faces = np.array([green, blue, white, yellow, orange, red])

def f():
    global faces
    global green
    green = np.rot90(green, -1)
    layer = []
    affected = [white, red, yellow, orange]
    for face in affected:
        z = []
        if face[1][1] == 'w' or face[1][1] == 'y':
                z.extend(face[0])
                rev = False
        else:
            for x in range(3):
                z.extend(face[x][0])
                rev = True
        if rev:
            z.reverse()
        layer.extend(z)
    for x in range(3):
        forward(layer)
    for face in affected:
        if face[1][1] == 'w' or face[1][1] == 'y':
            face[0] = layer[0:3]
            for x in range(3):
                layer.__delitem__(0)
        else:
            for x in range(3):
                face[x][0] = layer[0]
                layer.__delitem__(0)
    faces = np.array([green, blue, white, yellow, orange, red])

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
    for x in range(3):
        disp[1][x].reverse()
        disp[3][x].reverse()
        disp[5][x].reverse()
    for x,face in enumerate(disp):
        for y,row in enumerate(face):
            for z,piece in enumerate(row):
                if disp[x][y][z] == 'r':
                    disp[x][y][z] = 'red'
                if disp[x][y][z] == 'o':
                    disp[x][y][z] = 'orange'
                if disp[x][y][z] == 'b':
                    disp[x][y][z] = 'blue'
                if disp[x][y][z] == 'g':
                    disp[x][y][z] = 'green'
                if disp[x][y][z] == 'y':
                    disp[x][y][z] = 'yellow'
                if disp[x][y][z] == 'w':
                    disp[x][y][z] = 'white'

    for x in range(6):
        for y in range(3):
            for z,piece in enumerate(disp[x][y]):
                pygame.draw.rect(bg, piece, (25+x*150 + z*40, 25+y*40, 35,35), width=0)

    pygame.display.update()