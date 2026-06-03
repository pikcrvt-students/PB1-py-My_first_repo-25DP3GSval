komp = [[0.0 for kolonna in range(3)] for rinda in range(4)]
vid = [0.0] * 4

grupa = [""] * 3

grupa[0] = "1"
grupa[1] = "2"
grupa[2] = "3"

for kurss in range(1, 5):
    print()
    print('Vērtējumi', kurss, '. kursa', 'kursiem')
    for j in range(3):
        print(kurss, '. kursa grupa DP', kurss, grupa[j], 'vidējā atzīme:', sep='', end='')
        komp[kurss-1][j] = float(input())

for kurss in range(1, 5):
    sum = 0
    for j in range(3):
        sum = sum + komp[kurss-1][j]
    vid[kurss-1] = sum / 3

print()
print('Kursa grupu vidējā atzīme')
for kurss in range(1, 5):
    print(f'{kurss:3} {vid[kurss-1]:7.2f}')

print()