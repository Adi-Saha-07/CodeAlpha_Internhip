Question1="hello"
Question2="how are you" 
Question3="i am also fine"
Question4="what are you doing"

greeting1="good morning"
greeting2="good evening"
greeting3="okay good night"
    
reply1=" AI : Hey ! what's up"
reply2=" AI : I'm Fine . How are you 😃 ?"
reply3=" AI : Wow great"
reply4=" AI : I'm talking to you 🫠"

greetingreply1=" AI : Good Morning"
greetingreply2=" AI : Good Evening" 
greetingreply3=" AI : Good Night"

stop="bye"


def login():
    global name
    name=input(" For login 'Friday AI' enter your name : ")
    
    print(" \n You are successfully logged in 🤩"
          " \n To exit , type 'Bye' or say 'Good Night' to end the chat\n")

def Question(name):
 
 while True:

    user=input(" You : ").strip().lower()

    if user==Question1: print(reply1 + " " + name + " 😛 ? ")

    elif user==Question2: print(reply2)

    elif user==Question3: print(reply3 + " " + name + " 🌚")
    
    elif user==Question4: print(reply4)

    elif user==greeting1: print(greetingreply1 + " " + name + " 🌄")

    elif user==greeting2: print(greetingreply2 + " " + name + " 🌆")

    elif user==greeting3:
        print(greetingreply3 + " " + name + " 😴🌃")
        break

    elif user==stop:
        print(" AI : Bye Bye 🥹")
        break

    else: print(" AI : Sorry, I couldn't understand that. I'm still learning, please try again. 😞")


login()
Question(name)