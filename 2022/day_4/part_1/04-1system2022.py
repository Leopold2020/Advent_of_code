# Oskar Svedlund
# TEINF-20
# 2022-12-08
# day 4 of 2022

with open("2022/day_4/part_1/04-1input2022.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines
    lines = [s.replace("\n", "") for s in lines]


    for line in lines:

        part_1, part_2 = line.split(",")

