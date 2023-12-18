"""
CP1404/CP5632 - Practical
function calculate_score_result(score)
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

function main()
    get user_score
    result = calculate_score_result(user_score)
    print result

    random_score = random.uniform(0, 100)
    print random_score
    random_result = calculate_score_result(random_score)
    print random_result
"""

import random


def calculate_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter score: "))
    result = calculate_score_result(user_score)
    print(result)

    # Generating a random score
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    random_result = calculate_score_result(random_score)
    print(random_result)
