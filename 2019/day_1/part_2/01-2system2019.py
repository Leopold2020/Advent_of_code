# Oskar Svedlund
# TEINF-20
# 2022-11-23
# day 1 part 2 of 2019

fuel = 0

with open("2019/day_1/part_2/01-2input2019.txt", "r", encoding="utf-8") as reader:
    for line in reader.readlines():
        new_line = int(line)
        new_line = (new_line // 3) - 2
        fuel += new_line

        required_fuel = new_line
        while required_fuel != 0:
            required_fuel = required_fuel // 3 - 2
            if required_fuel < 0:
                required_fuel = 0
            else:
                fuel += required_fuel


print(fuel)