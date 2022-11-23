# Oskar Svedlund
# Teinf-20
# 2022-11-23
# day 1 of 2020

result = 0
with open("2020/01input.txt", "r", encoding="utf-8") as reader:
    for line1 in reader.readlines:
        for line2 in reader.readlines:

            if line1 + line2 == 2020:
                result = line1 * line2 

print(line1, line2)
print(result)