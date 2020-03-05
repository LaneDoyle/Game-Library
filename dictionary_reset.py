#!/usr/bin/python3
#Lane Doyle
#1/28/20

import pickle 

'''Program to reset the dictionary'''

games = {1: ['FPS', 'Halo 3', 'Bungee', 'Microsoft', 'Xbox 360', '2007',
             '7', 'Either', '30.00', 'Yes', '1/15/2008', 'This game blows chunks!'],
         2: ['Sandbox', 'Minecraft', 'Mojang', 'Mojang', 'Xbox One', '2011',
             '10', 'Either', '40.00', '', '3/15/2017', ''],
         3: ['Action Role-Playing', 'Fallout 4', 'Bethesda Game Studios', 'Bethesda Softworks', 
             'Xbox One', '2015', '7', 'Single Player', '70.00', 'Yes', '12/25/2015', 'Best game ever!'],
         4: ['Action Role-Playing', 'Fallout New Vegas', 'Bethesda Game Studios', 'Bethesda Softworks', 
             'Xbox One', '2010', '9', 'Single Player', '40.00', 'Yes', '2/23/2017', 'Really good!']}

data_file = open("game_lib.pickle", "wb")
pickle.dump(games, data_file)
data_file.close()