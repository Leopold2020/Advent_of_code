# Oskar Svedlund
# TEINF-20
# 2022-11-24
# day 6 of 2021, Niclas solution


def import_puzzle(location):
    with open(location, "rt") as f:
        return [int(entry) for entry in f.readline().split(",")]


def part_one(fishes):
    fish_timers = list(fishes)
    days = 80

    for _ in range(days):
        new_fish = []
        for fish in enumerate(fish_timers):
            fish_timers[fish[0]] -= 1 
            if fish_timers[fish[0]] == -1:
                new_fish.append(8)
                fish_timers[fish[0]] = 6
        fish_timers.extend(new_fish)
    return len(fish_timers)

if __name__ == "__main__":
    fishes = import_puzzle("2021/day_6/part_1/06-1input2021.txt")
    print(part_one(fishes))