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
    #print("Running add_and_edit()")
    
    while True:
        print('''
        ---------------------
        Changing Your Library
        ---------------------
        
        Editing Options:
        1) Add a game
        2) Edit an already existing game
        ''')
        editing_option = input("What would you like to do? ")
        
        if editing_option == '1':
            add()
            continue_edit = False
            
        elif editing_option == '2':
            edit()
            continue_edit = False
        confirmation = input("Would you like to continue editing? ")
        if confirmation.lower() == "n":
            break
def add():
    new_key = len(games) + 1
    valid = False
    while not valid:
        new_genre = input("What is the genre? ")
        new_title = input("What is the title? ")
        new_developer = input("Who is the developer? ")
        new_publisher = input("Who is the publisher? ")
        new_system = input("What is the system it is played on? ")
        new_release = input("What is the release date? ")
        new_rating = input("What is the rating? ")
        new_sme = input("Is it single player, mulit, or either? ")
        new_price = input("What is the price? ")
        new_beat = input("Have you beaten it? ")
        new_purchase = input("What is the purchase date? ")
        new_notes = input("Any notes? ")
        new_entry = [new_genre, new_title, new_developer, new_publisher, new_system,
                     new_release, new_rating, new_sme, new_price, new_beat, new_purchase,
                     new_notes]
        print("------------------------")
        print("Genre: ", new_genre)
        print("Title: ", new_title)
        print("Developer: ", new_developer)
        print("Publisher: ", new_publisher)
        print("System: ", new_system)
        print("Release Date: ", new_release)
        print("Rating: ", new_rating)
        print("Single/multi/either: ", new_sme)
        print("Price: ", new_price)
        print("Beat it?: ", new_beat)
        print("Purchase Date: ", new_purchase)
        print("Notes: ", new_notes)
        answer = input("Is all of this information correct? Y/N ")
        if answer.lower() == "y":
            valid = True
            games[new_key] = new_entry  
def edit():
    valid = False
    while not valid:
        print("Your current library: ")
        for key in games.keys():
            print(key, "-", games[key][1])
        edit_key = input("Which game would you like to edit? ")
        edit_key = int(edit_key)
        edit_entry = games[edit_key]
        if edit_key in games:
            print("Current genre: ", edit_entry[0])
            edit_entry[0] = input("New Genre: ")
            print("")
            print("Current title: ", edit_entry[1])
            edit_entry[1] = input("New title: ")
            print("")
            print("Current developer: ", edit_entry[2])
            edit_entry[2] = input("New developer: ")
            print("")
            print("Current publisher: ", edit_entry[3])
            edit_entry[3] = input("New publisher: ")
            print("")
            print("Current system: ", edit_entry[4])
            edit_entry[4] = input("New system: ")
            print("")
            print("Current release date: ", edit_entry[5])
            edit_entry[5] = input("New release date: ")
            print("Current rating: ", edit_entry[6])
            print("")
            edit_entry[6] = input("New rating: ") 
            print("Current single player/multi/either: ", edit_entry[7])
            edit_entry[7] = input("New single player/multi/either: ")
            print("")
            print("Current price: ", edit_entry[8])
            edit_entry[8] = input("New price: ")
            print("")
            print("Current status(beaten): ", edit_entry[9])
            edit_entry[9] = input("New status: ")
            print("")
            print("Current purchase date: ", edit_entry[10])
            edit_entry[10] = input("New purchase date: ")
            print("")
            print("Current notes: ", edit_entry[11])
            edit_entry[11] = input("New notes: ")
            
            print("------------------------")
            print("Genre: ", edit_entry[0])
            print("Title: ", edit_entry[1])
            print("Developer: ", edit_entry[2])
            print("Publisher: ", edit_entry[3])
            print("System: ", edit_entry[4])
            print("Release Date: ", edit_entry[5])
            print("Rating: ", edit_entry[6])
            print("Single/multi/either: ", edit_entry[7])
            print("Price: ", edit_entry[8])
            print("Beat it?: ", edit_entry[9])
            print("Purchase Date: ", edit_entry[10])
            print("Notes: ", edit_entry[11])
            
            answer = input("Is all of this information correct? Y/N ")
            if answer.lower() == "y":
                valid = True
                edit_entry = games[edit_key]
        else:
            print("NO MATCHES FOUND!") 
            
