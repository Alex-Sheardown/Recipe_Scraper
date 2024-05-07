import os
import app

def create_directory_structure():

    main_dir = "data"
    # Create main directory
    if not os.path.exists(main_dir):
        os.makedirs(main_dir)

if __name__ == "__main__":
    create_directory_structure()
    #app.WelcomeWindow().mainloop()
    app.welcome_window = app.WelcomeWindow()
    app.welcome_window.mainloop()

    #38percent 11:25 the 17th
    #from 58 at 9:10 pm same day 72 hours prediction
