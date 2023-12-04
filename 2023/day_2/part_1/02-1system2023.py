# Oskar Svedlund
# TE4
# 2023-12-04
# day 2 part 1 of 2023 advent of code


with open("2023/day_2/02-input2023.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    total = 0
    for i in lines:
        game_id, game = i.split(": ")
        cheater = False
        for round in game.split("; "):
            for instance in round.split(", "):
                number, color = instance.split(" ")
                if color == "red" and int(number) > MAX_RED:
                    cheater = True
                elif color == "green" and int(number) > MAX_GREEN:
                    cheater = True
                elif color == "blue" and int(number) > MAX_BLUE:
                    cheater = True
        if cheater == False:
            total += int(game_id.split(" ")[1])
    print(total)