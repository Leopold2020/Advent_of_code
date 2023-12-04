# Oskar Svedlund
# TE4
# 2023-12-04
# day 2 part 2 of 2023 advent of code

with open("2023/day_2/02-input2023.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]
    total = 0
    for i in lines:
        game_id, game = i.split(": ")
        minimum_red = 0
        minimum_green = 0
        minimum_blue = 0
        for round in game.split("; "):
            for instance in round.split(", "):
                number, color = instance.split(" ")
                match color:
                    case "red":
                        if int(number) > minimum_red:
                            minimum_red = int(number)
                    case "green":
                        if int(number) > minimum_green:
                            minimum_green = int(number)
                    case "blue":
                        if int(number) > minimum_blue:
                            minimum_blue = int(number)
        total += minimum_red*minimum_green*minimum_blue
    print(total)