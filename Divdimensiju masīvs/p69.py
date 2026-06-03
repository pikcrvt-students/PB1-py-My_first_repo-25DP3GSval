n1 = int(input('Ievadi rindu skaitu: '))
m1 = int(input('Ievadi kolonnu skaitu: '))

x = [[0.0 for j in range(m1)] for x in range(n1)]

for i in range(n1):
    for j in range(m1):
        x[i][j] = float(input('x[' + str(i) + '][' + str(j) + ']= '))

# izvade
print('Ievadītais masīvs')
for i in range(n1):
    for j in range(m1):
        print(f'{x[i][j]:9.2f}', end='')
    print()

print()
L = int(input('Ievadi kolonnas indeksu no 0 līdz ' + str(m1 - 1) + ', ieskaitot '))

if L >= 0 and L < m1:
    min = x[0][L]
    for i in range(1, n1):
        if x[i][L] < min:
            min = x[i][L]
    print(f'Kolonnas minimālā vērtība: {min:0.2f}')
else:
    print('Kolonnas ar tādu indeksu nav!')