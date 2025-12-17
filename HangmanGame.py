import random

def login():
    global name
    name=input(" Enter your name to Login Hangman Game : ")
    print("\n You are successfully logged in 🤩")

def play_game():

    Secret_Words=["Thor","Loki","Hulk","Ironman"]
    Random_word=random.choice(Secret_Words).lower()

    Guess=list(Random_word)
    Find_Word=[]

    s="go"
    start=input("\n Hey " + name +
                "\n Enter 'GO' to game the game : ").strip().lower()

    if start == s:

        print("\n Secret Word is :", end=" ")
        for i in range(len(Random_word)):
            print("_", end=" ")

        i=10
        while i > 0:
            print("\n Chances left : ", i)

            word=input(" Guess THE WORD : ").lower()

            if word in Random_word and word not in Find_Word:
                Find_Word.append(word)

                print(" Secret Word :", end=" ")
                for ch in Random_word:
                    if ch in Find_Word:
                        print(ch, end=" ")
                    else:
                        print("_", end=" ")

                if set(Find_Word) >= set(Guess):
                    print("\n You Win ")
                    break

            elif word not in Random_word:
                print(f" {word} is not in Secret Word")

            i-=1

        if i==0:
            print("\n You Lose ")
            print(" The word was:", Random_word)

login()
play_game()