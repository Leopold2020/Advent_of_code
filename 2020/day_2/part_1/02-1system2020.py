# Oskar Svedlund
# TEINF-20
# 2022-11-23
# day 2 of 2020


value = 0
with open("2020/day_2/part_1/02-1input2020.txt", "r", encoding="utf-8") as reader:
    for line in reader.readlines():
        number, letter, word = line.split(" ")
        smallest, largest = number.split("-")
        letter = letter.replace(":","")

        check = word.count(letter)

        if check >= int(smallest) and check <= int(largest):
            value += 1

print(value)