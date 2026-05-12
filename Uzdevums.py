from math import pi

radiuss = int(input("Ievadi Rādiusu:"))

while radiuss < 0:
    radiuss = int(input("Ievadi pozitīvu rādiusu:"))

risinajums = 2 * pi * radiuss

print("Risinājums:", risinajums)