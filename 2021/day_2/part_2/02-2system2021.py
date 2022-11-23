# Oskar Svedlund
# Teinf-20
# 2022-11-17
# day 2 of 2021

def forward_positions(current_forward, aim, value):
    current_depth = 0
    value = value.strip("forward ")
    value = int(value)
    current_forward += value
    current_depth += aim * value
    return current_forward, current_depth


def up(value):
    value = value.strip("up ")
    value = int(value)
    return value

def down(value):
    value = value.strip("down ")
    value = int(value)
    return value

def main(forward, depth, aim):
    with open("2021/day_2/part_2/02-2input2021.txt", "r", encoding="utf-8") as reader:
        for line in reader.readlines():
            if "forward" in line:
                forward, new_depth = forward_positions(forward, aim, line)
                depth += new_depth

            elif "up" in line:
                aim -= up(line)


            elif "down" in line:
                aim += down(line)
    
    return forward, depth, aim


if __name__ == "__main__":
    forward = 0
    depth = 0
    aim = 0
    forward, depth, aim = main(forward, depth, aim)

    print(forward, depth)
    print(forward * depth)