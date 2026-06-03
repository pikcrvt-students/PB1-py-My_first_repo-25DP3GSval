t = [
    [-2, -1, 0, 5],
    [5, 2, 5, 7],
    [3, 1, 4, 6]
]

print('Rīgā 4. dienā bija', t[1][3], 'grādi')
print('Liepājā 1. dienā bija', t[2][0], 'grādi')
print()

for indekss in range(3):
    print('Otrajā dienā', indekss + 1, '. stacijā temperatūra bija', t[indekss][1])
print()

summa = 0
for j in range(4):
    summa = summa + t[2][j]

print(f'Vidējā temperatūra Liepājā ir {summa/4:0.3f} grādi.')
print()

for rinda in range(3):
    for kolonna in range(4):
        if t[rinda][kolonna] >= -2 and t[rinda][kolonna] <= 2:
            print('Stacija Nr.', rinda + 1, 'tāda temperatūra bija, kolonna', kolonna + 1, '. dienā.')
print()

for rinda in range(3):
    for kolonna in range(4):
        print(f'{t[rinda][kolonna]:3d}', end='')
    print()