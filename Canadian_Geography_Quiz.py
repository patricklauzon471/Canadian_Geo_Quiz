
score = 0

#Introduction, introduce the game
print("Welcome to the Canadian Geography Quiz!")
print("-----------------------------------------")
print("You will recieve ten questions about Canadian Geography, see how many you can get!")

game_started = input("Type in Y if you would like to proceed: ")

#Allow the player to start the game

if game_started != "Y":
    print("Game has been terminated\n")
    quit()

print("Right, answer!, let's get started!\n\n")

#Cycle through questions, increasing score if the answer is correct

print("Question 1.")
print("-----------------------------------------")
answer1 = input("What is Canada's largest province by population\n 1. Manitoba, 2. British Columbia, 3. Quebec, 4. Ontario: ")
if answer1 == '4':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 2.")
print("-----------------------------------------")
answer2 = input("How many territories does Canada have\n 1. 4, 2. 2, 3. 3, 4. 5: ")
if answer2 == '3':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 3.")
print("-----------------------------------------")
answer3 = input("Which province is the Calgary Stampede located in\n 1. Alberta, 2. British Columbia, 3. Manitoba, 4. Nova Scotia: ")
if answer3 == '1':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")    

print("Question 4.")
print("-----------------------------------------")
answer4 = input("What Canadian city has the largest arabic population per capita\n 1. Edmonton, 2. Windsor, 3. Toronto, 4. Brampton: ")
if answer4 == '2':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 5.")
print("-----------------------------------------")
answer5 = input("What is Canada's only French speaking province\n 1. Manitoba, 2. British Columbia, 3. Quebec, 4. Ontario: ")
if answer5 == '3':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 6.")
print("-----------------------------------------")
answer6 = input("How many ocean's does Canada border\n 1. 2, 2. 4, 3. 3, 4. 1: ")
if answer6 == '3':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 7.")
print("-----------------------------------------")
answer7 = input("Which year did Canada officially become a country?\n 1. 1912, 2. 1863, 3. 1757, 4. 1921: ")
if answer7 == '2':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 8.")
print("-----------------------------------------")
answer8 = input("What is Canada's smallest province by size and population\n 1. Manitoba, 2. New Brunswick, 3. Nova Scotia, 4. Prince Edward Island: ")
if answer8 == '4':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 9.")
print("-----------------------------------------")
answer9 = input("What percent of Canadians live within 100 miles of the US border\n 1. 70%, 2. 60%, 3. 85%, 4. 95%: ")
if answer9 == '3':
    print("correct\n")
    score += 1
else:
    print("Sorry, that's incorrect\n")

print("Question 10.")
print("-----------------------------------------")
answer10 = input("What is Canada's warmest city by mean yearly temperature\n 1. Windsor, 2. Victoria, 3. Kamloops, 4. London: ")
if answer10 == '2':
    print("correct\n\n")
    score += 1
else:
    print("Sorry, that's incorrect\n\n")

#Display the final score using proper formatting

print("-----------------------------------------")
print(f"Your score is {score}/10")