print("Worlds Hardest Quiz")

question = 0    # Tells me which questions the user has done
questions = ["120 - 63 =: ",
             "Where was Osama Bin Laden born?: ",
             "Who is Martin Kalanda-phiri?: "]

userAnswers = ["","",""] # Stores the answers for points

answers = ["a. 47\nb. 57\nc. Blue\nd. America\n",
           "a. The Middle East\nb. America \nc. Tehran Suadi Arabia\nd. Riyadh, Saudi Arabia",
           "a. MARTin\nb. MarTIN\nc. Martin\nd. mARTin"]

correct = 0

while question < 3:
   print(questions[question])
   print(answers[question])
   answers[question] = input("To answer, pick a letter or leave it blank to skip it: ").lower()

   if question == 0:
       if answers[question] == "a":
           print()
           print("Sorry, You appear to be mentally challenged")
           question = question + 1
           print()
       elif answers[question] == "b":
           print()
           print("Good Job! That is correct. You can do subtraction.")
           correct = correct + 1
           question = question + 1
           print()
       elif answers[question] == "c":
           print()
           print("Sorry, You appear to be mentally challenged")
           question = question + 1
           print()
       elif answers[question] == "d":
           print()
           print("Sorry, You appear to be mentally challenged")
           question = question + 1
           print()
       elif answers[question] == "":
           print("Awww...you skipped one!")
           question = question + 1
           print()    
       else:
           print("Invalid character, please try again.")    

   elif question == 1:
       if answers[question] == "a":
           print()
           print("Sorry, You are not a real T-man")
           question = question + 1
           print()
       elif answers[question] == "b":
           print()
           print("Sorry, You are not a real T-man")
           question = question + 1
           print()
       elif answers[question] == "c":
           print()
           print("Sorry, You are not a real T-man")
           question = question + 1
           print()
       elif answers[question] == "d":
           print()
           print("Terrorist! You got it right!")
           correct = correct + 1
           question = question + 1
           print()
       elif answers[question] == "":
           print("Awww...you skipped one!")
           question = question + 1
           print()    
       else:
           print("Invalid character, please try again.")

   elif question == 2:
       if answers[question] == "a":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "b":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()        
       elif answers[question] == "c":
           print()
           print("Amazing! You're awesome!")
           correct = correct + 1
           question = question + 1
           print()
       elif answers[question] == "d":
           print()
           print("Sorry, please try again.")
           question = question + 1
           print()
       elif answers[question] == "":
           print("Awww...you skipped one!")
           question = question + 1
           print()
           print("Thanks for playing!")
           
again = input("Would you like to play again? if so please type y otherwise; later loser: ")
if again == 'y': 
       question = 0




                  
