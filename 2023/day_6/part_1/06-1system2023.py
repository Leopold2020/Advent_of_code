
def get_total(time, distance):
    total = []
    value = 0
    for _ in range(int(time)):
        value += 1
        if (value * (int(time)-value)) > int(distance):
            total.append(value)
    return len(total)

with open("2023/day_6/06-input2023.txt", "r", encoding="utf-8") as reader:
    lines = reader.readlines()
    lines = [s.replace("\n", "") for s in lines]
    total = []
    times = lines[0].split()
    distances = lines[1].split()
    for i in range(1, len(distances)):
        get_total(times[i], distances[i])
        total.append(get_total(times[i], distances[i]))
    final_value = 1
    for i in total:
        final_value *= i
    print(final_value)
    