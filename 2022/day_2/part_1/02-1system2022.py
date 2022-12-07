# Oskar Svedlund
# TEINF-20
# 2022-12-07
# Day 2 of 2022

total_score = 0
round_choice = 1

ROCK = ["A", "Z", 1]
PAPER = ["B", "X", 2]
SCISSORS = ["C", "Y", 3]

def cheeking_case(input): #The idea is that the input is checked and the function returns what you should play to win, to get draw and lose.
    match input:
        case "A": return "X", "Z", "Y"

        case "B": return  "Y", "X", "Z"

        case "C": return "Z", "Y", "X"


with open("2022/day_2/part_1/02-1input2022.txt") as reader:
    lines = reader.readlines()

    for line in lines:
        reciving, response = line.split(" ")

        match round_choice:

            case 1:
                used, _, __ = cheeking_case(reciving)

            case 2:
                pass

            case 3:
                pass
        
        if round_choice == 3: round_choice = 1

        else: round_choice += 1


