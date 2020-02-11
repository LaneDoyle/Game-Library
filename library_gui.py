#!/usr/bin/python3
#Lane Doyle
#2/11/2020

import pickle as pk
import tkinter as tk
from tkinter import scrolledtext

'''The Game Library Program'''

TITLE_FONT = ("Times New Roman", 24)
WIDGET_FONT = ("Arial", 15)

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        lbl_title = tk.Label(text = "Game Library", font = TITLE_FONT)
        lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        btn_add = tk.Button(text = "Add", font = WIDGET_FONT)
        btn_add.grid(row = 1, column = 0)
        
        btn_edit = tk.Button(text = "Edit", font = WIDGET_FONT)
        btn_edit.grid(row = 2, column = 0)
        
        btn_search = tk.Button(text = "Search", font = WIDGET_FONT, 
                               command = self.raise_search)
        btn_search.grid(row = 3, column = 0)
    
        btn_remove = tk.Button(text = "Remove", font = WIDGET_FONT)
        btn_remove.grid(row = 4, column = 0)
        
        btn_save = tk.Button(text = "Save", font = WIDGET_FONT)
        btn_save.grid(row = 5, column = 0)
        
    def raise_search(self):
        search_menu.tkraise()
        

class SearchMenu(tk.Frame):        
    def __init__(self):
        tk.Frame.__init__(self)
        lbl_title = tk.Label(text = "Search", font = TITLE_FONT)
        lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        lbl_searchby = tk.Label(text = "Search By:", font = TITLE_FONT)
        lbl_searchby.grid(row = 1, column = 0, sticky = "news")     
        
        ent_searchby = tk.Entry(font = WIDGET_FONT)
        ent_searchby.grid(row = 2, column = 0, sticky = "news")
        
        lbl_searchfor = tk.Label(text = "Search For:", font = TITLE_FONT)
        lbl_searchfor.grid(row = 3, column = 0, sticky = "news")        
        
        ent_searchfor = tk.Entry(font = WIDGET_FONT)
        ent_searchfor.grid(row = 4, column = 0, sticky = "news")
        
        lbl_filters = tk.Label(text = "Print Filters:", font = TITLE_FONT)
        lbl_filters.grid(row = 1, column = 1, sticky = "news")
        
        chk_genre = tk.Checkbutton(text='Genre', onvalue = 1, offvalue = 0)
        chk_genre.grid(row = 2, column = 1, sticky = "news")
        
        chk_title = tk.Checkbutton(text='Title', onvalue = 1, offvalue = 0)
        chk_title.grid(row = 2, column = 2, sticky = "news")
        
        chk_developer = tk.Checkbutton(text='Developer', onvalue = 1, offvalue = 0)
        chk_developer.grid(row = 3, column = 1, sticky = "news")
        
        chk_publisher = tk.Checkbutton(text='Publisher', onvalue = 1, offvalue = 0)
        chk_publisher.grid(row = 3, column = 2, sticky = "news")
        
        chk_system = tk.Checkbutton(text='System', onvalue = 1, offvalue = 0)
        chk_system.grid(row = 4, column = 1, sticky = "news")
        
        chk_purchasedate= tk.Checkbutton(text='Purchase Date', onvalue = 1, offvalue = 0)
        chk_purchasedate.grid(row = 4, column = 2, sticky = "news")
        
        chk_sme = tk.Checkbutton(text='Single/Multi/Either', onvalue = 1, offvalue = 0)
        chk_sme.grid(row = 5, column = 1, sticky = "news")
        
        chk_price = tk.Checkbutton(text='Genre', onvalue = 1, offvalue = 0)
        chk_price.grid(row = 5, column = 2, sticky = "news")
        
        chk_releasedate = tk.Checkbutton(text='Release Date', onvalue = 1, offvalue = 0)
        chk_releasedate.grid(row = 6, column = 1, sticky = "news")
        
        chk_status = tk.Checkbutton(text='Status', onvalue = 1, offvalue = 0)
        chk_status.grid(row = 6, column = 2, sticky = "news")
        
        chk_rating = tk.Checkbutton(text='Rating', onvalue = 1, offvalue = 0)
        chk_rating.grid(row = 7, column = 1, sticky = "news")
        
        #scr_results = scrolledtext(font = WIDGET_FONT, wrap = 'word')
        #scr_results.grid(row = 8, column = 0, columnspan = 2, sticky = "news")
        
        btn_back = tk.Button(text = "Back", font = WIDGET_FONT)
        btn_back.grid(row = 9, column = 0)
    
        btn_submit = tk.Button(text = "Submit", font = WIDGET_FONT)
        btn_submit.grid(row = 9, column = 1)
        
        btn_clear = tk.Button(text = "Clear", font = WIDGET_FONT)
        btn_clear.grid(row = 9, column = 2)        
        
        
        
        
        
if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    #root.title("The Game Library")
    root.geometry("500x500")
    #main_menu = MainMenu()
    #main_menu.grid(row = 0, column = 0, stick = "news")
    
    search_menu = SearchMenu()
    search_menu.grid(row = 0, column = 0, stick = "news")    
    
    #main_menu.tkraise()
    root.mainloop()
        