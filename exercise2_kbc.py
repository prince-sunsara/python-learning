""" 
KAUN BANEGA KARODPATI
"""

questions = [
    [
        "What does HTML stand for?","Hyper Transfer Markup Language","Hyperlink and Text Markup Language",
        "Hyper Text Markup Language","High-Level Text Markup Language",3
    ],
    [
        "Which of the following CSS properties is used to change the text color of an element?",
        "background-color","font-color","color","text-color",3
    ],
    [
        "What is the purpose of JavaScript in web development?","To style web pages","To create database tables",
        "To add interactivity and functionality to web pages","To define the structure of a webpage",3
    ],
    [
        "Which of the following is NOT a commonly used front-end JavaScript framework or library?",
        "React","Angular","Django","Vue.js",3
    ],
    [
        "What does API stand for in the context of web development?",
        "Application Programming Interface","Advanced Programming Interface","Advanced Programming Interface","Advanced Protocol Integration",1
    ],
    [
        "Which of the following HTTP status codes indicates a successful request in web development?",
        "200 OK","404 Not Found","500 Internal Server Error","302 Found",1
    ],
    [
        "What is the primary purpose of a CSS media query?",
        "To define the structure of an HTML document","To apply different styles based on the device's characteristics, such as screen size","To create interactive animations","To store data on the client-side",2
    ],
    [
        "In web development, which language is used to query and manipulate data in relational databases?",
        "Java","Python","SQL (Structured Query Language)","Ruby",3
    ],
    [
        "What does CSS stand for in web development?",
        "Cascading Style Sheet","Cascading Style Sheet","Colorful Style Sheet","Creative Style Sheet",1
    ],
    [
        "Which of the following is a commonly used version control system for tracking changes in web development projects?",
        "Java","Sublime Text","Git","jQuery",3
    ],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
fixMoney = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"{i+1}. {question[0]} [for Rs.{levels[i]}]")
    print(f" 1.{question[1]}\n 2.{question[2]}\n 3.{question[3]}\n 4.{question[4]}")
    ans = int(input("\nEnter your ans (1-4): "))
    
    if(ans == question[-1]):
        print("\ncorrect answer")
        money = levels[i]
        if i < len(questions)-2:
            print(f"Your current money is {money}Rs.\n\n\n")
        else:
            print(f"Congratulations you won this session.\nYou won total {money}Rs.\n\n\n")
        if i == 3:
            fixMoney = 5000
        elif i == 6:
            fixMoney = 40000
    else:
        if i <= 3:
            print(f"Sorry wrong answer, You loss.")
        elif i > 3:
            print(f"Sorry wrong answer, You got {fixMoney}Rs.")
        elif i > 6:
            print(f"Sorry wrong answer, You got {fixMoney}Rs.")
            
        break 