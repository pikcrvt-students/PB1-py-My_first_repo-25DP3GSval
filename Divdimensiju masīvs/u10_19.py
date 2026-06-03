a = []

for i in range(10):
    rinda = []
    for j in range(10):
        rinda.append('0')
    a.append(rinda)

for m in range(2):
    print('Pirmais spēlētāj, ievadi', m + 1, '. kuģa koordinātas')
    x = int(input('Ievadi rindu: '))
    y = int(input('Ievadi kolonnu: '))

    a[x][y] = 'k'

for i in range(50):
    print()

trap = 0

for m in range(2):
    print('Otrais spēlētāj, ievadi', m + 1, '. šāviena koordinātas')
    x = int(input('Ievadi rindu: '))
    y = int(input('Ievadi kolonnu: '))

    if a[x][y] == 'k':
        trap = trap + 1
        a[x][y] = 'x'
    else:
        a[x][y] = 'm'

print('Kara lauks:')

for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()

print('Iznīcināti', trap, 'kuģi')