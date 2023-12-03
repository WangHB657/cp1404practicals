import random

MIN_NUM = 1
MAX_NUM = 45
NUMS_PER_LINE = 6
numbers = []

NUM_QUICK_PICKS = int(input("How many quick picks? "))

for i in range(NUM_QUICK_PICKS):
    for j in range(NUMS_PER_LINE):
        number = random.randint(MIN_NUM, MAX_NUM)
        numbers.append(number)
        numbers.sort()
    print(" ".join(f"{num:2}" for num in numbers))
    numbers.clear()

