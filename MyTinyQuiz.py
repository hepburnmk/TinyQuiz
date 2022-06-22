print("Welcome to my MegaQuiz")

playing = input("Do you want to play my Quiz? ").lower()
if playing != "yes":
    quit()

print("\nThat's great! Let's get going and play the game")

tally = 0

answer = input("\nWhat colour is a lemon? ").lower()

if answer == "yellow":
    print("Well Done, you sure know your fruits")
    tally += 1

else:
    print("That's not correct, you need to brush up on your fruit knowledge")

answer1 = input("\nWhat is the capital of Ireland? ").lower()

if answer1 == "dublin":
    print("Way to go friend! You are a geography expert")
    tally += 1

else:
    print("Good try but you didn't get it right, maybe you need to invest in an atlas ")

answer2 = input("\nWhich year was the United Nations formed ")

if answer2 == "1945":
    print("Oh, look at you history buff!")
    tally += 1

else:
    print("oopsie, you didn't get it this time, maybe next time slugger! ")

answer3 = input('\nWhat company was initially know as "Blue Ribbon Sports"? ').lower()

if answer3 == "nike":
    print("Woohoo, Just Do It - good job")
    tally += 1

else:
    print("You didn't get it this time, I believe in you though ")

print("I hope you had fun! You got", tally, "questions correct today")
print("I hope you had fun! You got", ((tally/4) *100), "%")
