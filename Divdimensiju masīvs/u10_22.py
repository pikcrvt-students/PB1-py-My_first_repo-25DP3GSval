nauda = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(4):
    print('Ievadi', i + 1, '. veikala ieņēmumus')

    for j in range(5):
        nauda[i][j] = float(input(str(j + 1) + '. diena: '))

print()

for i in range(4):
    summa = 0

    for j in range(5):
        summa = summa + nauda[i][j]

    videji = summa / 5

    print(i + 1, '. veikala vidējā peļņa vienā dienā ir', videji)