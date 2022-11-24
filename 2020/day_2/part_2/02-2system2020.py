# Oskar Svedlund
# TEINF-20
# 2022-11-24
# day 2 part 2 of 2020


value = 0
with open("2020/day_2/part_2/02-2input2020.txt", "r", encoding="utf-8") as reader:
    for line in reader.readlines():
        number, letter, word = line.split(" ")
        smallest, largest = number.split("-")
        letter = letter.replace(":","")

        small_check = word[int(smallest)]

        try: large_check = word[int(largest)]
        except: large_check = False

        if small_check == letter or large_check == letter and small_check != large_check:
            value += 1


print(value)