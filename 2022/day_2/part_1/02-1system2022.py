# Oskar Svedlund
# TEINF-20
# 2022-12-07
# Day 2 of 2022

total_score = 0

ROCK = ["A", "X", 1]
PAPER = ["B", "Y", 2]
SCISSORS = ["C", "Z", 3]

def value(input1:str, input2:str):
    points = 0
    match input2:
        case "X": points += 1

        case "Y": points += 2
        
        case "Z": points += 3

    match input1, input2:
        case ("A", "Y") | ("B", "Z") | ("C", "X"):
            points += 6

        case ("A", "X") | ("B", "Y") | ("C", "Z"):
            points += 3

    return int(points)

with open("2022/day_2/part_1/02-1input2022.txt") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]

    for line in lines:
        reciving, response = line.split(" ")        
        total_score += value(reciving, response)

    
    print(total_score)