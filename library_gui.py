#!/usr/bin/python3
#Lane Doyle
#2/11/2020

import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

'''The Game Library Program'''

TITLE_FONT = ("Times New Roman", 24)
WIDGET_FONT = ("Arial", 15)

class Screen(tk.Frame):
    current = 0 
    def __init__(self):
        tk.Frame.__init__(self)
    
    def switch_frame():
        screens[Screen.current].tkraise()
        
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "Add", font = WIDGET_FONT,
                                 command = self.raise_addedit)
        self.btn_add.grid(row = 1, column = 0)
        
        self.btn_edit = tk.Button(self, text = "Edit", font = WIDGET_FONT,
                                  command = self.raise_editselection)
        self.btn_edit.grid(row = 2, column = 0)
        
        self.btn_search = tk.Button(self, text = "Search", font = WIDGET_FONT,
                                    command = self.raise_search)
        self.btn_search.grid(row = 3, column = 0)
    
        self.btn_remove = tk.Button(self, text = "Remove", font = WIDGET_FONT,
                                    command = self.raise_removeselection)
        self.btn_remove.grid(row = 4, column = 0)
        
        self.btn_save = tk.Button(self, text = "Save", font = WIDGET_FONT,
                                  command = self.raise_save)
        self.btn_save.grid(row = 5, column = 0)
        
    def raise_addedit(self):
        Screen.current = 2
        Screen.switch_frame()  
    
    def raise_search(self):
        Screen.current = 1
        Screen.switch_frame() 
    
    def raise_removeselection(self):
        pop_up = tk.Tk()
        pop_up.title("Remove Selection")
        frm_edit_select = RemoveSelectionMenu(pop_up)
        frm_edit_select.grid(row = 0, column = 0) 
        
    def raise_save(self):
        print("File Saved.")
    
    def raise_editselection(self):
        pop_up = tk.Tk()
        pop_up.title("Edit Selection")
        frm_edit_select = EditSelectionMenu(pop_up)
        frm_edit_select.grid(row = 0, column = 0)
               

