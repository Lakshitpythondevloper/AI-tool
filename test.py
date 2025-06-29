import os
import webbrowser

#This function collects names and marks of students, calculates total marks, and displays the results.

def name_of_students():

    print("Welcome to student totalling marks generator")
    print("\n")
    names_of_student = []
    number_of_student = 4

    while number_of_student >= 0:
        input_students = input("Enter the name of student: ")
        names_of_student.append(input_students)
        number_of_student -= 1

    marks_of_student1 = int(input("Enter the marks of student 1: "))
    marks_of_student2 = int(input("Enter the marks of student 2: "))
    marks_of_student3 = int(input("Enter the marks of student 3: "))
    marks_of_student4 = int(input("Enter the marks of student 4: "))
    marks_of_student5 = int(input("Enter the marks of student 5: "))

    print("The marks of" + "" + names_of_student[0] + " is " + str(marks_of_student1))
    print("The marks of" + "" + names_of_student[1] + " is " + str(marks_of_student2))
    print("The marks of" + "" + names_of_student[2] + " is " + str(marks_of_student3))
    print("The marks of" + "" + names_of_student[3] + " is " + str(marks_of_student4))
    print("The marks of" + "" + names_of_student[4] + " is " + str(marks_of_student5))

    total_marks = marks_of_student1 + marks_of_student2 + marks_of_student3 + marks_of_student4 + marks_of_student5
    print("The total marks of all students is: ", total_marks)


# This function creates a table genrator with for loop
def table_genrator():
        print("Welcome to multiplication table genrator")
        print(r'''   
    ___________ ____   ____                                                    
    \__    ___/____ \_ |__ |  |   ____      ____   ____   ________________ _/  |_  ___________ 
      |    |  \__  \ | __ \|  | _/ __ \    / ___\_/ __ \ /    \_  __ \__  \\   __\/  _ \_  __ \
      |    |   / __ \| \_\ \  |_\  ___/   / /_/  >  ___/|   |  \  | \// __ \|  | (  <_> )  | \/
      |____|  (____  /___  /____/\___  >  \___  / \___  >___|  /__|  (____  /__|  \____/|__|   
                   \/    \/          \/  /_____/      \/     \/           \/                   ''')

        name_input1 = input("Hey! welcome to this content please enter your name first to continue: ")

        table_input = int(input(f"Hi {name_input1}! Which number of table you want to create example(2,3,4 etc...): "))

        for table in range(1, 11):
            output = table_input * table
            print(output)
print("Here is your multiplication table")

def quiz_genrator():
        print(r'''
    .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. |
    | |    ___       | || | _____  _____ | || |     _____    | || |   ________   | |
    | |  .'   '.     | || ||_   _||_   _|| || |    |_   _|   | || |  |  __   _|  | |
    | | /  .-.  \    | || |  | |    | |  | || |      | |     | || |  |_/  / /    | |
    | | | |   | |    | || |  | '    ' |  | || |      | |     | || |     .'.' _   | |
    | | \  `-'  \_   | || |   \ `--' /   | || |     _| |_    | || |   _/ /__/ |  | |
    | |  `.___.\__|  | || |    `.__.'    | || |    |_____|   | || |  |________|  | |
    | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------' ''')

        print("Welcome to quiz!")
        quiz = ["Which insect does formic acid is exist?", "What is the currency of Japan?",
                "Which is the biggest flower in the world?", "How many types of cloud services give me only number.",
                "What is the full-form of 'LLM' in AI"
                ]

        input_name = input("Please enter your name to continue quiz: ").capitalize()
        question1 = input(f"Hey {input_name} Give me the answer of this question {quiz[0]}: ").capitalize()
        question2 = input(f"Okay {input_name} Now Give me the answer of 2 question {quiz[1]}: ").capitalize()
        question3 = input(f"Now Give me the answer of 3 question {quiz[2]}: ").capitalize()
        question4 = int(input(f"Give me the answer of 4 question {quiz[3]}: "))
        question5 = input(f"Last question {input_name} Give me the answer of 5 question {quiz[4]}: ").capitalize()

        score = 0

        if question1 == "Ant":
            print("Question 1 is correct")
            score += 1
        if question2 == "Yen":
            print("Question 2 is correct")
            score += 1
        if question3 == "Rafflesia":
            print("Question 3 is correct")
            score += 1
        if question4 == 3:
            print("Question 4 is correct")
            score += 1
        if question5 == "Large language model":
            print(f"Wow {input_name} question 5 is also correct✨😀 Your score is {score}")
            score += 1
        else:
            print("question is incorrect sorry ☹️")

        if score == 5:
            webbrowser.open(
                "https://firebase.google.com/?gad_source=1&gad_campaignid=20100026058&gbraid=0AAAAADpUDOgZ7v3WRZ7crs18IyHqpKJp3&gclid=Cj0KCQjwpf7CBhCfARIsANIETVoJ9kn8hjYhxKtrADfyJC6TohrDz2u12QiRkkiXNijOwrD7TN8Z5d8aApgtEALw_wcB&gclsrc=aw.ds")

