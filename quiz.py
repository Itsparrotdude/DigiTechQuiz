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

subjects = "Math. Not currently supported: Digital Technology, Biology, Chemistry, Physics, Statistics, Physical Education, Health and Economics!"


score = 0

print("Welcome to Quiz Central!")
name = input("Please enter you name: ")
yearlvl = input(f"Thanks {name}, please enter your year level: ")

while yearlvl.isdigit():
    if yearlvl == "11":
        print("Welcome to the Y11 Quiz Central!")
        print(f"Here is a list of all the Year 11 subjects: {subjects}" )
        studysubject = input("What subject would you like to study?: ")
        while studysubject != "Math":
            print("Please choose an available subject!")  
            studysubject = input("What subject would you like to study?: ")
        else: 
            for question, answer in quiz.items():
                correct_answer = answer[0]
                random.shuffle(answer)
                print(question)
                for answernum, option in enumerate(answer, start=1):
                    print(f"{answernum}) {option}")
                answer_label = int(input("Your answer: "))
                user_input = (answer[answer_label - 1])
                if user_input == correct_answer:
                    print("Correct")
                    score += 1
                else:
                    print(f"Incorrect! The answer was {correct_answer} not {user_input}!")

            print(f"Your final score is: {score}/{len(quiz)}") 
           
    else:
        print("Sorry but Quiz Central is not currently supported in your region, please make a request to our offices in Mumbai for support in your year level!")
else:
    print("Please enter an integer in between 0-13!")