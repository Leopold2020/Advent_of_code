# Oskar Svedlund
# TEINF-20
# 2022-11-16
# sonar 2.0

previous_line = int()
incresed = int()
decresed = int()
x = 0

with open("2021/01input.txt", "r", encoding="utf-8") as f:
    previous_line = int(f.readline())
    for line in f.readlines():
        line_2 = f.readlines()
        
        line = int(line)

        if line > previous_line:
            incresed += 1

        if line < previous_line:
            decresed += 1

        previous_line = line

print(incresed, decresed)