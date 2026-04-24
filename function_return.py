def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

skaitis1 = int(input("Ievadi pirmo skaitli: "))
skaitis2 = int(input("Ievadi otro skaitli: "))

lielākais = maximum(skaitis1, skaitis2)

print(lielākais)