def print_all():
    #print("Running print_all()")
    games_key_list = games.keys()
    
    for key in games_key_list:
        print()
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
    
def search():
    #print("Running search_by_title()")
    while True:
        print('''
        ----------------------
        Searching Your Library
        ----------------------
        
        Search Options:
        1) Genre
        2) Title
        3) Developer
        4) Publisher 
        5) System 
        6) Release Date
        7) Rating 
        8) Single Player/Multi/Either
        9) Price
        10) Beat it?
        11) Purchase Date
        ''')
        search_option = input("What would you like to search by? ")
        
        if search_option == '1':
            search_by_genre()
        elif search_option == '2':
            search_by_title()
        elif search_option == '3':
            search_by_developer()
        elif search_option == '4':
            search_by_publisher()
        elif search_option == '5':
            search_by_system()
        elif search_option == '6':
            search_by_release()
        elif search_option == '7':
            search_by_rating()
        elif search_option == '8':
            search_by_sme()
        elif search_option == '9':
            search_by_price()
        elif search_option == '10':
            search_by_beat()
        elif search_option == '11':
            search_by_purchasedate()
        else:
            print("That is not a valid option!")               
        
        search_input = input("Would you like to continue searching? Y/N ")
        
        if search_input == 'N' or search_input == 'n':
            break

            
def search_by_title():
    found_one = False
    search_results = {}
    title = input("What is the title of the game? ")
    for key in games.keys():
        if title in games[key][1]:
            found_one = True
            print()
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
    if not found_one:
        print("NO MATCHES FOUND!") 
        
def search_by_genre():
    found_one = False
    genre = input("What is the genre of the game? ")
    for key in games.keys():
        if genre in games[key][0]:
            found_one = True
            print()
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
                        
    if not found_one:
        print("NO MATCHES FOUND!") 
        
def search_by_developer():
    found_one = False
    developer = input("Who developed the game? ")
    for key in games.keys():
        if developer in games[key][2]:
            found_one = True
            print()
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
                       
    if not found_one:
        print("NO MATCHES FOUND!") 
        
def search_by_publisher():
    found_one = False
    publisher = input("Who published the game? ")
    for key in games.keys():
        if publisher in games[key][3]:
            found_one = True
            print()
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
                        
    if not found_one:
        print("NO MATCHES FOUND!")

def search_by_system():
    found_one = False
    system = input("What system is it played on? ")
    for key in games.keys():
        if system in games[key][4]:
            found_one = True
            print()
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
                       
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_release():
    found_one = False
    release = input("When was it released? ")
    for key in games.keys():
        if release in games[key][5]:
            found_one = True
            print()
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
                        
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_rating():
    found_one = False
    rating = input("What is the rating? ")
    for key in games.keys():
        if rating in games[key][6]:
            found_one = True
            print()
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
                       
    if not found_one:
        print("NO MATCHES FOUND!")

def search_by_sme(): 
    #sme = single, multi, or either
    found_one = False
    sme = input("Is it single player, multi or either? ")
    for key in games.keys():
        if sme in games[key][7]:
            found_one = True
            print()
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
                      
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_price():
    found_one = False
    price = input("What was the price of the game? ")
    for key in games.keys():
        if price in games[key][8]:
            found_one = True
            print()
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
                       
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_beat():
    found_one = False
    beat = input("Have you beaten it? ")
    for key in games.keys():
        if beat in games[key][9]:
            found_one = True
            print()
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
                      
    if not found_one:
        print("NO MATCHES FOUND!")
        
def search_by_purchasedate():
    found_one = False
    purchasedate = input("When did ou purchase it? ")
    for key in games.keys():
        if purchasedate in games[key][10]:
            found_one = True
            print()
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
                       
    if not found_one:
        print("NO MATCHES FOUND!")    
    
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
    confirm = input("Are you sure you want to quit? Y/N ")
    if confirm.lower() == "y":
        print("Goodbye!")
        sys.exit()
    elif confirm.lower() == "n":
        pass

#Main Menu    
while True:
    print('''
    ------------------------
    Welcome to your library!
    ------------------------
    
    Main Menu:
    1) Add/Edit Game
    2) Print All Games
    3) Search 
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
        search()
    elif choice == "4":
        remove_title()
    elif choice == "5":
        save_library()
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("That is not a valid option!")    