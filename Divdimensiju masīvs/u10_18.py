a = [
    ['0', '0', '0'],
    ['0', '0', '0'],
    ['0', '0', '0']
]

for m in range(2):
    print('Pirmais spēlētāj, ievadi', m + 1, '. kuģa koordinātas')
    x = int(input('Ievadi rindu no 0 līdz 2: '))
    y = int(input('Ievadi kolonnu no 0 līdz 2: '))

    a[x][y] = 'k'

for i in range(50):
    print()

trap = 0

for m in range(2):
    print('Otrais spēlētāj, ievadi', m + 1, '. šāviena koordinātas')
    x = int(input('Ievadi rindu no 0 līdz 2: '))
    y = int(input('Ievadi kolonnu no 0 līdz 2: '))

    if a[x][y] == 'k':
        trap = trap + 1
        a[x][y] = 'x'
    else:
        a[x][y] = 'm'

print('Kara lauks:')

for i in range(3):
    for j in range(3):
        print(a[i][j], end=' ')
    print()

print('Iznīcināti', trap, 'kuģi')