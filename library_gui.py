#!/usr/bin/python3
#Lane Doyle
#2/11/2020

import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb

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
                                 command = self.raise_add)
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
                                  command = self.save)
        self.btn_save.grid(row = 5, column = 0)
        
    def raise_add(self):
        Screen.current = 2
        AddButtons.clear(self)
        Screen.switch_frame() 
               
    
    def raise_search(self):
        Screen.current = 1
        Screen.switch_frame() 
    
    def raise_removeselection(self):
        pop_up = tk.Tk()
        pop_up.title("Remove Selection")
        frm_edit_select = RemoveSelectionMenu(pop_up)
        frm_edit_select.grid(row = 0, column = 0) 
        
    def save(self):
        popup = tk.Tk()
        popup.title("Saved")
        msg = "File has been saved."
        frm_error = GenericMessage(popup, msg)
        frm_error.grid(row = 0, column = 0)
        datafile = open("game_lib.pickle", "wb")
        pk.dump(games, datafile)
        datafile.close()         
    
    def raise_editselection(self):
        pop_up = tk.Tk()
        pop_up.title("Edit Selection")
        frm_edit_select = EditSelectionMenu(pop_up)
        frm_edit_select.grid(row = 0, column = 0)
               
class AddMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.mode_options = ["", "Single Player", "Multi Player", "Either"]
        self.mode_tkvar = tk.StringVar(self)
        self.mode_tkvar.set(self.mode_options[0])
        
        self.status_options = ["", "Finished", "Unfinished"]
        self.status_tkvar = tk.StringVar(self)
        self.status_tkvar.set(self.status_options[0])        
        
        self.lbl_maintitle = tk.Label(self, text = "Add", font = TITLE_FONT)
        self.lbl_maintitle.grid(row = 0, column = 0, columnspan = 4, sticky = "news")
        
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
        
