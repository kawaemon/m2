import random

OUTPUT_FILE_NAME = "chart.csv"
CLASS_ROOM_WIDTH = 6

def groupn(array, n):
    current = 0
    while len(array) > current:
        yield array[current:current+n]
        current += n

members = []

with open("member.txt", "r") as f:
    for line in f.readlines():
        number, name = line.split()
        members.append(f"{number} {name}")

random.shuffle(members)

with open(OUTPUT_FILE_NAME, "w") as f:
    for line in groupn(members, CLASS_ROOM_WIDTH):
        print(",".join(line), file=f)

