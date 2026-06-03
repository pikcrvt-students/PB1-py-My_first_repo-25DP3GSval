t = [
    [-2, -1, 0, 5],
    [5, 2, 5, 7],
    [3, 1, 4, 6]
]

mazakais = t[0][0]
lielakais = t[0][0]

for i in range(3):
    for j in range(4):
        if t[i][j] < mazakais:
            mazakais = t[i][j]

        if t[i][j] > lielakais:
            lielakais = t[i][j]

starpiba = lielakais - mazakais

print('Mazākā temperatūra ir', mazakais)
print('Lielākā temperatūra ir', lielakais)
print('Starpība ir', starpiba)