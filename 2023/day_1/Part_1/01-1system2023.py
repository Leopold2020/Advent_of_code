# Oskar Svedlund
# TE4
# 2023-12-04
# day 1 part 1 of 2023 advent of code


with open("2023/day_1/01-input2023.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]
    total = 0
    for line in lines:
        numbers = []
        for data in line:
            if data.isnumeric():
                numbers.append(data)
        total += int(numbers[0] + numbers[-1])
    print(total)