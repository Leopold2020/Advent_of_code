# Oskar Svedlund
# TE4
# 2023-12-04
# day 1 part 2 of 2023 advent of code

def get_number(line:str):
    spelt_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = []
    for pos, data in enumerate(line):
            if data.isnumeric():
                numbers.append(int(data))
            else:
                for number, i in enumerate(spelt_numbers):
                    if line[pos:len(i)+pos:] == i:
                        numbers.append(number)
    return numbers

with open("2023/day_1/01-input2023.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]
    total = 0
    for line in lines:
        numbers = get_number(line)
        double_digit = str(numbers[0]) + str(numbers[-1])
        total += int(double_digit)
    print(total)