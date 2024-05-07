import csv
import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog
from tkinter import ttk
import tkinter.scrolledtext as st 

import pandas as pd

from file_processing import word_counter_in_json

import sys
sys.path.insert(1, 'G:\Code\Recipe Project\Stage_3_Database and Cleaning\Table_Organizer\Ingredient_processing')  # Replace '/path/to/directory' with the actual directory path


from  process_ingredient import raw_translated_ingredient

 

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
        

        self.second_frame = Frame(self)
        self.second_frame.grid(row=0, column=0, sticky='nsew')


        self.second_frame.rowconfigure([0,1], minsize=self.general_row, weight=1)

        
        self.second_frame.columnconfigure(0, minsize=self.general_column , weight=1)
        self.second_frame.columnconfigure(2, minsize=self.general_column , weight=1)
        self.second_frame.columnconfigure(4, minsize=self.general_column , weight=1)
        self.second_frame.columnconfigure(6, minsize=self.general_column , weight=1)

        patterns_filename = "G:\Code\Recipe Project\Stage_3_Database and Cleaning\Table_Organizer\\regex_holder\\"
        self.df, self.df2 = word_counter_in_json(file_path, "ingredients_translated")
        #df2 = df
        self.df3 = self.json_to_dataframe(patterns_filename + "useless.json")
        self.df4 = self.json_to_dataframe(patterns_filename + "modifier_patterns.json")
        self.df5 = self.json_to_dataframe(patterns_filename + "measurement_patterns.json")
        self.df5 = self.df5.sort_values(by='name')


        #Tree 1 left top corner frequency of words
        self.tree1, self.scrollbar1 = self.populate_treeview(self.df, 0, 0, self.second_frame, self.general_column )
        self.tree1.bind('<Double-1>', self.on_double_click_table_1)
        self.tree1.column("# 1", width=40, stretch=False) #anchor=CENTER
        
        #Tree 2 middle top 
        #The difference between edited and non edited
        self.tree2, self.scrollbar2 = self.populate_treeview(self.df2, 0, 2, self.second_frame, self.general_column )
        self.tree2.bind('<Double-1>', self.on_double_click_table_2)

        #Tree 3 - 5 bottom left start
        #The regex files
        self.tree3, self.scrollbar3 = self.populate_treeview(self.df3, 1, 0, self.second_frame, self.general_column )
        self.tree3.bind('<Double-1>', self.on_double_click_table_3)

        self.tree4, self.scrollbar4 = self.populate_treeview(self.df4, 1, 2, self.second_frame, self.general_column )
        self.tree4.bind('<Double-1>', self.on_double_click_table_4)
        self.tree4.column("# 1",width=120, stretch=False)

        self.tree5, self.scrollbar5 = self.populate_treeview(self.df5, 1, 4, self.second_frame,self.general_column )
        self.tree5.bind('<Double-1>', self.on_double_click_table_5)
        self.tree5.column("# 1", width=80, stretch=False)

    
        # Bind double-click event to cells
        font_size = 10
        self.text_box = tk.Text(self.second_frame, wrap="word", font=("Arial", font_size), width=int(self.general_column /(font_size)))
        self.scrollbar6 = ttk.Scrollbar(self.second_frame, orient="vertical", command=self.text_box.yview)
        self.text_box.grid(row=1, column=6, sticky='nsew')
        self.scrollbar6.grid(row=1, column=7, sticky='nsw')
        self.text_box.config(yscrollcommand=self.scrollbar6.set)
        self.third_frame_a_setup()
        self.third_frame_search()

    def third_frame_a_setup (self):
        #main text processor
        
        self.third_frame = tk.Frame(self.second_frame)
        self.third_frame.grid(row=0, column=4, columnspan=2, sticky='nsew')


        self.third_frame_sub_row = int((11*(self.general_row)/12)/6)
        self.third_frame.rowconfigure(0, minsize=int((1*self.general_row)/12), weight=1)
        self.third_frame.rowconfigure(1, minsize=self.third_frame_sub_row, weight=1)

        #Basic Buttons
        self.third_frame_choice = tk.Frame(self.third_frame)
        self.third_frame_choice.grid(row=0, column=0, sticky='nsew')
        self.third_frame_choice.columnconfigure([0,1], minsize=self.general_column /2, weight=1)

        font_size = 9
        button_width = int(((self.general_column /2)/font_size))
        button_height = 5

        self.search_button = tk.Button(self.third_frame_choice, width=button_width, font=("Arial", font_size), text="Search",  height=button_height, command=self.save)
        self.search_button.grid(row=0, column=0, sticky='new')
        self.development_button = tk.Button(self.third_frame_choice, width=button_width,font=("Arial", font_size), text="Development",  height=button_height, command=self.save)
        self.development_button.grid(row=0, column=1, sticky='new')

    def third_frame_build(self):
        #Drop box 1, 0 
        self.third_frame_build_frame = tk.Frame(self.third_frame)
        self.third_frame_build_frame.grid(row=1, column=0, sticky='new')

        

    def third_frame_search(self):
        #Drop box 1, 0 
        self.third_frame_search_frame = tk.Frame(self.third_frame)
        self.third_frame_search_frame.grid(row=1, column=0, sticky='new')
        self.third_frame_search_frame.rowconfigure([0,1,2], minsize=int(self.third_frame_sub_row/3), weight=1)                               
       

        self.third_frame_drop_box = tk.Frame(self.third_frame_search_frame)
        self.third_frame_drop_box.grid(row=0, column=0, sticky='new')
        
        self.third_frame_drop_box.columnconfigure(0, minsize=int((1*self.general_column )/3), weight=1)
        self.third_frame_drop_box.columnconfigure(1, minsize=int((2*self.general_column )/3), weight=1)
   

        # Create dropdown menus
        self.label1 = tk.Label(self.third_frame_drop_box, text="Search in:", font=("Arial", 20))
        self.label1.grid(row=0, column=0, sticky="w", padx=0, pady=5)

        self.label2 = tk.Label(self.third_frame_drop_box, text="Search for:", font=("Arial", 20))
        self.label2.grid(row=1, column=0, sticky="w", padx=0, pady=5)

        self.columns_drop_down = ["word count", "Comparison 1", "Junk Word", "Modifiers", "Measurements"]
        self.dropdown1 = ttk.Combobox(self.third_frame_drop_box,  font=("Arial", 14), values=self.columns_drop_down)
        self.dropdown1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.dropdown1.bind("<<ComboboxSelected>>", self.update_dropdown2)

        self.dropdown2 = ttk.Combobox(self.third_frame_drop_box,  font=("Arial", 14))
        self.dropdown2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Create search box
        self.search_box = tk.Entry(self.third_frame_search_frame, font=("Arial", 15))
        self.search_box.grid(row=1, column=0, padx=5, pady=5, sticky="new")

   
        # Create buttons 3, 0
        self.third_frame_end_buttons = tk.Frame(self.third_frame_search_frame)
        self.third_frame_end_buttons.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.third_frame_end_buttons.columnconfigure([0,1], minsize=int(self.general_column /2), weight=1)

        self.search_button = tk.Button(self.third_frame_end_buttons, text="Search", font=("Arial", 15), command=self.search)
        self.search_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.clear_button = tk.Button(self.third_frame_end_buttons, text="Clear",  font=("Arial", 15), command=self.clear)
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

    def search(self):
        print("Search button clicked")

    def save(self):
        print("Save button clicked")

    def clear(self):
        print("Clear button clicked")

    def test(self):
        print("Test button clicked")

    def delete(self):
        print("Delete button clicked")
        

    def filter_word(self, word_df, filter_word):
        # Filter the DataFrame based on whether the original word contains the filter word
        filtered_df = word_df[word_df['Original_Word'].str.contains(filter_word)].copy()
        filtered_df = word_df[word_df['Original_Word'].str.contains(filter_word, case=False) | word_df['Processed_Word'].str.contains(filter_word, case=False)].copy()

        return filtered_df
    
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

    def on_double_click_table_1(self, event):
        item = self.tree1.selection()[0]
        column = self.tree1.identify_column(event.x)
        region = self.tree1.identify("region", event.x, event.y)
        print("region", region)
        print("column", column)

        if column != "#2":
            value = self.tree1.item(item, 'values')[int(column[1:]) - 1]  # Adjust column index
            print(f"Clicked cell value: {value}")
            if value.isnumeric() == False:
                df = self.filter_word(self.df2, value)
                self.populate_treeview(df, self.tree2_3)
            else:
                print("here")
                df = self.filter_id(self.df2, value)
                self.populate_treeview(df, self.tree2_3)
            

        
        #self.filter_word(self.df, filter_word)
        

    def on_double_click_table_2(self, event):
        item = self.tree2.selection()[0]
        column = self.tree2.identify_column(event.x)
        if column == "#2":
            self.text_box.delete('1.0', tk.END)
            value = self.tree2.item(item, 'values')[int(column[1:]) - 1]  # Adjust column index
            item_break_down = raw_translated_ingredient(value, False)
            print(str(item_break_down))
            for x in item_break_down:
                print(x)
                fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = x
                text = "raw:    " + value +  ",\nmodifiers: " + str(fmo) + ",\nmeasurements: " + str(fme) + ",\ntext: " + str(text) + ",\nhash: " + str(mod_hash) + ",\nname: "+ str(name)+ ",\nportion: "+ str(portion) + ",\nmulti_part_ingredient_status: " + str(mpis) + ",\nignore this: " + str(ignore_this) + "\n\n"
                print("text", text)
                self.text_box.insert(tk.END, text)
            #fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = item_break_down[0]
            print(f"Clicked cell value: {value}")

    def on_double_click_table_3(self, event):
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        value = self.tree.item(item, 'values')[int(column[1:]) - 1]  # Adjust column index
        print(f"Clicked cell value: {value}")

    def on_double_click_table_4(self, event):
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        value = self.tree.item(item, 'values')[int(column[1:]) - 1]  # Adjust column index
        print(f"Clicked cell value: {value}")

    def on_double_click_table_5(self, event):
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        value = self.tree.item(item, 'values')[int(column[1:]) - 1]  # Adjust column index
        print(f"Clicked cell value: {value}")

        












    

        
        



