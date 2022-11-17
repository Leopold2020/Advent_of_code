# Oskar Svedlund
# TEINF-20
# 2022-11-16
# day 1 of 2021

previous_line = int()
incresed = int()
decresed = int()

with open("2021/01input.txt", "r", encoding="utf-8") as f:
    previous_line = int(f.readline())
    for line in f.readlines():
        
        line = int(line)

        if line > previous_line:
            incresed += 1

        if line < previous_line:
            decresed += 1

        previous_line = line

print(incresed, decresed)