class SearchMenu(Screen):        
    def __init__(self):
        Screen.__init__(self)
        self.search_options = ["All", "Genre", "Title", "Developer", "Publisher", "System", 
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
        self.frm_printfilters.grid(row = 1, column = 1, rowspan = 4, sticky = "news")
        
        self.scr_results = ScrolledText(self, height = 8, width = 40, font = WIDGET_FONT, wrap = 'word')
        self.scr_results.grid(row = 5, column = 0, columnspan = 2, sticky = "news")
        
        self.frm_searchbuttons = SearchButtons(self)
        self.frm_searchbuttons.grid(row = 6, column = 1, sticky = "news")
        
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
    
    def filter_print(self, entry):
        if self.frm_printfilters.genre_var.get() == True:
            msg = entry[0] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.title_var.get() == True:
            msg = entry[1] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.dev_var.get() == True:
            msg = entry[2] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.pub_var.get() == True:
            msg = entry[3] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.sys_var.get() == True:
            msg = entry[4] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.purchase_var.get() == True:
            msg = entry[5] + "\n"
            self.scr_results.insert("insert", msg) 
            
        if self.frm_printfilters.mode_var.get() == True:
            msg = entry[6] + "\n"
            self.scr_results.insert("insert", msg)
        
        if self.frm_printfilters.price_var.get() == True:
            msg = entry[7] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.release_var.get() == True:
            msg = entry[8] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.status_var.get() == True:
            msg = entry[9] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.rating_var.get() == True:
            msg = entry[10] + "\n"
            self.scr_results.insert("insert", msg)
            
        if self.frm_printfilters.notes_var.get() == True:
            msg = entry[11] + "\n"
            self.scr_results.insert("insert", msg)
            
        msg = "**********************\n"
        self.scr_results.insert("insert", msg)
        
    
                
            
      
class PrintFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.genre_var = tk.BooleanVar(self, True)
        self.title_var = tk.BooleanVar(self, True)
        self.dev_var = tk.BooleanVar(self, True)
        self.pub_var = tk.BooleanVar(self, True)
        self.sys_var = tk.BooleanVar(self, True)
        self.purchase_var = tk.BooleanVar(self, True)
        self.mode_var = tk.BooleanVar(self, True)
        self.price_var = tk.BooleanVar(self, True)
        self.release_var = tk.BooleanVar(self, True)
        self.status_var = tk.BooleanVar(self, True)
        self.rating_var = tk.BooleanVar(self, True)
        self.notes_var = tk.BooleanVar(self, True)
        
        
        self.lbl_filters = tk.Label(self, text = "Print Filters:", font = TITLE_FONT)
        self.lbl_filters.grid(row = 0, column = 1, columnspan = 2,  sticky = "news")
        
        self.chk_genre = tk.Checkbutton(self, text='Genre', onvalue = 1, offvalue = 0, 
                                        variable = self.genre_var)
        self.chk_genre.grid(row = 1, column = 1)
        
        self.chk_title = tk.Checkbutton(self, text='Title', onvalue = 1, offvalue = 0,
                                        variable = self.title_var)
        self.chk_title.grid(row = 2, column = 1)
        
        self.chk_developer = tk.Checkbutton(self, text='Developer', onvalue = 1, offvalue = 0,
                                            variable = self.dev_var)
        self.chk_developer.grid(row = 3, column = 1)
        
        self.chk_publisher = tk.Checkbutton(self, text='Publisher', onvalue = 1, offvalue = 0 ,
                                            variable = self.pub_var)
        self.chk_publisher.grid(row = 4, column = 1)
        
        self.chk_system = tk.Checkbutton(self, text='System', onvalue = 1, offvalue = 0,
                                         variable = self.sys_var)
        self.chk_system.grid(row = 1, column = 2)
        
        self.chk_purchasedate= tk.Checkbutton(self, text='Purchase Date', onvalue = 1, offvalue = 0,
                                              variable = self.purchase_var)
        self.chk_purchasedate.grid(row = 2, column = 2)
        
        self.chk_sme = tk.Checkbutton(self, text='Single/Multi/Either', onvalue = 1, offvalue = 0,
                                      variable = self.mode_var)
        self.chk_sme.grid(row = 3, column = 2)
        
        self.chk_price = tk.Checkbutton(self, text='Price', onvalue = 1, offvalue = 0,
                                        variable = self.price_var)
        self.chk_price.grid(row = 4, column = 2)
        
        self.chk_releasedate = tk.Checkbutton(self, text='Release Date', onvalue = 1, offvalue = 0,
                                              variable = self.release_var)
        self.chk_releasedate.grid(row = 1, column = 3)
        
        self.chk_status = tk.Checkbutton(self, text='Status', onvalue = 1, offvalue = 0,
                                         variable = self.status_var)
        self.chk_status.grid(row = 2, column = 3)
        
        self.chk_rating = tk.Checkbutton(self, text='Rating', onvalue = 1, offvalue = 0,
                                         variable = self.rating_var)
        self.chk_rating.grid(row = 3, column = 3)
        self.chk_notes = tk.Checkbutton(self, text='Notes', onvalue = 1, offvalue = 0,
                                         variable = self.notes_var)
        self.chk_notes.grid(row = 4, column = 3)        
        
class SearchButtons(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.btn_back = tk.Button(self, text = "Back", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 0, column = 0)
    
        self.btn_submit = tk.Button(self, text = "Search", font = WIDGET_FONT,
                                    command = self.print_search)
        self.btn_submit.grid(row = 0, column = 2)
        
        self.btn_clear = tk.Button(self, text = "Clear", font = WIDGET_FONT,
                                   command = self.clear)
        self.btn_clear.grid(row = 0, column = 1)
    
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()
    
    def clear(self):
        screens[1].frm_printfilters.genre_var.set(False)
        screens[1].frm_printfilters.title_var.set(False)
        screens[1].frm_printfilters.dev_var.set(False)
        screens[1].frm_printfilters.pub_var.set(False)
        screens[1].frm_printfilters.sys_var.set(False) 
        screens[1].frm_printfilters.purchase_var.set(False) 
        screens[1].frm_printfilters.mode_var.set(False) 
        screens[1].frm_printfilters.price_var.set(False) 
        screens[1].frm_printfilters.release_var.set(False) 
        screens[1].frm_printfilters.status_var.set(False) 
        screens[1].frm_printfilters.rating_var.set(False)
        screens[1].frm_printfilters.notes_var.set(False)
        screens[1].scr_results.delete(0.0, "end")
        
    def submit_search(self):
        screens[1].scr_results.delete(0.0, "end")
        for key in games.keys():
            entry = games[key]
            screens[1].filter_print(entry)
            
    def print_search(self):
        screens[1].scr_results.delete(0.0, "end")
        
        for key in games.keys():
            screens[1].entry = games[key]
            keyword = screens[1].ent_searchfor.get()
            if screens[1].search_tkvar.get() == screens[1].search_options[0]:
                screens[1].filter_print(screens[1].entry)
                
            if screens[1].search_tkvar.get() == screens[1].search_options[1]:
                if keyword in screens[1].entry[0]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[2]:
                if keyword in screens[1].entry[1]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[3]:
                if keyword in screens[1].entry[2]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[4]:
                if keyword in screens[1].entry[3]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[5]:
                if keyword in screens[1].entry[4]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[6]:
                if keyword in screens[1].entry[5]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[7]:
                if keyword in screens[1].entry[6]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[8]:
                if keyword in screens[1].entry[7]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[9]:
                if keyword in screens[1].entry[8]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[10]:
                if keyword in screens[1].entry[9]:
                    screens[1].filter_print(screens[1].entry)
                    
            if screens[1].search_tkvar.get() == screens[1].search_options[11]:
                if keyword in screens[1].entry[10]:
                    screens[1].filter_print(screens[1].entry)    
         
class AddButtons(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.btn_back = tk.Button(self, text = "Cancel", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 0, column = 0)
    
        self.btn_submit = tk.Button(self, text = "Clear", font = WIDGET_FONT,
                                    command = self.clear)
        self.btn_submit.grid(row = 0, column = 1)
        
        self.btn_clear = tk.Button(self, text = "Confirm", font = WIDGET_FONT,
                                   command = self.confirm)
        self.btn_clear.grid(row = 0, column = 2)
        
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()
    
    def confirm(self):
        entry = []
        entry.append(screens[2].ent_genre.get())
        entry.append(screens[2].ent_title.get())
        entry.append(screens[2].ent_dev.get())
        entry.append(screens[2].ent_pub.get())
        entry.append(screens[2].ent_system.get())
        entry.append(screens[2].ent_release.get())
        entry.append(screens[2].ent_rating.get())
        entry.append(screens[2].mode_tkvar.get())
        entry.append(screens[2].ent_price.get())
        entry.append(screens[2].status_tkvar.get())
        entry.append(screens[2].ent_purchase.get())
        entry.append(screens[2].scr_notes.get(0.0, "end"))
        games[len(games) + 1] = entry
        popup = tk.Tk()
        popup.title("Success")
        msg = "Title has been added."
        frm_error = GenericMessage(popup, msg)
        frm_error.grid(row = 0, column = 0)
        
        Screen.current = 0
        Screen.switch_frame()        
        
        
    def clear(self):
        screens[2].ent_genre.delete(0, "end")
        screens[2].ent_title.delete(0, "end")
        screens[2].ent_dev.delete(0, "end")
        screens[2].ent_pub.delete(0, "end")
        screens[2].ent_system.delete(0, "end")
        screens[2].ent_purchase.delete(0, "end")
        screens[2].ent_price.delete(0, "end")
        screens[2].ent_release.delete(0, "end")
        screens[2].ent_rating.delete(0, "end")
        screens[2].scr_notes.delete(0.0, "end")
        screens[2].mode_tkvar.set(screens[2].mode_options[0])
        screens[2].status_tkvar.set(screens[2].status_options[0])
        
class EditButtons(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        
        self.btn_back = tk.Button(self, text = "Cancel", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 0, column = 0)
    
        self.btn_submit = tk.Button(self, text = "Reset", font = WIDGET_FONT,
                                    command = self.reset)
        self.btn_submit.grid(row = 0, column = 1)
        
        self.btn_clear = tk.Button(self, text = "Confirm", font = WIDGET_FONT,
                                   command = self.confirm)
        self.btn_clear.grid(row = 0, column = 2)
        
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()  
    
    def confirm(self):
        entry = []
        entry.append(screens[3].ent_genre.get())
        entry.append(screens[3].ent_title.get())
        entry.append(screens[3].ent_dev.get())
        entry.append(screens[3].ent_pub.get())
        entry.append(screens[3].ent_system.get())
        entry.append(screens[3].ent_release.get())
        entry.append(screens[3].ent_rating.get())
        entry.append(screens[3].mode_tkvar.get())
        entry.append(screens[3].ent_price.get())
        entry.append(screens[3].status_tkvar.get())
        entry.append(screens[3].ent_purchase.get())
        entry.append(screens[3].scr_notes.get(0.0, "end"))
        games[screens[3].edit_key] = entry
        
        Screen.current = 0
        Screen.switch_frame()  
        screens[3].edit_key
        
    def reset(self):
        self.master.update()       

class EditMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.edit_key = 0
        self.mode_options = ["", "Single Player", "Multi Player", "Either"]
        self.mode_tkvar = tk.StringVar(self)
        self.mode_tkvar.set(self.mode_options[0])
        
        self.status_options = ["", "Finished", "Unfinished"]
        self.status_tkvar = tk.StringVar(self)
        self.status_tkvar.set(self.status_options[0])        
        
        self.lbl_title = tk.Label(self, text = "Edit", font = TITLE_FONT)
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
        
        self.frm_editbuttons = EditButtons(self)
        self.frm_editbuttons.grid(row = 8, column = 1, columnspan = 2, sticky = "ew")
        
    def update(self):
        entry = games[self.edit_key]
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])
        self.ent_title.delete(0, "end")
        self.ent_title.insert(0, entry[1])
        self.ent_dev.delete(0, "end")
        self.ent_dev.insert(0, entry[2])
        self.ent_pub.delete(0, "end")
        self.ent_pub.insert(0, entry[3])
        self.ent_system.delete(0, "end")
        self.ent_system.insert(0, entry[4])
        self.ent_purchase.delete(0, "end")
        self.ent_purchase.insert(0, entry[10])
        self.ent_price.delete(0, "end")
        self.ent_price.insert(0, entry[8])
        self.ent_release.delete(0, "end")
        self.ent_release.insert (0, entry[5])
        self.ent_rating.delete(0, "end")
        self.ent_rating.insert (0, entry[6])
        self.scr_notes.delete(0.0, "end")
        self.scr_notes.insert (0.0, entry[11])
            
        if entry[7].lower() == "single player":
            self.mode_tkvar.set(self.mode_options[1])
        elif entry[7].lower() == "multi player":
            self.mode_tkvar.set(self.mode_options[2])
        elif entry[7].lower() == "either":
            self.mode_tkvar.set(self.mode_options[3])
        else:
            self.mode_tkvar.set(self.mode_options[0])
            
        if entry[9].lower() == "finished":
            self.status_tkvar.set(self.status_options[1])
        elif entry[9].lower() == "unfinished":
            self.status_tkvar.set(self.status_options[2])
        else:
            self.status_tkvar.set(self.status_options[0])
            
        
                
        
         
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
                                    command = self.raise_edit)
        self.btn_submit.grid(row = 2, column = 1)
    
    def raise_main(self):
        self.parent.destroy()
        
    def raise_edit(self):
        if self.edit_tkvar.get() == self.edit_options[0]:
            popup = tk.Tk()
            popup.title("ERROR")
            msg = "ERROR: Please select a title"
            frm_error = GenericMessage(popup, msg)
            frm_error.grid(row = 0, column = 0)
        else:
            for i in range(len(self.edit_options)):
                if self.edit_tkvar.get() == self.edit_options[i]:
                    screens[3].edit_key = i
                    break
            Screen.current = 3
            screens[Screen.current].update()
            Screen.switch_frame()
            self.parent.destroy()
        
class RemoveSelectionMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.remove_options = ["Select a Title"]
        for key in games.keys():
            self.remove_options.append(games[key][1])
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
        if self.remove_tkvar.get() == self.remove_options[0]:
            popup = tk.Tk()
            popup.title("ERROR")
            msg = "ERROR: Please select a title"
            frm_error = GenericMessage(popup, msg)
            frm_error.grid(row = 0, column = 0)
        else:
            for i in range(len(self.remove_options)):
                if self.remove_tkvar.get() == self.remove_options[i]:
                    self.remove_key = i
                    screens[4].remove_key = i
                    entry = games[self.remove_key]
                    screens[4].scr_games.delete(0.0, "end")
                    screens[4].scr_games.insert(0.0, entry[1])                     
                    break            
            Screen.current = 4
            Screen.switch_frame()
            self.parent.destroy()
        
            
              
class RemoveMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.remove_key = 0
        self.lbl_title = tk.Label(self, text = "These are the titles marked for removal:", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
        
        self.scr_games = ScrolledText(self, height = 8, width = 40, font = WIDGET_FONT, wrap = 'word')
        self.scr_games.grid(row = 1, column = 0, columnspan = 2, sticky = "news") 
        
        self.btn_back = tk.Button(self, text = "Cancel", font = WIDGET_FONT,
                                  command = self.raise_main)
        self.btn_back.grid(row = 2, column = 0)
    
        self.btn_verify = tk.Button(self, text = "Remove", font = WIDGET_FONT,
                                    command = self.remove)
        self.btn_verify.grid(row = 2, column = 1)
    
    def remove(self):
        temp_remove_key = self.remove_key
        for key in range(1, len(games)+1):
            if key >= temp_remove_key and key != len(games):
                games[key] = games[key + 1]
        games.pop(len(games))

                           
        Screen.current = 0
        Screen.switch_frame()
    
    def raise_main(self):
        Screen.current = 0
        Screen.switch_frame()        
        
        

class GenericMessage(tk.Frame):
    def __init__(self, parent, msg =  "generic"):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.lbl_continue = tk.Label(self, text = msg)
        self.lbl_continue.grid(row = 0, column = 0)
        
        self.btn_ok = tk.Button(self, text = "Ok", 
                                command = self.parent.destroy)
        self.btn_ok.grid(row = 1, column = 0)
     
if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    root.title("The Game Library")
    root.geometry("900x700") 
    
    screens = [MainMenu(), SearchMenu(), AddMenu(), EditMenu(), RemoveMenu()]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    
    screens[0].tkraise()
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()    