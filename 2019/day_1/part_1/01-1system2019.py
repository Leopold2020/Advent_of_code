# Oskar Svedlund
# TEINF-20
# 2022-11-23
# day 1 of 2019

fuel = 0
with open("2019/day_1/part_1/01-1input2019.txt", "r", encoding="utf-8") as reader:
    for line in reader.readlines():
        new_line = (int(line) // 3) - 2
        fuel += new_line

print(fuel)