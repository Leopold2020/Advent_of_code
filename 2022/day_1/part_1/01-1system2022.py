# Oskar Svedlund
# TEINF-20
# 2022-12-01
# Day 1 of 2022

elves = []
values = []
present_value = 0

with open("2022/day_1/part_1/01-1input2022.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()

    lines = [elem.replace("\n", "") for elem in lines]
    lines.append("")

    for line in lines:

        try: line = int(line)
        except: line = str(line)

        if line != "":
            present_value += line

        else: 
            values.append(present_value)
            present_value = 0

    print("largest number is ", max(values))