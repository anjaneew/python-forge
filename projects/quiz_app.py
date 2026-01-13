#Quiz App

questions = ("Q1. Who are the planets in navagraha?", 
             "Q2. Who is the lord of Karma?",
             "Q1. Who is the teacher of gods?")

options = (("A. seven", "B. nine", "C. ten"), 
           ("A. saturn", "B. jupiter", "C. kethu"), 
           ("A. saturn", "B. jupiter", "C. kethu"))
answers = ("B", "A", "B")
guesses = []
score = 0
question_num = 0

# display questions

for question in questions:
    print()
    print(question)
    print()
    for option in options[question_num]:
        print(option, end=" ")    
    print()
    guess = input("Enter answer: (A, B, C): ").upper()
    print("________________________________________") 
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")    
    question_num += 1

print()
print("________________________________________") 
score = int(score/len(questions)) * 100
print(f"Your score is {score:.2f}%") 
print("________________________________________") 

    