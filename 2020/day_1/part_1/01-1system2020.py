# Oskar Svedlund
# Teinf-20
# 2022-11-23
# day 1 of 2020

result = 0
with open("2020/day_1/part_1/01-1input2020.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    for line1 in lines:
        line1 = int(line1)
        for line2 in lines:
            line2 = int(line2)

            if line1 + line2 == 2020:
                chosen_line1 = line1
                chosen_line2 = line2
                result = line1 * line2 
                print(result)

print(chosen_line1, chosen_line2)
print(result)