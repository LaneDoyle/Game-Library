#!/usr/bin/python3
#Lane Doyle
#2/11/2020

import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

'''The Game Library Program'''

TITLE_FONT = ("Times New Roman", 24)
WIDGET_FONT = ("Arial", 15)

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "Add", font = WIDGET_FONT)
        self.btn_add.grid(row = 1, column = 0)
        
        self.btn_edit = tk.Button(self, text = "Edit", font = WIDGET_FONT)
        self.btn_edit.grid(row = 2, column = 0)
        
        self.btn_search = tk.Button(self, text = "Search", font = WIDGET_FONT, 
                               command = self.raise_search)
        self.btn_search.grid(row = 3, column = 0)
    
        self.btn_remove = tk.Button(self, text = "Remove", font = WIDGET_FONT)
        self.btn_remove.grid(row = 4, column = 0)
        
        self.btn_save = tk.Button(self, text = "Save", font = WIDGET_FONT)
        self.btn_save.grid(row = 5, column = 0)
        
    def raise_search(self):
        search_menu.tkraise()
        

class SearchMenu(tk.Frame):        
    def __init__(self):
        tk.Frame.__init__(self)
        options = ["Genre", "Title", "Developer", "Publisher", "System", 
                   "Release Date", "Rating", "Mode", "Price", "Status",
                   "Purchase Date"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        
        self.lbl_title = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_searchby = tk.Label(self, text = "Search By:", font = TITLE_FONT)
        self.lbl_searchby.grid(row = 1, column = 0, sticky = "news")     
        
        self.dbx_searchby = tk.OptionMenu(self, tkvar, *options)
        self.dbx_searchby.grid(row = 2, column = 0, sticky = "news")
        
        self.lbl_searchfor = tk.Label(self, text = "Search For:", font = TITLE_FONT)
        self.lbl_searchfor.grid(row = 3, column = 0, sticky = "news")        
        
        self.ent_searchfor = tk.Entry(self, font = WIDGET_FONT)
        self.ent_searchfor.grid(row = 4, column = 0, sticky = "news")

        self.frm_printfilters = PrintFilters(self)
        self.frm_printfilters.grid(row = 4, column = 1, sticky = "news")
        
        self.scr_results = ScrolledText(self, height = 8, width = 40, font = WIDGET_FONT, wrap = 'word')
        self.scr_results.grid(row = 5, column = 0, columnspan = 2, sticky = "news")
        
        self.frm_searchbuttons = SearchButtons(self)
        self.frm_searchbuttons.grid(row = 6, column = 1, sticky = "news")       
      
class PrintFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.lbl_filters = tk.Label(self, text = "Print Filters:", font = TITLE_FONT)
        self.lbl_filters.grid(row = 0, column = 1, columnspan = 2,  sticky = "news")
        
        self.chk_genre = tk.Checkbutton(self, text='Genre', onvalue = 1, offvalue = 0)
        self.chk_genre.grid(row = 1, column = 1)
        
        self.chk_title = tk.Checkbutton(self, text='Title', onvalue = 1, offvalue = 0)
        self.chk_title.grid(row = 2, column = 1)
        
        self.chk_developer = tk.Checkbutton(self, text='Developer', onvalue = 1, offvalue = 0)
        self.chk_developer.grid(row = 3, column = 1)
        
        self.chk_publisher = tk.Checkbutton(self, text='Publisher', onvalue = 1, offvalue = 0)
        self.chk_publisher.grid(row = 4, column = 1)
        
        self.chk_system = tk.Checkbutton(self, text='System', onvalue = 1, offvalue = 0)
        self.chk_system.grid(row = 1, column = 2)
        
        self.chk_purchasedate= tk.Checkbutton(self, text='Purchase Date', onvalue = 1, offvalue = 0)
        self.chk_purchasedate.grid(row = 2, column = 2)
        
        self.chk_sme = tk.Checkbutton(self, text='Single/Multi/Either', onvalue = 1, offvalue = 0)
        self.chk_sme.grid(row = 3, column = 2)
        
        self.chk_price = tk.Checkbutton(self, text='Genre', onvalue = 1, offvalue = 0)
        self.chk_price.grid(row = 4, column = 2)
        
        self.chk_releasedate = tk.Checkbutton(self, text='Release Date', onvalue = 1, offvalue = 0)
        self.chk_releasedate.grid(row = 1, column = 3)
        
        self.chk_status = tk.Checkbutton(self, text='Status', onvalue = 1, offvalue = 0)
        self.chk_status.grid(row = 2, column = 3)
        
        self.chk_rating = tk.Checkbutton(self, text='Rating', onvalue = 1, offvalue = 0)
        self.chk_rating.grid(row = 3, column = 3)  
        
class SearchButtons(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.btn_back = tk.Button(self, text = "Back", font = WIDGET_FONT)
        self.btn_back.grid(row = 0, column = 0)
    
        self.btn_submit = tk.Button(self, text = "Submit", font = WIDGET_FONT)
        self.btn_submit.grid(row = 0, column = 1)
        
        self.btn_clear = tk.Button(self, text = "Clear", font = WIDGET_FONT)
        self.btn_clear.grid(row = 0, column = 2)

class AddMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text = "Add", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        self.lbl_genre = tk.Label(self, text = "Genre:", font = TITLE_FONT)
        self.lbl_genre.grid(row = 1, column = 0, sticky = "news")        
        
        self.ent_genre = tk.Entry(self, font = WIDGET_FONT)
        self.ent_genre.grid(row = 1, column = 1, sticky = "news")
        
        self.lbl_title = tk.Label(self, text = "Title:", font = TITLE_FONT)
        self.lbl_title.grid(row = 1, column = 2, sticky = "news")        
        
        self.ent_title = tk.Entry(self, font = WIDGET_FONT)
        self.ent_title.grid(row = 1, column = 3, sticky = "news")        
        
        
if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    #root.title("The Game Library")
    #root.geometry("500x500")
    
    #main_menu = MainMenu()
    #main_menu.grid(row = 0, column = 0, stick = "news")
    
    #search_menu = SearchMenu()
    #search_menu.grid(row = 0, column = 0, stick = "news")
    
    add_menu = AddMenu()
    add_menu.grid(row = 0, column = 0, stick = "news")
    
    #main_menu.tkraise()
    root.mainloop()
        