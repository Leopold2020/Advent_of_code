# Oskar Svedlund
# TEINF-20
# 2022-12-07
# Day 2 part 2 of 2022

total_score = 0

ROCK = ["A", 1]
PAPER = ["B", 2]
SCISSORS = ["C", 3]

def value(input1:str, input2:str):
    points = 0
    result = ""
    used = ""

    match input2:
        case "X":
            points += 0
            result = "lose"

        case "Y":
            points += 3
            result = "draw"

        case "Z":
            points += 6
            result = "win"

    match result:
        case "win":
            match input1:
                case "A": used = "paper"

                case "B": used = "scissor"

                case "C": used = "rock"
        
        case "draw":
            match input1:
                case "A": used = "rock"

                case "B": used = "paper"

                case "C": used = "scissor"

        case "lose":
            match input1:
                case "A": used = "scissor"

                case "B": used = "rock"

                case "C": used = "paper"

    match used:
        case "rock": points += 1

        case "paper": points += 2
        
        case "scissor": points += 3


    return int(points)

with open("2022/day_2/part_2/02-2input2022.txt") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]

    for line in lines:
        reciving, response = line.split(" ")
        total_score += value(reciving, response)

    
    print(total_score)