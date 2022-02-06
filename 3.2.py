import random

OUTPUT_FILE_NAME = "chart_for_teacher.csv"
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
    for line in list(groupn(members, CLASS_ROOM_WIDTH))[::-1]:
        if len(line) != CLASS_ROOM_WIDTH:
            line = ["" for _ in range(CLASS_ROOM_WIDTH - len(line))] + line

        print(",".join(line), file=f)

