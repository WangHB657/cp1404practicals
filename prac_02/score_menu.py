"""
function calculate_score_result(score)
    if score < 0 or score > 100
        return "Invalid score"
    else if score > 90
        return "Excellent"
    else if score > 50
        return "Passable"
    else
        return "Bad"


function print_score_result(score)
    result = calculate_score_result(score)
    print score, result


function show_stars(score)
    print "*" * score


function get_valid_score()
    get score
    if 0 <= score <= 100
        return score
    else
        print "Invalid score. Please enter a score between 0 and 100."


function main()
    print(MENU)
    score = get_valid_score()
    choice = ""
    while choice != "Q"
        get choice
        if choice == "G"
            score = get_valid_score()
        else if choice == "P"
            print_score_result(score)
        else if choice == "S"
            show_stars(score)
    print "Farewell!"


main()
"""

MENU = """Menu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def calculate_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def print_score_result(score):
    result = calculate_score_result(score)
    print(f"The result for the score {score} is: {result}")


def show_stars(score):
    print("*" * int(score))


def get_valid_score():
    score = float(input("Enter a score (0-100): "))
    if 0 <= score <= 100:
        return score
    else:
        print("Invalid score. Please enter a score between 0 and 100.")


def main():
    print(MENU)
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        choice = input("Enter your choice: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_score_result(score)
        elif choice == "S":
            show_stars(score)
    print("Farewell!")


main()
