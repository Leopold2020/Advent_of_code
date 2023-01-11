# Oskar Svedlund
# TEINF-20
# 2022-12-08
# day 4 of 2022

amount = 0

with open("2022/day_4/part_1/04-1input2022.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]

    line = lines
    for line in lines:

        part_1, part_2 = line.split(",")

        smaller_part1, bigger_part1 = part_1.split("-")
        smaller_part2, bigger_part2 = part_2.split("-")

        if (smaller_part1 <= smaller_part2 and bigger_part1 >= bigger_part2): #or (smaller_part1 >= smaller_part2 and bigger_part1 <= bigger_part2):
            amount += 1

    
    print(amount)
