list1 = ["⬜", "⬜", "⬜"]
list2 = ["⬜", "⬜", "⬜"]
list3 = ["⬜", "⬜", "⬜"]

map = [list1, list2, list3]

print("Bievenu sur lieu de ton trésor")
position = input("Ou veux-tu caché ton trésor aujourd'hui ? ")

letter = position[0]
abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"

print(f"{list1}\n{list2}\n{list3}")

target = int(input())
even_somme = 0
for number in range(2, target + 1, 2):
    even_somme += number
print(even_somme)

target = int(input())
for number in range(1, target + 1):
    print(number)


altermate_number = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        altermate_number += number
print(altermate_number)

