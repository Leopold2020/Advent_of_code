# Oskar Svedlund
# TEINF-20
# 2022-12-08
# day 3 part 2 of 2022

the_one = ""

import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27

with open("2022/day_3/part_2/03-2input2022.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    total_value = 0

    for line in range(0, len(lines)-2, 3):
        
        lines = [elem.replace("\n", "") for elem in lines]

        part1, part2, part3 = lines[line], lines[line + 1], lines[line + 2] 

        for letter in part1:
            if letter in part2:
                if letter in part3:
                    the_one = letter
                
        total_value += values[the_one]

    print(total_value)