class SearchMenu(Screen):        
    def __init__(self):
        Screen.__init__(self)
        self.search_options = ["Genre", "Title", "Developer", "Publisher", "System", 
                   "Release Date", "Rating", "Mode", "Price", "Status",
                   "Purchase Date"]
        self.search_tkvar = tk.StringVar(self)
        self.search_tkvar.set(self.search_options[0])
        
        self.lbl_title = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        self.lbl_searchby = tk.Label(self, text = "Search By:", font = TITLE_FONT)
        self.lbl_searchby.grid(row = 1, column = 0, sticky = "news")     
        
        self.dbx_searchby = tk.OptionMenu(self, self.search_tkvar, *self.search_options)
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
        
        self.btn_back = tk.Button(self, text = "Back", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 0, column = 0)
    
        self.btn_submit = tk.Button(self, text = "Submit", font = WIDGET_FONT,
                                    command = self.raise_main)
        self.btn_submit.grid(row = 0, column = 2)
        
        self.btn_clear = tk.Button(self, text = "Clear", font = WIDGET_FONT)
        self.btn_clear.grid(row = 0, column = 1)
    
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()
    
        
class AddButtons(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.btn_back = tk.Button(self, text = "Cancel", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 0, column = 0)
    
        self.btn_submit = tk.Button(self, text = "Reset", font = WIDGET_FONT,
                                    command = "")
        self.btn_submit.grid(row = 0, column = 1)
        
        self.btn_clear = tk.Button(self, text = "Confirm", font = WIDGET_FONT,
                                   command = self.raise_main)
        self.btn_clear.grid(row = 0, column = 2)
        
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()    
        

class AddEditMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.mode_options = ["Single", "Multi_Player", "Either"]
        self.mode_tkvar = tk.StringVar(self)
        self.mode_tkvar.set(self.mode_options[0])
        
        self.status_options = ["Yes", "No"]
        self.status_tkvar = tk.StringVar(self)
        self.status_tkvar.set(self.status_options[0])        
        
        self.lbl_title = tk.Label(self, text = "Add and Edit", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 4, sticky = "news")
        
        self.lbl_genre = tk.Label(self, text = "Genre:", font = TITLE_FONT)
        self.lbl_genre.grid(row = 1, column = 0, sticky = "news")        
        
        self.ent_genre = tk.Entry(self, font = WIDGET_FONT)
        self.ent_genre.grid(row = 1, column = 1, sticky = "news")
        
        self.lbl_title = tk.Label(self, text = "Title:", font = TITLE_FONT)
        self.lbl_title.grid(row = 1, column = 2, sticky = "news")        
        
        self.ent_title = tk.Entry(self, font = WIDGET_FONT)
        self.ent_title.grid(row = 1, column = 3, sticky = "news")
        
        self.lbl_dev = tk.Label(self, text = "Developer:", font = TITLE_FONT)
        self.lbl_dev.grid(row = 2, column = 0, sticky = "news")        
        
        self.ent_dev = tk.Entry(self, font = WIDGET_FONT)
        self.ent_dev.grid(row = 2, column = 1, sticky = "news")
        
        self.lbl_pub = tk.Label(self, text = "Publisher:", font = TITLE_FONT)
        self.lbl_pub.grid(row = 2, column = 2, sticky = "news")        
        
        self.ent_pub = tk.Entry(self, font = WIDGET_FONT)
        self.ent_pub.grid(row = 2, column = 3, sticky = "news")
        
        self.lbl_system = tk.Label(self, text = "System:", font = TITLE_FONT)
        self.lbl_system.grid(row = 3, column = 0, sticky = "news")        
        
        self.ent_system = tk.Entry(self, font = WIDGET_FONT)
        self.ent_system.grid(row = 3, column = 1, sticky = "news")
        
        self.lbl_release = tk.Label(self, text = "Release Date:", font = TITLE_FONT)
        self.lbl_release.grid(row = 3, column = 2, sticky = "news")        
        
        self.ent_release = tk.Entry(self, font = WIDGET_FONT)
        self.ent_release.grid(row = 3, column = 3, sticky = "news") 
        
        self.lbl_rating = tk.Label(self, text = "Rating:", font = TITLE_FONT)
        self.lbl_rating.grid(row = 4, column = 0, sticky = "news")        
        
        self.ent_rating = tk.Entry(self, font = WIDGET_FONT)
        self.ent_rating.grid(row = 4, column = 1, sticky = "news")
        
        self.lbl_mode = tk.Label(self, text = "Mode:", font = TITLE_FONT)
        self.lbl_mode.grid(row = 4, column = 2, sticky = "news")        
        
        self.dbx_mode = tk.OptionMenu(self, self.mode_tkvar, *self.mode_options)
        self.dbx_mode.grid(row = 4, column = 3, sticky = "news")
        
        self.lbl_price = tk.Label(self, text = "Price:", font = TITLE_FONT)
        self.lbl_price.grid(row = 5, column = 0, sticky = "news")        
        
        self.ent_price = tk.Entry(self, font = WIDGET_FONT)
        self.ent_price.grid(row = 5, column = 1, sticky = "news")        
        
        self.lbl_status = tk.Label(self, text = "Status:", font = TITLE_FONT)
        self.lbl_status.grid(row = 5, column = 2, sticky = "news")        
        
        self.dbx_status = tk.OptionMenu(self, self.status_tkvar, *self.status_options)
        self.dbx_status.grid(row = 5, column = 3, sticky = "news")
        
        self.lbl_purchase = tk.Label(self, text = "Purchase Date:", font = TITLE_FONT)
        self.lbl_purchase.grid(row = 6, column = 0, sticky = "news")
        
        self.ent_purchase = tk.Entry(self, font = WIDGET_FONT)
        self.ent_purchase.grid(row = 6, column = 1, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text = "Notes:", font = TITLE_FONT)
        self.lbl_notes.grid(row = 7, column = 0, sticky = "news")        
        
        self.scr_notes = ScrolledText(self, height = 8, width = 40, font = WIDGET_FONT, wrap = 'word')
        self.scr_notes.grid(row = 7, column = 1, columnspan = 2, sticky = "news")
        
        self.frm_addbuttons = AddButtons(self)
        self.frm_addbuttons.grid(row = 8, column = 1, columnspan = 2, sticky = "ew")        
        
class EditSelectionMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.edit_options = ["Select a Title"]
        for key in games.keys():
            self.edit_options.append(games[key][1])
        self.edit_tkvar = tk.StringVar(self)
        self.edit_tkvar.set(self.edit_options[0])
        
        self.lbl_title = tk.Label(self, text = "Which title would you like to edit?", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.dbx_games = tk.OptionMenu(self, self.edit_tkvar, *self.edit_options)
        self.dbx_games.grid(row = 1, column = 0, columnspan = 2, sticky = "news")
        
        self.btn_back = tk.Button(self, text = "Cancel", font = WIDGET_FONT, 
                                  command = self.raise_main)
        self.btn_back.grid(row = 2, column = 0)
    
        self.btn_submit = tk.Button(self, text = "Edit", font = WIDGET_FONT,
                                    command = self.raise_addedit)
        self.btn_submit.grid(row = 2, column = 1)
    
    def raise_main(self):
        self.parent.destroy()
        
    def raise_addedit(self):
        Screen.current = 2
        Screen.switch_frame() 
        self.parent.destroy()
        
class RemoveSelectionMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.remove_options = ["Title 1", "Title 2"]
        self.remove_tkvar = tk.StringVar(self)
        self.remove_tkvar.set(self.remove_options[0])       
        
        self.lbl_title = tk.Label(self, text = "Which title would you like to remove?", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.dbx_games = tk.OptionMenu(self, self.remove_tkvar, *self.remove_options)
        self.dbx_games.grid(row = 1, column = 0, columnspan = 2, sticky = "news")
        
        self.btn_back = tk.Button(self, text = "Cancel", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 2, column = 0)
    
        self.btn_verify = tk.Button(self, text = "Verify", font = WIDGET_FONT,
                                    command = self.raise_remove)
        self.btn_verify.grid(row = 2, column = 1)
        
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()
        self.parent.destroy()
        
    def raise_remove(self):
        Screen.current = 3
        Screen.switch_frame()
        self.parent.destroy()
              
class RemoveMenu(Screen):
    def __init__(self):
        Screen.__init__(self)       
        
        self.lbl_title = tk.Label(self, text = "These are the titles marked for removal:", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.scr_games = ScrolledText(self, height = 8, width = 40, font = WIDGET_FONT, wrap = 'word')
        self.scr_games.grid(row = 1, column = 0, columnspan = 2, sticky = "news") 
        
        self.btn_back = tk.Button(self, text = "Cancel", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 2, column = 0)
    
        self.btn_verify = tk.Button(self, text = "Remove", font = WIDGET_FONT,
                                    command = self.raise_main)
        self.btn_verify.grid(row = 2, column = 1)
    
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()
 

        
if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    root.title("The Game Library")
    root.geometry("900x700") 
    
    screens = [MainMenu(), SearchMenu(), AddEditMenu(), RemoveMenu()]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    
    screens[0].tkraise()
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()    