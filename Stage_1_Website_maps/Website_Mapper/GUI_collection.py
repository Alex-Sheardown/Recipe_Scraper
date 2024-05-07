from tkinter import *
import tkinter as tk

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,master=None, **kwargs ):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()



    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def donothing():
    x = 0
    
def menuBar(root):
    
    show_Internal = tk.BooleanVar()
    show_External = tk.BooleanVar()
    show_Error  = tk.BooleanVar()

    show_Internal.set(1)

    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Pause", command=root.quit)
    filemenu.add_cascade(label="Exit", menu=filemenu)

    viewmenu = Menu(menubar, tearoff=0)
    #viewmenu.add_command(label="Feed", command=donothing)

    

    
    submenu = Menu(viewmenu, tearoff=0)
    submenu.add_checkbutton(label="Internal Links",    onvalue=0,      offvalue=1,     var=show_Internal)
    submenu.add_checkbutton(label="External Links",    onvalue=1,      offvalue=0,     variable=show_External)
    submenu.add_checkbutton(label="Error Links",       onvalue=1,      offvalue=0,     variable=show_Error)
    submenu.add_checkbutton(label="Include Reapats",       onvalue=1,      offvalue=0,     variable=show_Error)
    submenu.add_checkbutton(label="Connections",       onvalue=1,      offvalue=0,     variable=show_Error)
    #viewmenu.add_cascade(label='Feed options', menu=submenu, underline=0)
   
    viewmenu.add_cascade(
        label="Feed options",
        menu=submenu 
    )


    viewmenu.add_command(label="Statistics", command=donothing)
    viewmenu.add_command(label="General", command=donothing)
    viewmenu.add_separator()
    
    viewmenu.add_separator()
    viewmenu.add_command(label="Externa Links", command=donothing)
    viewmenu.add_command(label="Internal Links", command=donothing)
    viewmenu.add_command(label="External Links", command=donothing)
    menubar.add_cascade(label="View", menu=viewmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    show_Internal.set(True)
    root.config(menu=menubar)
    

    

def main():
    root = Tk()
    
    

    myframe = Frame(root)
    root.geometry('1000x750')

    
    myframe.pack(fill=BOTH, expand=YES)

    """
    mycanvas = ResizingCanvas(myframe,width=850, height=400, bg="LightBlue1", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    # add some widgets to the canvas
    
    mycanvas.create_line(0, 0, 200, 100)
    mycanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")

    mycanvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")

    mycanvas.create_window(100,10,fill="darkblue",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")
    """

    T = tk.Text(root, height=100, width=30)
    
    #T.place(bordermode=OUTSIDE, height=1000, width=100)
    #T.grid(row=0, column=0, padx=(100, 10))
    quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished."""
    T.insert(tk.END, quote)
    T.pack(padx=6, pady=4)

    #mycanvas.menu()
    
    menuBar(root)
    

    # tag all of the drawn widgets
    #mycanvas.addtag_all("all")

    """
    var = StringVar()
    label = Message( root, textvariable = var, relief = RAISED )

    var.set("Hey!? How are you doing?")
    """

    """
    
    """

    #label.pack()


    root.mainloop()




if __name__ == "__main__":
    main()