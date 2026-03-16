import time

animal = {"Lion":0, "Deer":0, "Wolf":0, "Mockingbird":0, "Dragon":0}

print("For this quiz,you will have options. " \
"Answer '1' for 'strongly disagree' and '5' for 'strongly agree.'")

time.sleep(2)
print()

while True:
    try:
        q1 = int(input("1) How impulsive are you?: "))
        if q1 < 1 or q1 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")

if q1 == 1:
    animal["Dragon"] += 5
elif q1 == 2:
    animal["Lion"] += 4
elif q1 == 3:
    animal["Wolf"] += 3
elif q1 == 4:
    animal["Deer"] += 2
elif q1 == 5:
    animal["Mockingbird"] += 1


print()

while True:
    try:
        q2 = int(input("2) Do you enjoy socializing and meeting new people?: "))
        if q2 < 1 or q2 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks  .")



if q2 == 1:
    animal["Dragon"] += 5
elif q2 == 2:
    animal["Lion"] += 4
elif q2 == 3:
    animal["Wolf"] += 3
elif q2 == 4:
    animal["Deer"] += 2
elif q2 == 5:
    animal["Mockingbird"] += 1


print()

while True:
    try:
        q3 = int(input("3) Do you like to take charge in a group?: "))
        if q3 < 1 or q3 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")

if q3 == 1:
    animal["Dragon"] += 5
elif q3 == 2:
    animal["Lion"] += 4
elif q3 == 3:
    animal["Wolf"] += 3
elif q3 == 4:
    animal["Deer"] += 2
elif q3 == 5:
    animal["Mockingbird"] += 1
else:
    print("Invalid input!")

print()
while True:
    try:
        q4 = int(input("4) Do you prefer working alone rather than in a team?: "))
        if q4 < 1 or q4 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")


if q4 == 1:
    animal["Dragon"] += 5
elif q4 == 2:
    animal["Lion"] += 4
elif q4 == 3:
    animal["Wolf"] += 3
elif q4 == 4:
    animal["Deer"] += 2
elif q4 == 5:
    animal["Mockingbird"] += 1

print()

while True:
    try:
        q5 = int(input("5) Are you curious and playful most of the time?: "))
        if q5 < 1 or q5 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")

if q5 == 1:
    animal["Dragon"] += 5
elif q5 == 2:
    animal["Lion"] += 4
elif q5 == 3:
    animal["Wolf"] += 3
elif q5 == 4:
    animal["Deer"] += 2
elif q5 == 5:
    animal["Mockingbird"] += 1

print()

while True:
    try:
        q6 = int(input("6) What do you want to be when you grow up?: \n"
        "1 = A CEO\n"
        "2 = A Model\n"
        "3 = A White collar criminal\n"
        "4 = A Scientist\n"
        "5 = An Artist\n"))
        if q6 < 1 or q6 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")


if q6 == 1:
    animal["Dragon"] += 5
elif q6 == 2:
    animal["Lion"] += 4
elif q6 == 3:
    animal["Wolf"] += 3
elif q6 == 4:
    animal["Deer"] += 2
elif q6 == 5:
    animal["Mockingbird"] += 1

print()

while True:
    try:
        q7 = int(input("7) Are you easily impressed?: "))

        if q7 < 1 or q7 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")



if q7 == 1:
    animal["Dragon"] += 5
elif q7 == 2:
    animal["Lion"] += 4
elif q7 == 3:
    animal["Wolf"] += 3
elif q7 == 4:
    animal["Deer"] += 2
elif q7 == 5:
    animal["Mockingbird"] += 1

print()

while True:
    try:
        q8 = int(input("8) If someone brings cake into a room, what do you do?: \n"
                       "1 = Jump on the cake and eat everything\n"
                       "2 = Request for the biggest slice or nothing\n"
                       "3 = Steal the cake when no one is looking\n"
                       "4 = Admire the patterns and structure of the cake\n"
                       "5 = Say 'No, calories!' and walk away\n"
                       " "))
        if q8 < 1 or q8 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")


if q8 == 1:
    animal["Dragon"] += 5
elif q8 == 2:
    animal["Lion"] += 4
elif q8 == 3:
    animal["Wolf"] += 3
elif q8 == 4:
    animal["Deer"] += 2
elif q8 == 5:
    animal["Mockingbird"] += 1
else:
    print("Invalid input!")

print()

while True:
    try:
        q9 = int(input("9) If you hear your jam in a club, what's your move?: \n"
                       "1 = Sit down and observe the dancers\n"
                       "2 = Start singing and dancing with your friends\n"
                          "3 = Start dancing with your friends but not singing\n"
                            "4 = Start singing with your friends but not dancing\n"
                              "5 = Start singing and/or dancing by yourself\n"
                              " ")) 
        if q9 < 1 or q9 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")


if q9 == 1:
    animal["Dragon"] += 5
elif q9 == 2:
    animal["Lion"] += 4
elif q9 == 3:
    animal["Wolf"] += 3
elif q9 == 4:
    animal["Deer"] += 2
elif q9 == 5:
    animal["Mockingbird"] += 1


print()

while True:
    try:
        q10 = int(input("10) If you could have a superpower for one day, what would it be? \n"
"1 = Flight (Like supergirl)\n"
"2 = Super strenght (Like Mr. Thunderman)\n"
"3 = Invisibility and stealth (Like Shadowcat)\n" 
"4 = Speak with nature (Like Snow White)\n"
"5 = Illusionist (Like DR. Strange)\n"
" "))
        if q10 < 1 or q10 > 5:
            print("Please enter a number between 1 and 5.")
            continue
        break
    except ValueError:
        print("Please enter a valid number. Thanks.")



if q10 == 1:
    animal["Dragon"] += 5
elif q10 == 2:
    animal["Lion"] += 4
elif q10 == 3:
    animal["Wolf"] += 3
elif q10 == 4:
    animal["Deer"] += 2
elif q10 == 5:
    animal["Mockingbird"] += 1

print("---------------------")
print("All done!")
time.sleep(2)
print("And now for your result!")

total_score = sum(animal.values())

if total_score > 40 and total_score <= 50:
    print("You are a dragon! Fearless, ambitious and ready to take charge of anything you set your mind to! " \
          "You dont follow rules. " \
          "You are a true dragon, and you will always be there for those you love.")
elif total_score > 30 and total_score <= 40:
    print("You are a lion" \
          "\nYou are a natural born leader, and you have a strong sense of self. " \
          "Many people look to you for guidance, and you dont dissappoint. " \
          "You are very loyal to your friends and family, and you will do anything to protect them. " \
          "You are a true lion, and you will always be there for those you love.")
elif total_score > 20 and total_score <= 30:
    print("You are a wolf" \
          "\nYou are a clever, independent and protective animal. " \
          "Things seem to disappear when you come around. " \
          "You think you are mysterious. " \
          "You are a true wolf, and you will always be there for those you love.")
elif total_score > 10 and total_score <= 20:
    print("You are a deer" \
          "\nYou are a gentle, kind and graceful animal. " \
          "You are very empathetic and love to help others. " \
          "You are easily impressed and love to be around beauty. " \
          "You are a true deer, and you will always be there for those you love.")
elif total_score == 10:
    print("You are a mockingbird" \
          "\nYou are a playful, curious and creative animal. " \
          "You are very social and love to be around others. " \
          "You bring joy, mischief and laughter wherever you go. " \
          "You are a true mockingbird, and you will always be there for those you love.")



