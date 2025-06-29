# 🌟 AI-tool 🤖

Welcome to **AI-tool**! This repository is a showcase of cutting-edge AI solutions crafted in pure Python. Whether you are a beginner or a seasoned developer, you'll find well-documented code examples, creative explanations, and a visually engaging experience here.



## ✨ Features

- 🌈 **Beautifully Explained Python Code**  
- 🧠 **AI/ML Algorithms**  
- 📚 **Line-by-Line Explanations**  
- 🤝 **Open to Contributors**  
- 💡 **Creative Backgrounds and Emojis**  

---

## 🚀 Why Use This Project?

- **Interactive Learning:** Run the script and interact with various mini-apps, from quizzes to games!  
- **Sharpen Your Skills:** Each function demonstrates Python basics, logic, and user input/output.  
- **All-in-One Utility:** Useful for students, beginners, or anyone who wants a playful AI-driven script.  
- **Open for Extension:** You can easily add your own features or mini-projects!

---

## 🧠 About `Simple AI.py`

This file is a fun, interactive, all-in-one Python script that offers a variety of simple AI-powered tasks and utility mini-apps. It’s perfect for learning Python basics, logic, and user interaction!

### 📝 What can it do?

- 🎓 Calculate and display total marks for a group of students
- ➗ Generate multiplication tables
- ❓ Run a multiple-choice quiz
- 🏝️ Play a text-based adventure game
- 💸 Split bills among friends (with tips)
- 🗑️ Delete folders from your Desktop (⚠️ Use with caution!)

---

## 📜 How does it work? (Line-by-Line Explanation)

### 1. Imports

```python
import os
import webbrowser
```
- `os` is for interacting with your computer’s files and folders.
- `webbrowser` lets Python open links in your web browser.

---

### 2. Student Totalling Marks Generator

```python
def name_of_students():
    print("Welcome to student totalling marks generator")
    ...
    names_of_student = []
    number_of_student = 4
    while number_of_student >= 0:
        input_students = input("Enter the name of student: ")
        names_of_student.append(input_students)
        number_of_student -= 1
    marks_of_student1 = int(input("Enter the marks of student 1: "))
    ...
    print("The marks of" + "" + names_of_student[0] + " is " + str(marks_of_student1))
    ...
    total_marks = marks_of_student1 + ... + marks_of_student5
    print("The total marks of all students is: ", total_marks)
```
**Explanation:**  
- Greets the user.
- Collects 5 student names in a list.
- Asks for each student’s marks.
- Prints each student’s marks.
- Adds all marks and displays the total.

---

### 3. Multiplication Table Generator

```python
def table_genrator():
    print("Welcome to multiplication table genrator")
    print(r''' <ASCII art> ''')
    name_input1 = input("Hey! ... enter your name ...")
    table_input = int(input(f"Hi {name_input1}! ...Which number..."))
    for table in range(1, 11):
        output = table_input * table
        print(output)
    print("Here is your multiplication table")
```
**Explanation:**  
- Welcomes and asks your name.
- Asks which number’s table to generate.
- Prints multiplication table from 1 to 10.

---

### 4. Quiz Generator

```python
def quiz_genrator():
    print(r''' <ASCII art> ''')
    print("Welcome to quiz!")
    quiz = ["Which insect ...", ...]
    input_name = input("Please enter your name ...").capitalize()
    question1 = input(f"Hey {input_name} ... {quiz[0]}: ").capitalize()
    ...
    score = 0
    if question1 == "Ant": ...
    ...
    if score == 5:
        webbrowser.open("<reward link>")
```
**Explanation:**  
- Welcomes user, displays quiz banner.
- Asks 5 quiz questions.
- Checks each answer, increases score if correct.
- If you score 5/5, opens a congratulatory web page!

---

### 5. File Deleter (⚠️ Use with care!)

```python
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
```
**Explanation:**  
- Asks for up to 5 folder names to delete from Desktop.
- **Deletes** each folder using `os.rmdir`.
- **Caution:** You must replace `"Enter-your-username"` with your real Windows username.

---

### 6. Text Adventure Game

```python
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
```
**Explanation:**  
- A simple text-based game where your choices decide if you find the treasure or face game-over scenarios.

---

### 7. Bill Splitter

```python
def who_pay_the_bill():
    total_bill = float(input("Enter total bill: "))
    tip = int(input("Enter your tip ..."))
    peopel_split_there_money = int(input("Enter people numbers ..."))
    bill = tip / 100
    finaL_bill = bill * total_bill
    tbill = total_bill + finaL_bill
    total_people = tbill / peopel_split_there_money
    print(round(total_people, 2))
    print(f"people split their bill into {total_people} money₹")
```
**Explanation:**  
- Asks for the bill, tip %, and number of friends.
- Calculates tip and splits the total evenly.

---

### 8. Main Menu and User Choice

```python
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
```
**Explanation:**  
- Welcomes user, asks for their name.
- Prompts user to choose a feature by pressing a key.
- Calls the corresponding function, or prints an error if input is invalid.

---

## ASCII arts 🖌️: - 

```python
       ___________ ____   ____                                                    
    \__    ___/____ \_ |__ |  |   ____      ____   ____   ________________ _/  |_  ___________ 
      |    |  \__  \ | __ \|  | _/ __ \    / ___\_/ __ \ /    \_  __ \__  \\   __\/  _ \_  __ \
      |    |   / __ \| \_\ \  |_\  ___/   / /_/  >  ___/|   |  \  | \// __ \|  | (  <_> )  | \/
      |____|  (____  /___  /____/\___  >  \___  / \___  >___|  /__|  (____  /__|  \____/|__|   
                   \/    \/          \/  /_____/      \/     \/           \/          
```
```python
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
     '----------------'  '----------------'  '----------------'  '----------------'
```
```python
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
        *******************************************************************************'
```
```python
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
```

## 🌟 Fun Fact!

Did you know?  
The "AI-tool" project is designed to be a playground for both learning and teaching Python, encouraging hands-on interaction and creativity. You can use it as a foundation to build your own mini-projects and even challenge your friends with new features!

---

## 🌌 Beautiful Background

> <div align="center" style="background: linear-gradient(90deg, #8ecae6 0%, #219ebc 50%, #023047 100%); color: white; border-radius: 16px; padding: 20px;">
> <h2>🚀 Unlock the Power of AI with Python! 🚀</h2>
> <p>Explore, learn, and contribute to the future of artificial intelligence.</p>
> </div>

---

## 🤗 Contribution Guide

1. Fork this repository 🍴
2. Create your feature branch (`git checkout -b feature/my-feature`) 🌱
3. Commit your changes (`git commit -am 'Add awesome feature'`) ✏️
4. Push to the branch (`git push origin feature/my-feature`) 🚀
5. Open a Pull Request 📬

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <h3>Made with ❤️ by <a href="https://github.com/Lakshitpythondevloper">Lakshitpythondevloper</a></h3>
</div>
