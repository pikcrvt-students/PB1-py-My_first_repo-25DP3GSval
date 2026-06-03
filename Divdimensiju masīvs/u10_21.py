km = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(4):
    print('Ievadi', i + 1, '. šofera kilometrus')

    for j in range(5):
        km[i][j] = int(input(str(j + 1) + '. diena: '))

print()

for i in range(4):
    summa = 0

    for j in range(5):
        summa = summa + km[i][j]

    videji = summa / 5

    print(i + 1, '. šoferis kopā nobrauca', summa, 'km')
    print(i + 1, '. šoferis vidēji dienā nobrauca', videji, 'km')
    print()