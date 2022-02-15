import random

class HnB:
    def __init__(self):
        self.answer = f"{random.randint(0, 9999):04}"
        self.input_count = 0

    def __isValidInput(self, input):
        return input.isalnum() and len(input) == 4

    # 同じ場所にある数字の数
    def __countHit(self, input):
        assert self.__isValidInput(input)

        result = 0
        for i in range(4):
            if self.answer[i] == input[i]:
                result += 1

        return result

    # 桁が違う
    def __countBlow(self, input):
        assert self.__isValidInput(input)

        answerTemp = [c for c in self.answer]

        result = 0
        for i in range(4):
            inputChar = input[i]
            if self.answer[i] != inputChar and inputChar in answerTemp:
                answerTemp.remove(inputChar)
                result += 1

        return result

    def judgeNumber(self, input):
        if not self.__isValidInput(input):
            raise ValueError("input string must have 4 ascii digits")

        self.input_count += 1
        if self.answer == input:
            print(f"{self.input_count}回で正解!")
            return True

        print(f"{self.__countHit(input)}ヒット {self.__countBlow(input)}ブロー")
        return False

game = HnB()
while True:
    userInput = input("> ")
    try:
        end = game.judgeNumber(userInput)
    except ValueError:
        print("正しく数字を入力してください")
        continue

    if end:
        break
