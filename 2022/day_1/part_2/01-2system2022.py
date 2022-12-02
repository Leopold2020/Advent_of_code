# Oskar Svedlund
# TEINF-20
# 2022-12-02
# day 1 part 2 of 2022

elves = []
values = []
present_value = 0

with open("2022/day_1/part_2/01-2input2022.txt", "r", encoding="utf-8") as reader:
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

values.sort()

top_total = int(values[-1]) + int(values[-2]) + int(values[-3])


print("largest three numbers combined is ", top_total)