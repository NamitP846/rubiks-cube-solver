sol = "F1 F1 U1 B1 U1 U1 B1 B1 U1 U1 F2 B3 R1 B1 U1 U1 U1 L3 B1 L1 F3 L1 F1 R3 U1 R1 U1 L1 F3 L2 U1 L1 U2 F1 U3 B1 U3 B3 U2 B1 U3 B3 L3 U1 L1 F3 L1 F1 L3 F1 R3 F3 R2 L3 B1 R1 B3 R3 B3 R3 L1 R3 U1 R3 U3 B3 R3 B2 U3 B3 U1 B3 R1 B1 R1 U1 U1 U1"
goalsol = 'F2 U1 B1 U2 B2 U2 F2 B3 R1 B1 U3 L3 B1 L1 F3 L1 F1 R3 U1 R1 U1 L1 R3 L2 U1 L1 F1 U3 B1 U3 B3 U2 B1 U3 B3 L3 U1 L1 F3 L1 F1 L3 F1 R1 F3 R2 L3 B1 R1 B3 R3 B3 R3 L1 R3 U1 R3 U3 B3 R3 B2 U3 B3 U1 B3 R1 B1 R1 U3'

solmoves = list(sol[0::3])
solnums = list(sol[1::3])
for i, y in enumerate(solmoves[0:-1]):
    if y == solmoves[i+1]:
        solmoves[i]  = ' '
        solnums[i+1] = int(solnums[i]) + int(solnums[i+1])
        solnums[i] = ' '
solnums = [i for i in solnums if i != ' ']
solmoves = [i for i in solmoves if i != ' ']

sol = ''
for i in range(len(solmoves)):
    sol += solmoves[i]
    sol += str(solnums[i])
    sol += ' '

if sol == goalsol:
    print('adslfkjhasdf')


print(sol)