import random

# JUMBODICT = {
#     "Math": ["Math Quiz #1 (Easy)": {"x + 2 = 5": ["3", "2", "4", "5"]} ]
# }

mathquiz1y11 = {
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

mathquiztitles = [
    "Math Quiz #1 (Easy)",
    "Math Quiz #2 (Easy)",
    "Math Quiz #3 (Easy)",
    "Math Quiz #4 (Easy)",
    "Math Quiz #5 (Easy)",
    "Math Quiz #6 (Easy)"
]


subjects = [
    "Math",
    "Not currently supported:",
    "Digital Technology", 
    "Biology, Chemistry", 
    "Physics, Statistics", 
    "Physical Education", 
    "Health",
    "Economics!"
]


score = 0

print("Welcome to Quiz Central!")
name = input("Please enter you name: ")

while True:
    yearlvl = input(f"Thanks {name}, please enter your year level: ")
    if yearlvl.isdigit():
        if yearlvl == "11":
            print("Welcome to the Y11 Quiz Central!")
            print(f"Here is a list of all the Year 11 subjects:")
            for avalaiblesubjectsy11, subjectnamey11 in enumerate(subjects, start = 1):
                print(f"{avalaiblesubjectsy11}) {subjectnamey11}")
            while True:
                studysubject = input("What subject would you like to study?: ")
                if studysubject == "Math" or "1":
                    print("Welcome to the Quiz Centrals Math hub!")
                    print("Here is a list of all the avaiable Year 11 Math quizzes:")
                    for avalaiblemathy11quiz, quiznamemathy11 in enumerate(mathquiztitles, start = 1):
                        print(f"{avalaiblemathy11quiz}) {quiznamemathy11}")
                    while True:
                        mathquizuserchoice = input("Please select the quiz you would like to take? ")
                        if mathquizuserchoice == "1":
                            for question, answer in mathquiz1y11.items():
                                correct_answer = answer[0]
                                random.shuffle(answer)
                                
                                print(f"Question: {question}")
                                for answernum, option in enumerate(answer, start=1):
                                    print(f"{answernum}) {option}")
                                answer_label = int(input("Your answer: "))                                   
                                user_input = (answer[answer_label - 1])
                        
                                if user_input == correct_answer:
                                    print("Correct")
                                    score += 1
                                else:
                                    print(f"Incorrect! The answer was {correct_answer} not {user_input}!")

                            print(f"Your final score is: {score}/{len(mathquiz1y11)}") 

                        else: 
                            print("Please select a proper Math Quiz!")
                else: 
                    print("Please choose an available subject!")  
                    studysubject = input("What subject would you like to study?: ")
            
                    
            
        else:
            print(f"Sorry but Quiz Central is not currently supported for Y{yearlvl}, please make a request to our offices in Mumbai for support in your year level!")
    
    else:
        yearlvl = print("Please enter an integer in between 0-13!: ")
        
