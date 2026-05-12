radiuss = int(input("Ievadi Rādiusu:"))

while radiuss < 0:
    radiuss = int(input("Ievadi pozitīvu rādiusu:"))

risinajums = 2 * 3.1415 * radiuss

print("Risinājums:", risinajums)