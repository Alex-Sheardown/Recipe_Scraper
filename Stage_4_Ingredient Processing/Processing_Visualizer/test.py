import tkinter as tk
from tkinter import ttk
import json

class RegexApp(tk.Tk):
    def __init__(self, regex_data):
        super().__init__()
        self.title("Regex Pattern Viewer")
        self.geometry("800x600")

        self.regex_data = regex_data

        self.create_widgets()

    def create_widgets(self):
        # Create a Treeview to display regex patterns
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("Pattern", "Filter Reaction")
        self.tree.heading("#0", text="Index")
        self.tree.heading("Pattern", text="pattern")
        self.tree.heading("Filter Reaction", text="name")

        # Insert regex patterns into the Treeview
        for index, pattern_data in enumerate(self.regex_data):
            pattern = pattern_data["pattern"]
            filter_reaction = pattern_data["name"]
            self.tree.insert("", "end", text=index+1, values=(pattern, filter_reaction))

        self.tree.pack(expand=True, fill=tk.BOTH)

        # Add a filter button
        filter_button = tk.Button(self, text="Apply Filter", command=self.apply_filter)
        filter_button.pack()

    def apply_filter(self):
        # Retrieve selected regex pattern
        selected_item = self.tree.selection()[0]
        pattern_index = int(self.tree.item(selected_item, "text")) - 1
        selected_pattern_data = self.regex_data[pattern_index]
        selected_pattern = selected_pattern_data["pattern"]

        # Apply filter based on selected regex pattern
        # This is a placeholder action
        print(f"Applying filter for pattern: {selected_pattern}")

if __name__ == "__main__":
    # Example JSON data
    with open("G:\\Code\\Recipe Project\\Stage_3_Database and Cleaning\\Table_Organizer\\regex_holder\\modifier_patterns.json") as json_file:
        regex_data = json.load(json_file)

    app = RegexApp(regex_data)
    app.mainloop()
