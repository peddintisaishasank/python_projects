print("Welcome to my computer quiz!")

playing = input("Do you want to play? say yes or no?")
score=0

if playing.lower()!=("yes"):
    quit()
print("Okay! Let's play :)")

answer=input("What does CPU stand for?")
if answer.lower()=="central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer=input("What does PSU stand for?")
if answer.lower()=="power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got"+ str(score)+" questions correct!")
print("You got"+ str((score/4)*100)+ "%.")