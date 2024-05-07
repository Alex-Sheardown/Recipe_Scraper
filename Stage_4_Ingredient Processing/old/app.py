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
        #self.fullscreen_state = True

        self.second_frame = Frame(self)
        self.second_frame.grid(row=0, column=0, sticky='nsew')
        
       
        self.second_frame.grid(row=0, column=0, sticky='nsew')
        self.second_frame.rowconfigure([0,1], minsize=(height-40)/2, weight=1)

    
        general_row = ((width-35)/6)
        self.second_frame.columnconfigure(0, minsize=general_row, weight=1)
        self.second_frame.columnconfigure(2, minsize=general_row, weight=1)
        self.second_frame.columnconfigure(4, minsize=general_row, weight=1)
        self.second_frame.columnconfigure(6, minsize=general_row*3, weight=1)


        self.df, self.df2 = word_counter_in_json(file_path, "ingredients_translated")
        #df2 = df
        self.df3 = self.df
        self.df4 = self.df

        #Tree 1 left top corner frequency of words
        self.tree1 = ttk.Treeview(self.second_frame, columns=list(self.df.columns), show="headings")
        self.scrollbar1 = ttk.Scrollbar(self.second_frame, orient="vertical", command=self.tree1.yview)
        self.populate_treeview(self, self.df, self.tree1, self.scrollbar1, 0, 0)
        self.tree1.bind('<Double-1>', self.on_double_click_table_1)
        # Add scrollbar
        
       
        # Bind double-click event to cells
        


        #Tree 2-3 middle top 
        #The difference between edited and non edited
        self.tree2_3 = ttk.Treeview(self.second_frame, columns=list(self.df2.columns), show="headings")
        self.scrollbar2 = ttk.Scrollbar(self.second_frame, orient="vertical", command=self.tree2_3.yview)
        self.populate_treeview(self, self.df2, self.tree2, self.scrollbar1, 0, 2)
        self.tree2_3.bind('<Double-1>', self.on_double_click_table_2_3)


        #Tree 4 left bottom
        """
        self.tree4 = ttk.Treeview(self.second_frame, columns=list(self.df3.columns), show="headings")
     
        self.populate_treeview(self.df3,self.tree4)
        # Add scrollbar
        self.scrollbar4 = ttk.Scrollbar(self.second_frame, orient="vertical", command=self.tree4.yview)
        self.tree4.configure(yscrollcommand=self.scrollbar4.set)
        #grid
        self.tree4.grid(row=1, column=0, sticky='nsew', padx=0)
        """
        self.text_box = tk.Text(self.second_frame, wrap=tk.WORD)
        #self.text_box.insert(tk.END, "data")
        self.text_box.grid(row=1, column=0, sticky='nsew', padx=0)
        self.scrollbar4 = ttk.Scrollbar(self.second_frame, orient="vertical", command=self.text_box.yview)
        self.scrollbar4.grid(row=1, column=1, sticky='nsw', padx=0)
        #Bind
        self.text_box.config(yscrollcommand=self.scrollbar4.set)

        #Frame for under table 2-3 
        self.sub_frame = tk.Frame(self.second_frame )
        self.sub_frame.grid(row=1, column=2, columnspan= 3, sticky='nsew' )

        self.sub_frame.rowconfigure(0, minsize=(height-40)/2, weight=1)
        self.sub_frame.columnconfigure([0,2],  minsize=((width-35)/3), weight=1)

        #Tree 5 left middle
        self.tree5 = ttk.Treeview(self.sub_frame, columns=list(self.df4.columns), show="headings")

        self.populate_treeview(self.df,self.tree5)
        # Add scrollbar
        self.scrollbar5 = ttk.Scrollbar(self.sub_frame, orient="vertical", command=self.tree5.yview)
        self.tree5.configure(yscrollcommand=self.scrollbar5.set)
        #grid
        self.tree5.grid(row=0, column=0, sticky='nsew', padx=0, rowspan= 2)
        self.scrollbar5.grid(row=0, column=1, sticky='nsw', padx=0, rowspan= 2)
        #Bind
        self.tree5.bind('<Double-1>', self.on_double_click_table_5)

        #Bottom right hand coner 6
        self.third_frame = tk.Frame(self.sub_frame)
        self.third_frame.grid(row=0, column=2, sticky='nsw')
        
        self.third_frame.rowconfigure([0,1], minsize=(1*(height-40)/6)/6, weight=1)
        self.third_frame.rowconfigure(2, minsize=(4*(height-40)/6)/6, weight=1)


        #self.third_frame.rowconfigure(2, minsize=((height-40)/4)-1000, weight=1)
        self.third_frame.columnconfigure(0,   minsize=(1*(((width-35)/3)/2)/6), weight=1)
        self.third_frame.columnconfigure(1,   minsize=(5*(((width-35)/3)/2)/6), weight=1)
        


        self.label1 = tk.Label(self.third_frame, text="name:", font=("Arial", 14))
        self.label1.grid(row=0, column=0, sticky='nw', padx= 10,pady= 10)

        self.textbox1 = tk.Text(self.third_frame , width=45, height=1, font=("Arial", 14))
        self.textbox1.grid(row=0, column=1, sticky='nsw',pady= 10)

        self.label2 = tk.Label(self.third_frame , text="regex:", font=("Arial", 14))
        self.label2.grid(row=1, column=0, sticky='nw', padx= 10)

        self.textbox2 = tk.Text(self.third_frame , width=45, height=1, font=("Arial", 14))
        self.textbox2.grid(row=1, column=1, sticky='nsw')

        # Create a frame for buttons
        self.button_frame = tk.Frame(self.third_frame )
        self.button_frame.grid(row=2, column=0, columnspan=2, rowspan=2, padx=5, pady=5, sticky='nsew')

        # Define button width
        button_width = 40
        button_height = 5
        font_size = 9

        self.save_button = tk.Button(self.button_frame, text="Save", width=button_width, height=button_height, command=self.save, font=("Arial", font_size))
        self.save_button.grid(row=0, column=0, sticky='nsew')

        self.clear_button = tk.Button(self.button_frame, text="Clear", width=button_width,height=button_height, command=self.clear, font=("Arial", font_size))
        self.clear_button.grid(row=0, column=1, sticky='nsew')

        self.test_button = tk.Button(self.button_frame, text="Test", width=button_width, height=button_height,command=self.test, font=("Arial", font_size))
        self.test_button.grid(row=1, column=0, sticky='nsew')

        self.delete_button = tk.Button(self.button_frame, text="Delete", width=button_width,height=button_height, command=self.delete, font=("Arial", font_size))
        self.delete_button.grid(row=1, column=1, sticky='nsew')

     
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

    def populate_treeview(self, df, tree, scrollbar, place_row, place_column):
        for i in tree.get_children():
                tree.delete(i)
        for col in df:
            tree.heading(col, text=col)
        for index, row in df.iterrows():
            tree.insert('', 'end', values=list(row))

        tree.configure(yscrollcommand=self.scrollbar.set)
        #grid
        tree.grid(row=place_row, column=place_column, sticky='nsew', padx=0)
        scrollbar.grid(row=place_row, column=place_column+1, sticky='nsw', padx=0)

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
        

    def on_double_click_table_2_3(self, event):
        item = self.tree2_3.selection()[0]
        column = self.tree2_3.identify_column(event.x)
        if column == "#2":
            self.text_box.delete('1.0', tk.END)
            value = self.tree2_3.item(item, 'values')[int(column[1:]) - 1]  # Adjust column index
            item_break_down = raw_translated_ingredient(value, False)
            print(str(item_break_down))
            for x in item_break_down:
                print(x)
                fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = x
                text = "modifiers: " + str(fmo) + ",\nmeasurements: " + str(fme) + ",\ntext: " + str(text) + ",\nhash: " + str(mod_hash) + ",\nname: "+ str(name)+ ",\nportion: "+ str(portion) + ",\nmulti_part_ingredient_status: " + str(mpis) + ",\nignore this: " + str(ignore_this) + "\n\n"
                print("text", text)
                self.text_box.insert(tk.END, text)
            #fmo, fme, text, mod_hash, name, portion, mpis, ignore_this = item_break_down[0]
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

        












    

        
        



