import random

quiz = {
    "x + 2 = 5": [ "3", "2", "4", "5"],
    "5x = 10": [ "2", "15", "50", "0.5" ],
    "3x + 3 = 21": [ "6", "8", "15", "4"],
    "2x - 7 = 11": ["9", "7", "4", "6"],
    "4 + 3x = 19": ["5", "4", "7", "6"],
    "6x - 9 = 33": ["7", "8", "6", "9"],
    "9x = 54": ["6", "7", "9", "8"],
    "5x + 2 = 37": ["7", "6", "8", "9"],
    "10 - 2x = 4": ["3", "2", "5", "1"],
    "2x + 8 = 18": ["5", "6", "7", "4"],
}

for question, answer in quiz.items():
    correct_answer = answer[0]