def file_deleter():
        print("Welcome to file deleter from desktop.It can only delete 5 files.")

        input_1 = input("Enter a file name which you want delete")
        input_2 = input("Enter a file 2 name which you want delete")
        input_3 = input("Enter a file 3 name which you want delete")
        input_4 = input("Enter a file 4 name which you want delete")
        input_5 = input("Enter a file 5 name which you want delete")

        os.rmdir(
            r"C:\Users\Enter-your-username\Desktop/" + input_1)  # replace this "Enter-your-username" into your actual username in your computer
        os.rmdir(
            r"C:\Users\Enter-your-username\Desktop/" + input_2)  # replace this "Enter-your-username" into your actual username in your computer
        os.rmdir(
            r"C:\Users\Enter-your-username\Desktop/" + input_3)  # replace this "Enter-your-username" into your actual username in your computer
        os.rmdir(
            r"C:\Users\Enter-your-username\Desktop/" + input_4)  # replace this "Enter-your-username" into your actual username in your computer
        os.rmdir(
            r"C:\Users\Enter-your-username\Desktop/" + input_5)  # replace this "Enter-your-username" into your actual username in your computer

        # You can freely edit this code and the path in file deleter. 😀

def game():
        print(''' 
        *******************************************************************************
                  |                   |                  |                     |
         _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                  |                `"=._o`"=._      _`"=._                     |
         _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                  |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
         _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/________
        *******************************************************************************''')

        print("Welcome to treasure island.\nYour mission is to find the treasure.")

        first_input = input("Where you want to go? Left or Right: ").capitalize()

        if first_input == "Left":
            seconed_input = input(
                "Now you come to the lake. There is island between the lake what do you want?\n wait for boat or swim into lake type swim or wait: ").capitalize()

            if seconed_input == "Wait":
                third_output = input(
                    "You are arrived at island. There is a house with three doors\n One is yellow, one is red and one blue. Which color do you choose? type yellow or red or blue: ").capitalize()
            else:
                print("Attacked by trout. Game Over!🙁")

            if third_output == "Yellow":
                print("You Win!😎✨ The game is finished you got treasure congratulations.")
            elif third_output == "Red":
                print("Burned by fire.Game is over!🔥")
            else:
                print("Eaten by snake. Game is over!🐍")
        else:
            print("You are fall into a hole. Game is over!☹️")

def who_pay_the_bill():

        total_bill = float(input("Enter total bill: "))
        tip = int(input("Enter your tip you want to give: "))
        peopel_split_there_money = int(input("Enter people numbers which they give money by splitting: "))

        bill = tip / 100
        finaL_bill = bill * total_bill
        tbill = total_bill + finaL_bill
        total_people = tbill / peopel_split_there_money

        print(round(total_people, 2))
        print(f"people split their bill into {total_people} money₹")

print("Welcome to AI tool. This is a simple AI tool which can do some tasks for you.")
print(r'''                                
   ,---,                  ,---, 
  '  .' \              ,`--.' | 
 /  ;    '.            |   :  : 
:  :       \           :   |  ' 
:  |   /\   \          |   :  | 
|  :  ' ;.   :         '   '  ; 
|  |  ;/  \   \        |   |  | 
'  :  | \  \ ,'        '   :  ; 
|  |  '  '--'          |   |  ' 
|  :  :                '   :  | 
|  | ,'                ;   |.'  
`--''                  '---'                         
                                ''')
name_input = input("Please enter your name to continue this AI: ")
content_1 = input(f"Which content you want to choose {name_input} 1.totalling the student marks 2.quiz 3.game 4.who pay the bill in restaurant\n"
                  "and delete five files form desktop press 'T' for 1st option or press 'Q' for second option or press 'G' for third option\n"
                  "or press 'W' for fourth option and press 'Del' for fifth option: ").capitalize()

#Conditions: -

if content_1 == "T":
    name_of_students()
elif content_1 == "Q":
    quiz_genrator()
elif content_1 == "G":
    game()
elif content_1 == "W":
    who_pay_the_bill()
elif content_1 == "Del":
    file_deleter()
else:
    print("You have entered wrong input please try again later. Thank you for using this AI tool.😊")
