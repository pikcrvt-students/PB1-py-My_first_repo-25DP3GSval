a = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        a[i][j] = int(input('Ievadi skaitli: '))

summa = 0

print('Tabula:')

for i in range(3):
    for j in range(3):
        print(a[i][j], end=' ')
        summa = summa + a[i][j]
    print()

print('Summa ir', summa)