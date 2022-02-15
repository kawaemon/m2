import random

inputCount = 0
answer = random.randint(1, 99)

while True:
    try:
        userInput = int(input("> "))
    except ValueError:
        print("正しい数字を入力してください")
        continue

    inputCount += 1
    if answer == userInput:
        print(f"正解です。{inputCount}回でクリアしました。")
        break

    if answer > userInput:
        print(f"{userInput}より大きいです")
    else:
        print(f"{userInput}より小さいです")

