m = [
    [0, 0],
    [0, 0]
]

for i in range(2):
    for j in range(2):
        m[i][j] = int(input('Ievadi skaitli: '))

a = m[0][0]
b = m[0][1]
c = m[1][0]
d = m[1][1]

y = a * b - b * c

print('Matrica:')

for i in range(2):
    for j in range(2):
        print(m[i][j], end=' ')
    print()

print('y =', y)