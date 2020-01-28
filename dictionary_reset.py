#!/usr/bin/python3
#Lane Doyle
#1/28/20

import pickle 

'''Program to reset the dictionary'''

games = {1: ['FPS', 'Halo 3', 'Bungee', 'Microsoft', 'Xbox 360', '2007',
             '10', 'either', '30.00', 'Yes', '1/15/2008', 'This game blows chunks!'],
         2: ['Sandbox', 'Minecraft', 'Mojang', 'Mojang', 'Xbox One', '2011',
             '10', 'either', '40.00', 'N/A', '3/15/2017', ''],
         3: ['Action Role-Playing', 'Fallout 4', 'Bethesda Game Studios', 'Bethesda Softworks', 
             'Xbox One', '2015', '7', 'Single', '70.00', 'Yes', '12/25/2015', 'Best game ever!']}

data_file = open("game_lib.pickle", "wb")
pickle.dump(games, data_file)
data_file.close()