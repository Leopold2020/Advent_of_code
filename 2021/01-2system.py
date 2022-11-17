# Oskar Svedlund
# TEINF-20
# 2022-11-16
# day 1 part 2 of 2021

previous_line = int()
incresed = -1
decresed = int()
x = 0

with open("2021/01-2input.txt", "r", encoding="utf-8") as f:
    count_list = []
    count_list.append(int(f.readline().strip("\n")))

    for line in f.readlines():
        count_list.append(int(line.strip("\n")))

test_list = count_list


previous_value = 0
for index in range(len(test_list)-2):
    value = test_list[index] + test_list[index+1] + test_list[index+2]

    if value > previous_value:
        incresed += 1

    if value < previous_value:
        decresed += 1

    previous_value = value


print(incresed, decresed)