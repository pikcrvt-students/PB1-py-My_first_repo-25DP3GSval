from random import randrange

n = int(input('Ievadi rindu skaitu: '))
m = int(input('Ievadi kolonnu skaitu: '))

divdimensiju_masivs_A = [[0 for kolonnas in range(m)] for rindas in range(n)]

for i in range(n):
    for j in range(m):
        divdimensiju_masivs_A[i][j] = randrange(100)

print('Masīva izvade tabulas veidā:')

for i in range(n):
    for j in range(m):
        print(f'{divdimensiju_masivs_A[i][j]:4d}', end='')
    print()