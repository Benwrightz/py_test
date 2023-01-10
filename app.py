print("Hello!!! Welcome to my game")
name = input("what's your name? ")
print("HI " + name)
answer1 = input("do you want to play? ")
if answer1.lower() != "yes":
    quit()

print("let's play")
score = 0
answer2 = input("what is your shoe size? ")
answer3 = input("what's your favorite color? ")
Question = input("where's Sweden located? ")
if Question.lower() == "europe":
    print("correct")
    score += 1
else:
    print("incorrect")
Question = input("where's Thailand located? ")
if Question.lower() == "asia":
    print("correct")
    score += 1
else:
    print("incorrect")
Question = input("where's Angola located? ")
if Question.lower() == "africa":
    print("correct")
    score += 1 
else:
    print("incorrect")
Question = input("where's chelsea located? ")
if Question.lower() == "london":
    print("correct")
    score += 1
else:
    print("incorrect")
Question = input("who's liverpool's manager? ")
if Question.lower() == "Jurgen Klopp":
    print("correct")
    score += 1
else:
    print("incorrect")
print("You got " + str(score) + " questions correctly!!")





