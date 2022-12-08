# Oskar Svedlund
# TEINF-20
# 2022-12-08
# day 3 of 2022

the_one = ""

import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27

with open("2022/day_3/part_1/03-1input2022.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    total_value = 0

    for line in lines:
        part1, part2 = line[:len(line)//2], line[len(line)//2:]

        for letter1 in part1:
            if letter1 in part2:
                the_one = letter1
                
        total_value += values[the_one]

    print(total_value)
