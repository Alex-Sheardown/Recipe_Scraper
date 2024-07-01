import csv
import re
import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog
from tkinter import ttk
import tkinter.scrolledtext as st 

import pandas as pd

from file_processing import word_counter_in_json, filter_patterns_based_on_strings, filter_individual_names

import sys
sys.path.insert(1, 'G:\Code\Recipe Project\Stage_3_Database and Cleaning\Table_Organizer\Ingredient_processing')  # Replace '/path/to/directory' with the actual directory path

from  process_ingredient import raw_translated_ingredient
from file_processing import apply_regex_patterns



class WelcomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        #self.rowconfigure(0, minsize=800, weight=1)
        #self.columnconfigure(0, minsize=600, weight=1)

        #self.grid(row = 0, column = 0)
        self.first_frame_set_up()

    def first_frame_set_up(self):

        self.first_frame = Frame(self)
        self.first_frame.grid(row=0, column=0, sticky='nsew')
        

        self.first_frame.rowconfigure([0,1,2,3], minsize=150, weight=1)
        self.first_frame.columnconfigure(0, minsize=800, weight=1)



        self.name = tk.Label(self.first_frame, text="File Selection", font=("Helvetica", 30))
        self.name.grid(row=0, column=0, sticky='nsew')


        self.description = tk.Label(self.first_frame, text="Please select a TSV file:")
        self.description.grid(row=1, column=0, sticky='nsew')
        
        
        
        self.drop_frame = tk.Frame(self.first_frame, bg="lightgray", bd=2, relief="raised")
        self.drop_frame.grid(row=2, column=0, sticky='nsew')

        self.file_name = tk.StringVar()
        self.file_name.set("Drag and drop your file here")
        self.drop_label = tk.Label(self.first_frame, textvariable=self.file_name, bg="lightgray")
        self.drop_label.grid(row=2, column=0, sticky='nsew')
        
        self.process_button = tk.Button(self.first_frame, text="Process File", command=self.process_file)
        self.process_button.grid(row=3, column=0, sticky='nsew')

        self.full_file_path = ""
        self.str_file_name = ""
      
        self.drop_frame.bind("<Button-1>", self.select_file)
        self.drop_label.bind("<Button-1>", self.select_file)

    def select_file(self, event):
        file_path = filedialog.askopenfilename(filetypes=[("TSV files", "*.json")])
        self.full_file_path = file_path
        if file_path:
            # Here you can implement the TSV processing logic
            self.file_name.set(os.path.basename(file_path))
            self.str_file_name = os.path.basename(file_path)
            
        else:
            self.drop_label.config(text="Drag and drop your file here")  

    def process_file(self):
        file_path = self.full_file_path
        print("Selected File Path:", file_path)
        if file_path:
            print("found file path: ", file_path)
            self.second_frame_set_up(file_path)
    
    def second_frame_set_up(self, file_path):
        self.first_frame.destroy()
        
        self.geometry("1920x1080") 
        self.title("Spreadsheet Viewer")
        width= self.winfo_screenwidth() 
        height= self.winfo_screenheight()

        #setting tkinter window size
        self.geometry("%dx%d" % (width, height))
        self.state('zoomed') 

        self.general_row = (height-40)/2
        self.general_column = int(((width-90)/4))

        self.font_size = 9
        self.button_width = int(((self.general_column /2)/self.font_size))
        self.button_height = 5

        self.sub_row = int((11*(self.general_row)/12)/6)

        self.second_frame = Frame(self)
        self.second_frame.grid(row=0, column=0, sticky='nsew')


        self.second_frame.rowconfigure(0, minsize=self.general_row, weight=1)
        self.second_frame.rowconfigure([1,2], minsize=self.general_row/2, weight=1)

        
        self.second_frame.columnconfigure(0, minsize=self.general_column , weight=1)
        self.second_frame.columnconfigure(2, minsize=self.general_column , weight=1)
        self.second_frame.columnconfigure(4, minsize=self.general_column , weight=1)
        self.second_frame.columnconfigure(6, minsize=self.general_column , weight=1)

        patterns_filename = "G:\Code\Recipe Project\Stage_3_Database and Cleaning\Table_Organizer\\regex_holder\\"
        self.df, self.df2 = word_counter_in_json(file_path, "ingredients_translated")
        print(self.df2)
        self.current_df2 = self.df2
        #df2 = df
        self.df3 = self.json_to_dataframe(patterns_filename + "useless.json")
        self.df3a = self.df3[self.df3['status'] == 0]
        self.df3b = self.df3[self.df3['status'] != 0]
        self.df4 = self.json_to_dataframe(patterns_filename + "modifier_patterns.json")
        self.df4a = self.df4[self.df4['status'] == 0]
        self.df4b = self.df4[self.df4['status'] != 0]
        self.df5 = self.json_to_dataframe(patterns_filename + "measurement_patterns.json")
        self.df5a = self.df5[self.df5['status'] == 0]
        self.df5b = self.df5[self.df5['status'] != 0]
        self.df5 = self.df5.sort_values(by='name')


        #Tree 1 left top corner frequency of words
        self.tree1, self.scrollbar1 = self.populate_treeview(self.df, 0, 0, self.second_frame, self.general_column )
        self.tree1.bind('<ButtonRelease-1>', self.on_single_click_table_1)
        #self.tree1.bind('<Double-1>', lambda event: self.on_single_click_table_1(event, self.tree1))
        self.tree1.column("# 1", width=40, stretch=False) #anchor=CENTER
        
        #Tree 2 middle top 
        #The difference between edited and non edited
        self.tree2, self.scrollbar2 = self.populate_treeview(self.df2, 0, 2, self.second_frame, self.general_column )
        self.tree2.bind('<ButtonRelease-1>', self.on_double_click_table_2)
        #self.tree2.bind('<Double-1>', lambda event: self.on_double_click_table_2(event, self.tree2))
        self.tree2.grid(columnspan=3)
        self.scrollbar2.grid(column=5)

        #Tree 3 - 5 bottom left start
        #The regex files
        self.tree3a, self.scrollbar3a = self.populate_treeview(self.df3a, 1, 0, self.second_frame, self.general_column )
        self.tree3b, self.scrollbar3b = self.populate_treeview(self.df3b, 2, 0, self.second_frame, self.general_column )
        self.tree3a.bind('<ButtonRelease-1>', self.on_double_click_table_3a)
        self.tree3b.bind('<ButtonRelease-1>', self.on_double_click_table_3b)
        #self.tree3a.bind('<Double-1>', lambda event: self.on_double_click_table_3a(event, self.tree3a))

        self.tree4a, self.scrollbar4a = self.populate_treeview(self.df4a, 1, 2, self.second_frame, self.general_column )
        self.tree4b, self.scrollbar4b = self.populate_treeview(self.df4b, 2, 2, self.second_frame, self.general_column )
        self.tree4a.bind('<ButtonRelease-1>', self.on_double_click_table_4a)
        self.tree4b.bind('<ButtonRelease-1>', self.on_double_click_table_4b)
        self.tree4a.column("# 1",width=120, stretch=False)
        self.tree4b.column("# 1",width=120, stretch=False)

        self.tree5a, self.scrollbar5a = self.populate_treeview(self.df5a, 1, 4, self.second_frame,self.general_column )
        self.tree5b, self.scrollbar5b = self.populate_treeview(self.df5b, 2, 4, self.second_frame,self.general_column )
        self.tree5a.bind('<ButtonRelease-1>', self.on_double_click_table_5a)
        self.tree5b.bind('<ButtonRelease-1>', self.on_double_click_table_5b)
        self.tree5a.column("# 1", width=80, stretch=False)
        self.tree5b.column("# 1", width=80, stretch=False)

        self.third_frame_a_setup()
       
        font_size = 10
        self.text_box = tk.Text(self.second_frame, wrap="word", font=("Arial", font_size), width=int(self.general_column /(font_size)))
        self.scrollbar6 = ttk.Scrollbar(self.second_frame, orient="vertical", command=self.text_box.yview)
        self.text_box.grid(row=1, column=6, rowspan=2, sticky='nsew')
        self.scrollbar6.grid(row=1, column=7, rowspan=2, sticky='nsw')
        self.text_box.config(yscrollcommand=self.scrollbar6.set)

    # This is where we build the rest of the code for the right hand corner frame
    def third_frame_a_setup (self):
        #main text processor
        
        self.third_frame = tk.Frame(self.second_frame)
        self.third_frame.grid(row=0, column=6, columnspan=4, sticky='nsew')
        
        self.third_frame.rowconfigure(0, minsize=int((1*self.general_row)/12), weight=1)
        self.third_frame.rowconfigure(1, minsize=self.sub_row, weight=1)

        #Basic Buttons
        self.third_frame_choice = tk.Frame(self.third_frame)
        self.third_frame_choice.grid(row=0, column=0, sticky='nsew')
        self.third_frame_choice.columnconfigure([0,1], minsize=self.general_column /2, weight=1)

        self.search_button = tk.Button(self.third_frame_choice, width=self.button_width, font=("Arial", self.font_size), text="Search",  height=self.button_height, command=self.search)
        self.search_button.grid(row=0, column=0, sticky='new')
        self.development_button = tk.Button(self.third_frame_choice, width=self.button_width,font=("Arial", self.font_size), text="Development",  height=self.button_height, command=self.build)
        self.development_button.grid(row=0, column=1, sticky='new')

        self.third_frame_build()
        self.third_frame_build_frame.grid_forget()
        self.third_frame_search()

        self.third_frame_search_frame

    def third_frame_build(self):
        #Drop box 1, 0 
        self.third_frame_build_frame = tk.Frame(self.third_frame)
        self.third_frame_build_frame.grid(row=1, column=0, sticky='new')
        self.third_frame_build_frame.rowconfigure([0,1,2,3,4,5], minsize=int(self.sub_row/6), weight=1) 

        self.label2 = tk.Label(self.third_frame_build_frame, text="File:", font=("Arial", 20))
        self.label2.grid(row=0, column=0, sticky="w", padx=0, pady=5)

        self.columns_drop_down = ["Irrelevant", "Modifiers", "Metrics"]
        self.dropdown3 = ttk.Combobox(self.third_frame_build_frame,  font=("Arial", 14), values=self.columns_drop_down)
        self.dropdown3.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.dropdown3.bind("<<ComboboxSelected>>", self.update_dropdown2)


        self.label3 = tk.Label(self.third_frame_build_frame, text="Name:", font=("Arial", 20))
        self.label3.grid(row=1, column=0, sticky="w", padx=0, pady=5)

        # Create name box
        self.name_box = tk.Entry(self.third_frame_build_frame, font=("Arial", 15))
        self.name_box.grid(row=1, column=1, padx=5, pady=5, sticky="new")

        self.label4 = tk.Label(self.third_frame_build_frame, text="Regex:", font=("Arial", 20))
        self.label4.grid(row=2, column=0, sticky="w", padx=0, pady=5)

        # Create regex box
        self.regex_box = tk.Entry(self.third_frame_build_frame, font=("Arial", 15))
        self.regex_box.grid(row=2, column=1, padx=5, pady=5, sticky="new")

        
        self.label5 = tk.Label(self.third_frame_build_frame, text="Modified:", font=("Arial", 20))
        self.label5.grid(row=3, column=0, sticky="w", padx=0, pady=5)

        # Create altered box
        self.altered_regex_box = tk.Entry(self.third_frame_build_frame, font=("Arial", 15))
        self.altered_regex_box.grid(row=3, column=1, padx=5, pady=5, sticky="new")

        self.label5 = tk.Label(self.third_frame_build_frame, text="This the info", font=("Arial", 10))
        self.label5.grid(row=4, column=0, sticky="ew", padx=0, pady=5, columnspan=2 )

        self.third_frame_button = tk.Frame(self.third_frame_build_frame)
        self.third_frame_button.grid(rowspan=2, columnspan=2)

        self.delete_button = tk.Button(self.third_frame_button, width=self.button_width, font=("Arial", self.font_size),    text="Run",  height=self.button_height, command=self.run)
        self.delete_button.grid(row=0, column=0, sticky='new')
        self.save_button = tk.Button(self.third_frame_button, width=self.button_width,font=("Arial", self.font_size),       text="Save",  height=self.button_height, command=self.save)
        self.save_button.grid(row=0, column=1, sticky='new')

        self.test_button = tk.Button(self.third_frame_button, width=self.button_width, font=("Arial", self.font_size),      text="Reset",  height=self.button_height, command=self.reset)
        self.test_button.grid(row=1, column=0, sticky='new')
        self.clear_button = tk.Button(self.third_frame_button, width=self.button_width,font=("Arial", self.font_size),      text="Revert",  height=self.button_height, command=self.revert)
        self.clear_button.grid(row=1, column=1, sticky='new')

    def third_frame_search(self):
        #Drop box 1, 0 
        self.third_frame_search_frame = tk.Frame(self.third_frame)
        self.third_frame_search_frame.grid(row=1, column=0, sticky='new')
        self.third_frame_search_frame.rowconfigure([0,1,2], minsize=int(self.sub_row/3), weight=1)                               
       

        self.third_frame_drop_box = tk.Frame(self.third_frame_search_frame)
        self.third_frame_drop_box.grid(row=0, column=0, sticky='new')
        
        self.third_frame_drop_box.columnconfigure(0, minsize=int((1*self.general_column )/3), weight=1)
        self.third_frame_drop_box.columnconfigure(1, minsize=int((2*self.general_column )/3), weight=1)
   

        # Create dropdown menus
        self.label1 = tk.Label(self.third_frame_drop_box, text="File    :", font=("Arial", 20))
        self.label1.grid(row=0, column=0, sticky="w", padx=0, pady=5)

        self.label2 = tk.Label(self.third_frame_drop_box, text="Column  :", font=("Arial", 20))
        self.label2.grid(row=1, column=0, sticky="w", padx=0, pady=5)

        self.label3 = tk.Label(self.third_frame_drop_box, text="Entry   :", font=("Arial", 20))
        self.label3.grid(row=2, column=0, sticky="w", padx=0, pady=5)

        self.columns_drop_down = ["Count", "Compare", "Irrelevant", "Modifiers", "Metrics"]
        self.dropdown1 = ttk.Combobox(self.third_frame_drop_box,  font=("Arial", 14), values=self.columns_drop_down)
        self.dropdown1.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.dropdown1.bind("<<ComboboxSelected>>", self.update_dropdown2)

       
        self.dropdown2 = ttk.Combobox(self.third_frame_drop_box,  font=("Arial", 14))
        self.dropdown2.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        

        # Create search box
        """
        self.search_box = tk.Entry(self.third_frame_search_frame, font=("Arial", 15))
        self.search_box.grid(row=1, column=0, padx=5, pady=5, sticky="new")
        """

        self.search_box = tk.Entry(self.third_frame_drop_box, font=("Arial", 14))
        self.search_box.grid(row=2, column=1, padx=5, pady=5, sticky="we")

   
        # Create buttons 3, 0
        self.third_frame_end_buttons = tk.Frame(self.third_frame_search_frame)
        self.third_frame_end_buttons.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.third_frame_end_buttons.columnconfigure([0,1], minsize=int(self.general_column /2), weight=1)

        self.search_button = tk.Button(self.third_frame_end_buttons, text="Search", font=("Arial", 15), command=self.search1)
        self.search_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.clear_button = tk.Button(self.third_frame_end_buttons, text="Reset",  font=("Arial", 15), command=self.reset)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
     
    def update_dropdown2(self, event):
        selected_column = self.dropdown1.get()
        if selected_column == "word count": 
            options = self.df
            self.dropdown2.config(values=options)
        elif selected_column == "Comparison 1":
            options = self.df2
            self.dropdown2.config(values=options) 
        elif  selected_column == "Junk Word":
            options = self.df3
            self.dropdown2.config(values=options) 
        elif  selected_column == "Modifiers":
            options = self.df4
            self.dropdown2.config(values=options)
        elif  selected_column =="Measurements":
            options = self.df5# ["Option 1", "Option 2", "Option 3"]  # Sample options based on selected column
            self.dropdown2.config(values=options) 

    #Changes top right hand corner view for the search and build
    def build(self):
        print("Build button clicked")
        self.third_frame_search_frame.grid_forget()
        self.third_frame_build_frame.grid()

    def search(self):
        print("Search button clicked")
        self.third_frame_build_frame.grid_forget()
        self.third_frame_search_frame.grid(sticky="new")

    def filter_and_get_value(self, df, filter_column, filter_value, target_column):

        filtered_df = df[df[filter_column] == filter_value]
        if not filtered_df.empty:
            return filtered_df.iloc[0][target_column]
        else:
            return ""

    def regex_developer(self, value, option):
          
        self.search_box.delete(0, tk.END)
        self.name_box.delete(0, tk.END)
        self.regex_box.delete(0, tk.END)
        self.altered_regex_box.delete(0, tk.END)

        if option == 1:
            self.dropdown1.current(0)
            
            regex_pattern = self.word_to_regex(value[2])
            self.name_box.insert(tk.END, value[2])
            self.regex_box.insert(tk.END,regex_pattern)
            self.altered_regex_box.insert(tk.END, regex_pattern)
            self.search_box.insert(0, value[1])

        elif option == 2:
            self.dropdown1.current(1)
            self.search_box.insert(0, value[1])


        elif option == 3 or option == 4:
            self.dropdown1.current(2)
            self.dropdown3.current(0)
            self.name_box.insert(tk.END, value[2])
            self.search_box.insert(0, value[0])
            
            if option == 3:
                self.regex_box.insert(tk.END,value[0])
                result = self.filter_and_get_value(self.current_df3b, 'id', value[2], 'pattern')
                self.altered_regex_box.insert(tk.END, result)
                
            elif option == 4:
                result = self.filter_and_get_value(self.current_df3a, 'id', value[2], 'pattern')
                self.regex_box.insert(tk.END,result)
                self.altered_regex_box.insert(tk.END, value[0])
               
        elif option == 5 or option == 6:
            self.dropdown1.current(3)
            self.dropdown3.current(1)
            self.name_box.insert(tk.END, value[0])
            self.search_box.insert(0, value[1])
            if option == 5:
                self.regex_box.insert(tk.END,value[1])
                result = self.filter_and_get_value(self.current_df4b, 'name', value[0], 'pattern')
                self.altered_regex_box.insert(tk.END, result)
                self.search_box.insert(0, value[1])
            elif option == 6:
                result = self.filter_and_get_value(self.current_df4a, 'name', value[0], 'pattern')
                self.regex_box.insert(tk.END,result)
                self.altered_regex_box.insert(tk.END, value[1])
        elif option == 7 or option == 8:
            self.dropdown1.current(4)
            self.dropdown3.current(2)
            self.name_box.insert(tk.END, value[0])
            self.search_box.insert(0, value[1])
            if option == 7:
                self.regex_box.insert(tk.END,value[1])
                result = self.filter_and_get_value(self.current_df5b, 'name', value[0], 'pattern')
                self.altered_regex_box.insert(tk.END, result)
            elif option == 8:
                result = self.filter_and_get_value(self.current_df5a, 'name', value[0], 'pattern')
                self.regex_box.insert(tk.END,result)
                self.altered_regex_box.insert(tk.END, value[1])
     
    #Table 1's single click function for the word
    def on_single_click_table_1(self, event):
        print(self.tree1.selection())

        item = self.tree1.selection()[0]
        column = self.tree1.identify_column(event.x)
        region = self.tree1.identify("region", event.x, event.y)
        print("region", region)
        print("column", column)

        if column == "#2":
            value = self.tree1.item(item, 'values')[int(column[1:]) - 1]  # Adjust column index
            print(f"Clicked cell value: {value}")
            if value.isnumeric() == False:
                self.current_df2 = self.filter_word(self.df2, value)
                #self.tree2.delete(*self.tree2.get_children())
                
                self.tree2, self.scrollbar2 = self.populate_treeview(self.current_df2, 0, 2, self.second_frame, self.general_column)
                self.tree2.grid(columnspan=3)
                self.scrollbar2.grid(column=5)

                #Update Search
                self.dropdown1.set("word count")
                self.dropdown2.set("word")
                self.search_box.delete(0, tk.END)
                self.search_box.insert(tk.END, value)

                #Update Regex
                self.regex_developer(value, 0)
                self.fill_in_regex()
                #Update Regex Broad visual
            
                first_entry = self.current_df2.iloc[0]['Original_Word']
                self.summary_box(first_entry)

            else:
                print("here")
                #df = self.filter_id(self.df2, value)
                #self.populate_treeview(df, self.tree2)

    def summary_box(self, first_entry, test_status):
        self.text_box.delete('1.0', tk.END)
        result_list = raw_translated_ingredient(first_entry, False, test_status)
        count = 1
        for result in result_list:
            fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = result
            processed_string = "modifiers:  " + str(fmo) + ",\nmeasurements:   " + str(fme) + ",\ntext:   " + str(text) + ",\nhash: " + str(mod_hash) + ",\nname:  " +  str(name) + ",\nportion:  " + str(portion) + ",\nmulti_part_ingredient_status:  " + str(mpis) + ",\nignore this:  " + str(ignore_this) + "\n\n"
            self.text_box.insert(tk.END, processed_string)

    def fill_in_regex(self):

        self.current_df3a = filter_patterns_based_on_strings(self.df3a, self.current_df2, 'pattern', 'Original_Word')
        self.current_df3b = filter_patterns_based_on_strings(self.df3b, self.current_df2, 'pattern', 'Original_Word')
        self.tree3a, self.scrollbar3a = self.populate_treeview(self.current_df3a, 1, 0, self.second_frame, self.general_column)
        self.tree3b, self.scrollbar3b = self.populate_treeview(self.current_df3b, 2, 0, self.second_frame, self.general_column)
        self.tree3a.bind('<ButtonRelease-1>', self.on_double_click_table_3a)
        self.tree3b.bind('<ButtonRelease-1>', self.on_double_click_table_3b)

        #Modifier
        self.current_df4a = filter_individual_names(self.df4a, self.current_df2, "name", "modifiers")
        self.current_df4b = filter_individual_names(self.df4b, self.current_df2, "name", "modifiers")
        self.tree4a, self.scrollbar4a = self.populate_treeview(self.current_df4a, 1, 2, self.second_frame, self.general_column )
        self.tree4b, self.scrollbar4b = self.populate_treeview(self.current_df4b, 2, 2, self.second_frame, self.general_column )
        self.tree4a.bind('<ButtonRelease-1>', self.on_double_click_table_4a)
        self.tree4b.bind('<ButtonRelease-1>', self.on_double_click_table_4b)
                
        #Pattern
        self.current_df5a = filter_individual_names(self.df5a, self.current_df2, "name", "measurements")
        self.current_df5b = filter_individual_names(self.df5b, self.current_df2, "name", "measurements")
        self.tree5a, self.scrollbar5a = self.populate_treeview(self.current_df5a, 1, 4, self.second_frame,self.general_column )
        self.tree5b, self.scrollbar5b = self.populate_treeview(self.current_df5b, 2, 4, self.second_frame,self.general_column )
        self.tree5a.bind('<ButtonRelease-1>', self.on_double_click_table_5a)
        self.tree5b.bind('<ButtonRelease-1>', self.on_double_click_table_5b)

    def filter_word(self, word_df, filter_word):
        # Filter the DataFrame based on whether the original word contains the filter word
        filtered_df = word_df[word_df['Original_Word'].str.contains(filter_word)].copy()
        #filtered_df = word_df[word_df['Original_Word'].str.contains(filter_word, case=False) | word_df['Processed_Word'].str.contains(filter_word, case=False)].copy()
        filtered_df = word_df[word_df['Original_Word'].str.contains(filter_word, case=False, regex=False) | word_df['Processed_Word'].str.contains(filter_word, case=False, regex=False)].copy()


        return filtered_df
    
    def word_to_regex(self, word):
        # Escape special characters in the word
    

        escaped_word = "\s*" + str(word)
    
        
        return escaped_word

    def retrieve_row(self, tree):
        item_data = ""
        selected_items = tree.selection()  # Get all selected items
        for selected_item in selected_items:
            item_data = tree.item(selected_item)  # Get the item data
            print("Selected item data:", item_data["values"])
            item_data = item_data["values"]
        return item_data

    #Table 2's single click function for the word
    def on_double_click_table_2(self, event):
        """
        item_data = ""
        selected_items = self.tree2.selection()  # Get all selected items
        for selected_item in selected_items:
            item_data = self.tree2.item(selected_item)  # Get the item data
            print("Selected item data:", item_data["values"])
            item_data = item_data["values"]
        """
        item_data = self.retrieve_row(self.tree2)
      
        # Update the filtered DataFrame based on the "Original_Word" column
        self.current_df2 = self.df2[self.df2["Original_Word"] == item_data[1]]

        #self.current_df2 = self.df[self.df.apply(lambda row: (row == selected_df.iloc[0]).all(), axis=1)]
        self.tree2, self.scrollbar2 = self.populate_treeview(self.current_df2, 0, 2, self.second_frame, self.general_column)
        self.tree2.grid(columnspan=3)
        self.scrollbar2.grid(column=5)

        test_status = True
        if item_data[1] == 0:
            test_status = False

        self.summary_box(item_data[1], test_status)
        #Left off here!
        self.regex_developer(item_data, 2)
        self.fill_in_regex()
    #Table 3's single click function for the word
    def on_double_click_table_3a(self, event):
        item_data = self.retrieve_row(self.tree3a)
        self.regex_click(item_data[0])
        self.regex_developer(item_data, 3)

    def on_double_click_table_3b(self, event):
        item_data = self.retrieve_row(self.tree3b)
        self.regex_click(item_data[0])
        self.regex_developer(item_data, 4)

    #Table 4's single click function for the word      
    def on_double_click_table_4a(self, event):
        item_data = self.retrieve_row(self.tree4a)
        self.regex_click(item_data[0])
        self.regex_developer(item_data, 5)
        print("4a test")
    
    def on_double_click_table_4b(self, event):
        item_data = self.retrieve_row(self.tree4b)
        self.regex_click(item_data[0])
        self.regex_developer(item_data, 6)
        print("4b test")

    #Table 5's single click function for the word
    def on_double_click_table_5a(self, event):
        item_data = self.retrieve_row(self.tree5a)
        
        value = item_data[0]
        #value = value.split(" ")
        #self.filter_dataframe_by_regex(value)
        def match_words(words, value):
            return value in [word.strip() for word in words.split(',')]

        # Apply the function to filter the DataFrame
        self.current_df2 = self.df2[self.df2["measurements"].apply(lambda x: match_words(x, value))]
        #print(self.current_df2)
        self.tree2, self.scrollbar2 = self.populate_treeview(self.current_df2, 0, 2, self.second_frame, self.general_column)
        self.tree2.grid(columnspan=3)
        self.scrollbar2.grid(column=5)
      
        try:
            first_entry = self.current_df2.iloc[0]['Original_Word']
    
            self.summary_box(first_entry)
        except:
            print("empty")

        
        self.regex_click(item_data[0])
        self.regex_developer(item_data, 7)
        
    def on_double_click_table_5b(self, event):
        item_data = self.retrieve_row(self.tree5b)
        
        value = item_data[0]
        #value = value.split(" ")
        #self.filter_dataframe_by_regex(value)
        def match_words(words, value):
            return value in [word.strip() for word in words.split(',')]

        # Apply the function to filter the DataFrame
        self.current_df2 = self.df2[self.df2["measurements"].apply(lambda x: match_words(x, value))]
        #print(self.current_df2)
        self.tree2, self.scrollbar2 = self.populate_treeview(self.current_df2, 0, 2, self.second_frame, self.general_column)
        self.tree2.grid(columnspan=3)
        self.scrollbar2.grid(column=5)
        try:
            first_entry = self.current_df2.iloc[0]['Original_Word']
    
            self.summary_box(first_entry)
        except:
            print("empty")

        item_data = self.retrieve_row(self.tree5b)
        self.regex_click(item_data[0])
        self.regex_developer(item_data, 8)

    def filter_dataframe_by_regex(self):
        """
        Filter a DataFrame based on whether its values in a specific column are altered by regex patterns.
        
        Args:
            df (pd.DataFrame): The input DataFrame.
            value_column (str): The column in the DataFrame to apply the regex patterns to.
            patterns (list): A list of regex patterns (either single patterns or lists of patterns).
        
        Returns:
            pd.DataFrame: The filtered DataFrame containing only rows with altered values.
        """
        print("Here5a part 2--------------")
        """
        print(patterns)
        filtered_indices = []
        
        for index, value in self.df2["Original_Word"].items():
            altered_value = apply_regex_patterns(value, patterns)
            if altered_value is not None:
                filtered_indices.append(index)
        
        self.current_df2 = self.df2.loc[filtered_indices].copy()
        
        """

        self.fill_in_regex()

    def filter_df_with_regex(self, pattern):
        # Compile the regex pattern

        regex = re.compile(pattern)
        hold_df = self.df2.copy()
        filtered_df = hold_df[hold_df["Original_Word"].apply(lambda x: bool(regex.search(x)))]
        return filtered_df
        
        #return filtered_df

    def regex_click(self, value):

        hold_df = self.filter_df_with_regex(value)
        self.current_df2 = hold_df

        #print(self.current_df2)
        self.tree2, self.scrollbar2 = self.populate_treeview(self.current_df2, 0, 2, self.second_frame, self.general_column)
        self.tree2.grid(columnspan=3)
        self.scrollbar2.grid(column=5)
      
        try:
            first_entry = self.current_df2.iloc[0]['Original_Word']
       
            self.summary_box(first_entry)
        except:
            print("empty")
        
        self.fill_in_regex()

    def search1(self):
        print("Search button clicked")
        v1 = self.dropdown1.get()
        v2 = self.dropdown2.get()
        v3 = self.search_box.get()
        print("D1:", v1, "D2:", v2, "SB:", v3)


        
        
    def run(self):
        print("run button clicked")
        

    def save(self):
        print("save button clicked")


    def reset(self):
        self.dropdown1.current(0)

        self.search_box.delete(0, tk.END)
        self.name_box.delete(0, tk.END)
        self.regex_box.delete(0, tk.END)
        self.altered_regex_box.delete(0, tk.END)

        self.tree2, self.scrollbar2 = self.populate_treeview(self.df2, 0, 2, self.second_frame, self.general_column )
        self.tree2.bind('<ButtonRelease-1>', self.on_double_click_table_2)
        self.tree2.grid(columnspan=3)
        self.scrollbar2.grid(column=5)
        
        #Useless
        self.tree3a, self.scrollbar3a = self.populate_treeview(self.df3a, 1, 0, self.second_frame, self.general_column)
        self.tree3b, self.scrollbar3b = self.populate_treeview(self.df3b, 2, 0, self.second_frame, self.general_column)
        self.tree3a.bind('<ButtonRelease-1>', self.on_double_click_table_3a)
        self.tree3b.bind('<ButtonRelease-1>', self.on_double_click_table_3b)

        #Modifier
        self.tree4a, self.scrollbar4a = self.populate_treeview(self.df4a, 1, 2, self.second_frame, self.general_column )
        self.tree4b, self.scrollbar4b = self.populate_treeview(self.df4b, 2, 2, self.second_frame, self.general_column )
        self.tree4a.bind('<ButtonRelease-1>', self.on_double_click_table_4a)
        self.tree4b.bind('<ButtonRelease-1>', self.on_double_click_table_4b)
                
        #Pattern
        self.tree5a, self.scrollbar5a = self.populate_treeview(self.df5a, 1, 4, self.second_frame,self.general_column )
        self.tree5b, self.scrollbar5b = self.populate_treeview(self.df5b, 2, 4, self.second_frame,self.general_column )
        self.tree5a.bind('<ButtonRelease-1>', self.on_double_click_table_5a)
        self.tree5b.bind('<ButtonRelease-1>', self.on_double_click_table_5b)
        print("reset button clicked")

    def revert(self):
        print("revert button clicked")
    

    def filter_id(self, word_df, filter_id):
        # Filter the DataFrame based on whether the original word contains the filter word
        filtered_df = word_df[word_df['ID'] == int(filter_id)].copy()
        return filtered_df
    
    def json_to_dataframe(self,json_filename):
        # Read the JSON file into a DataFrame
        df = pd.read_json(json_filename)
        return df

    def populate_treeview(self, df, place_row, place_column, frame, parent_width):
        tree = ttk.Treeview(frame, columns=list(df.columns), show="headings")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        for i in tree.get_children():
                tree.delete(i)
        column_width = int(parent_width / len(df.columns))
        
        for col in df:
            tree.heading(col, text=col)
     
        for index, row in df.iterrows():
            tree.insert('', 'end', values=list(row))
        
        count =1 
        for col in df.columns:
            column = "# " + str(count)
            tree.column(column, width=column_width)
            count = count + 1

        tree.configure(yscrollcommand=scrollbar.set)
        #grid
        tree.grid(row=place_row, column=place_column, sticky='nsew', padx=0)
        scrollbar.grid(row=place_row, column=place_column+1, sticky='nsw', padx=0)
        return tree, scrollbar

    












    

        
        



