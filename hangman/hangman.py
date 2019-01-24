'''
Hangman
'''
import time
import os
import json
def menu():
    '''
    Hangman game in command line with python !!
    How to play
    1. Choose category to play
    2. Play it !!

    score calculator just your Life x 25
    have fun have fun
    '''
    #Setup variable
    directory_category = []
    category_list = []
    chosen_category = 0
    clear_screen = lambda: os.system('cls')
    #Setup menu
    for x in os.listdir('category'):
        directory_category.append("category/" + x)
        file = open("category/" + x).read()
        json_file = json.loads(file)
        print(json_file["name"])
        category_list.append(json_file["name"])
    #Choose category
    category_list_len = len(category_list)
    print("Select Category:")
    for i in range(category_list_len):
        print(str(i+1) + ".", category_list[i])

    #Take input and heck selection
    while chosen_category == 0 and (chosen_category <= category_list_len):
        try:
            chosen_category = int(input("Choose : "))
        except ValueError:
            print("Error!! Please enter number from 1 - " + str(category_list_len))
        if chosen_category > category_list_len:
            print("It not have this menu please try again")
            chosen_category = 0
    print("You choose", category_list[chosen_category-1])
    print("Have fun with hangman, please wait")
    time.sleep(1)
    clear_screen()
    play(directory_category[chosen_category-1])


def play(category):
    '''
    this is function to play this game 
    '''
    #Setup game
    life = 10
    score = 0
    file = open(category).read()
    json_file = json.loads(file)
    item = 1
    questions = json_file["questions"]

    #Start game
    for question in questions:
        print("Number", item)
        print("Hint: " '"' + questions[question] + '"')
        user_answer = []
        user_wrong = []

        #Setup word
        correct_answer = question
        for i in correct_answer:
            if i == " ":
                user_answer += " "
            else:
                user_answer += "_"
        for i in user_answer:
            print(i, end=" ")
        print("score %d, remaining wrong guess %d" % (score, life), end="")
        if len(user_wrong) != 0:
            print(", wrong guessed: ", end="")
            for wrong_character in user_wrong: print(wrong_character, end=" ")
        print("")

        #Play and Check answer
        while True:
            #Recieve user Input
            user_char = input("Enter your Character : ")
            while(len(user_char) != 1 or user_char == " "):
                print("Please enter only one Character or not have spacebar")
                user_char = input("Enter your Character : ")
            if user_char.lower() in correct_answer.lower():
                char_count = 0
                for char in correct_answer:
                    if(user_char.lower() == char.lower()):
                        #get score protect repeat
                        if(user_answer[char_count] == "_"):
                            score += (life*25)
                        user_answer[char_count] = correct_answer[char_count]
                    char_count += 1
            else:
                user_wrong.append(user_char)
                life -= 1
            for i in user_answer:
                print(i, end=" ")
            print("score %d, remaining wrong guess %d" % (score, life), end="")
            if len(user_wrong) != 0:
                print(", wrong guessed: ", end="")
                for wrong_character in user_wrong: print(wrong_character, end=" ")
            print("")

            #Check state
            if life <= 0:
                return print("Your lose with %d score" %(score))
            try:
                user_answer.index("_")
            except:
                item += 1
                break

    print("You win %d score in %s category. Thank you for play this I hope you will play another category." % (score, json_file["name"]))
menu()
