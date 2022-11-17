# Oskar Svedlund
# Teinf-20
# 2022-11-17
# day 2 of 2021

def forward_positions(value):
    value = value.strip("forward ")
    value = int(value)
    return value

def up(value):
    value = value.strip("up ")
    value = int(value)
    return value

def down(value):
    value = value.strip("down ")
    value = int(value)
    return value

def main(forward, depth):
    with open("2021/02input.txt", "r", encoding="utf-8") as reader:
        for line in reader.readlines():
            print(line)
            if "forward" in line:
                forward += forward_positions(line)

            elif "up" in line:
                depth -= up(line)


            elif "down" in line:
                depth += down(line)
    
    return forward, depth


if __name__ == "__main__":
    forward = 0
    depth = 0
    forward, depth = main(forward, depth)

    print(forward, depth)
    print(forward * depth)