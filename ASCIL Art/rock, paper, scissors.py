import random
import time
import os

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

arts = {
    "akmens": rock,
    "papīrs": paper,
    "šķēres": scissors
}

choices = list(arts.keys())

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown():
    for word in ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""", """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""",
""" """]:
        clear()
        print("\n" * 3)
        print(word.center(40))
        time.sleep(0.4)

def get_winner(player, computer):
    if player == computer:
        return "Neizšķirts!"
    wins = {
        ("akmens", "šķēres"),
        ("šķēres", "papīrs"),
        ("papīrs", "akmens")
    }
    return "Tu uzvarēji!" if (player, computer) in wins else "Dators uzvarēja!"

while True:
    clear()
    print("=== AKMENS ŠĶĒRES PAPĪRĪTS ===\n")
    print("Izvēlies: akmens / papīrs / šķēres")
    player = input("> ").lower()

    if player not in choices:
        print("Nepareiza Izvēle!")
        time.sleep(1.5)
        continue

    computer = random.choice(choices)

    countdown()
    clear()

    print("TU IZVĒLĒJIES:\n")
    print(arts[player])
    print("\nDATORS IZVĒLĒJĀS: \n")
    print(arts[computer])

    print("\n" + get_winner(player, computer))

    again = input("\nSpēlēt vēlreiz? (j/n): ").lower()
    if again != 'j':
        break

clear()
print("Paldies par spēli!")