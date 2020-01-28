#!/usr/bin/python3
#Lane Doyle
#1/27/20

import pickle 
import sys 

'''Program to create a game library'''

#Dictionary
games = {}
data_file = open("game_lib.pickle", "rb")
games = pickle.load(data_file)
data_file.close()

#Functions
def add_and_edit():
    print("Running add_and_edit()")

def print_all():
    #print("Running print_all()")
    games_key_list = games.keys()
    
    for key in games_key_list:
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single player/multi/either: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beat it?: ", games[key][9])
        print("Purchase Date: ", games[key][10])
        print("Notes: ", games[key][11])
        print("-----------")    
    
def search_by_title():
    print("Running search_by_title()")
    
def remove_title():
    print("Running remove_title()")
    
def save_library():
    #print("Running save_library()")
    data_file = open("game_lib.pickle", "wb")
    pickle.dump(games, data_file)
    data_file.close()    
    print("File saved!")
    
def quit():
    #print("Running quit()")
    print("Goodbye!")
    sys.exit()   

#Main Menu    
while True:
    print('''
    ------------------------
    Welcome to your library!
    ------------------------
    
    Main Menu:
    1) Add/Edit Game
    2) Print All Games
    3) Search By Title
    4) Remove a Game
    5) Save Library
    Q) Quit 
    ''')
    
    choice = input("What would you like to do? ")
    
    if choice == "1":
        add_and_edit()
    elif choice == "2":
        print_all()
    elif choice == "3":
        search_by_title()
    elif choice == "4":
        remove_title()
    elif choice == "5":
        save_library()
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("That is not a valid option!")    