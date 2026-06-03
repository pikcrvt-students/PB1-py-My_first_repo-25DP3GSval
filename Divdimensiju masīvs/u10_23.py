from random import randint

M = []

for i in range(10):
    rinda = []
    for j in range(10):
        rinda.append(0)
    M.append(rinda)

skaits = 0

while skaits < 10:
    x = randint(0, 9)
    y = randint(0, 9)

    if M[x][y] == 0:
        M[x][y] = 1
        skaits = skaits + 1

skaits = 0

while skaits < 10:
    x = randint(0, 9)
    y = randint(0, 9)

    if M[x][y] == 0:
        M[x][y] = 2
        skaits = skaits + 1

print('Spēles laukums:')

for i in range(10):
    for j in range(10):
        print(M[i][j], end=' ')
    print()

print()

x = int(input('Ievadi x: '))
y = int(input('Ievadi y: '))

if M[x][y] == 0:
    print('Šajā lauciņā nav vērtības')

if M[x][y] == 1:
    print('Šajā lauciņā ir krustiņš')

if M[x][y] == 2:
    print('Šajā lauciņā ir nullīte')

krustini = 0
nullites = 0

for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):

        if i >= 0 and i < 10 and j >= 0 and j < 10:

            if i != x or j != y:

                if M[i][j] == 1:
                    krustini = krustini + 1

                if M[i][j] == 2:
                    nullites = nullites + 1

print('Blakus ir', krustini, 'krustiņi')
print('Blakus ir', nullites, 'nullītes')