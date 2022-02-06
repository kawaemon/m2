import random

OUTPUT_FILE_NAME = "chart.csv"
CLASS_ROOM_WIDTH = 6

class Member:
    def __init__(self, line):
        self.number, self.name = line.split()
        self.front = self.name.endswith("*")
        if self.front:
            self.name = self.name[:len(self.name)-1] # trim '*'

    def as_str(self):
        return f"{self.number} {self.name}"

def groupn(array, n):
    current = 0
    while len(array) > current:
        yield array[current:current+n]
        current += n

front_members = []
members = []

with open("member.txt", "r") as f:
    for line in f.readlines():
        member = Member(line)
        if member.front:
            front_members.append(member.as_str())
        else:
            members.append(member.as_str())

front_members += list(map(lambda d: None, range(CLASS_ROOM_WIDTH * 2 - len(front_members))))

random.shuffle(front_members)
random.shuffle(members)

with open(OUTPUT_FILE_NAME, "w") as f:
    for line in groupn(front_members, CLASS_ROOM_WIDTH):
        printed = []
        for member in line:
            if member == None:
                if len(members) == 0: break
                member = members.pop()
            printed.append(member)

        print(",".join(printed), file=f)

    for line in groupn(members, CLASS_ROOM_WIDTH):
        print(",".join(line), file=f)
