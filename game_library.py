#!/usr/bin/python3
#Lane Doyle
#1/27/20

import pickle 
import sys 

'''Program to create a game library'''

#Dictionary
games = {1: ['FPS', 'Halo 3', 'Bungee', 'Microsoft', 'Xbox 360', '2007',
             '10', 'either', '30.00', 'Yes', '1/15/2008', 'This game blows chunks!'],
         2: ['Sandbox', 'Minecraft', 'Mojang', 'Mojang', 'Xbox One', '2011',
             '10', 'either', '40.00', 'N/A', '3/15/2017', ''],
         3: ['Action Role-Playing', 'Fallout 4', 'Bethesda Game Studios', 'Bethesda Softworks', 
             'Xbox One', '2015', '7', 'Single', '70.00', 'Yes', '12/25/2015', 'Best game ever!']}

#Functions
def add_and_edit():
    print("Running add_and_edit()")

def print_all():
    print("Running print_all()")
    
def search_by_title():
    print("Running search_by_title()")
    
def remove_title():
    print("Running remove_title()")
    
def save_library():
    print("Running save_library()")
    
def quit():
    print("Running quit()")
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