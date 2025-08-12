from user import *                          # import user.py to add users created to the the file
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry               # imported dateentry and tkcalendar that enables the user to choose dates from the calendar
from tkinter import filedialog              # imported filedialog that enable us to choose files form user computer files


class Register:
    """class that registers new users to the system"""

    def __init__(self):
        self.filepath=""
        self.new_window = Tk()          # creates new window
        self.new_window.title('Registration form')
        self.new_window.geometry('300x400')
        self.new_window.config(background="#ECECEC")

        self.frame_regis = ttk.Frame(self.new_window)
        self.label_0 = ttk.Label(self.frame_regis, text="Please Enter Your Details")
        self.label_0.grid(row=1, column=1, sticky="news")

        # inputs from the user
        # name
        self.label_1 = ttk.Label(self.frame_regis, text="Name", width=10, font=("bold", 10))
        self.label_1.grid(row=2, column=0)
        self.name_u = ttk.Entry(self.frame_regis)
        self.name_u.grid(row=2, column=1)

        # username
        self.label_3 = ttk.Label(self.frame_regis, text="User name", width=10, font=("bold", 10))
        self.label_3.grid(row=3, column=0)
        self.user_n = ttk.Entry(self.frame_regis)
        self.user_n.grid(row=3, column=1)

        # password
        self.label_4 = ttk.Label(self.frame_regis, text="Password", width=10, font=("bold", 10))
        self.label_4.grid(row=4, column=0)
        self.password_u = ttk.Entry(self.frame_regis)
        self.password_u.config(show='*')
        self.password_u.grid(row=4, column=1)

        # birthdate
        self.label_5 = ttk.Label(self.frame_regis, text="Birthdate", width=10, font=("bold", 10))
        self.label_5.grid(row=5, column=0)
        self.bdate_u = DateEntry(self.frame_regis, width=17, selectmode='day', year=2021, month=7, day=16)
        self.bdate_u.grid(row=5, column=1)

        # location
        self.label_6 = ttk.Label(self.frame_regis, text="Location", width=10, font=("bold", 10))
        self.label_6.grid(row=7, column=0)
        self.location_u = ttk.Entry(self.frame_regis)
        self.location_u.grid(row=7, column=1)

        # biography
        self.label_7 = ttk.Label(self.frame_regis, text="Biography", width=10, font=("bold", 10))
        self.label_7.grid(row=8, column=0)
        self.bio_u = ttk.Entry(self.frame_regis)
        self.bio_u.grid(row=8, column=1)

        # profile photo
        self.label_8 = ttk.Label(self.frame_regis, text="Profile Photo", width=10, font=("bold", 10))
        self.label_8.grid(row=9, column=0)
        self.photo = ttk.Button(self.frame_regis, text='Choose', command=self.openfile)
        self.photo.grid(row=9, column=1, stick='w')

        # reset button that clears all fields with data
        self.reset = ttk.Button(self.frame_regis, text="Reset", command=self.reset)
        self.reset.grid(row=11, column=1, stick='w')
        # exit button that quits from the window when triggered
        self.exit = ttk.Button(self.frame_regis, text="Exit", command=self.quitWindow)
        self.exit.grid(row=11, column=1,  stick='e')

        # ------ empty label
        self.free = ttk.Label(self.frame_regis)
        self.free.grid(row=12, column=1)

        # submits all the inputs from the user to text file
        b0 = ttk.Button(self.frame_regis, text='Submit', width=10, command=self.signup)
        b0.grid(row=13, column=1)

        self.frame_regis.pack()
        self.new_window.mainloop()
    # =====================FUNCTIONS======================================
    # reset function that clears all the fields that has data input from the user
    def reset(self):
        self.user_n.delete(0,END)
        self.name_u.delete(0,END)
        self.password_u.delete(0,END)
        self.bdate_u.delete(0,END)
        self.location_u.delete(0,END)
        self.bio_u.delete(0,END)

    # a function that quits the window and exit the program
    def quitWindow(self):
        self.new_window.destroy()

    # a function that let the user to choose a png file form their computer
    def openfile(self):
        filepath = filedialog.askopenfilename(title="select a file")
        self.filepath= filepath         # we globalize the variable to use it in another function

    # a function that stores all the inputs from the user to a text file
    def signup(self):
        try:
            username = self.user_n.get()
            name = self.name_u.get()
            password = self.password_u.get()
            birth = self.bdate_u.get()
            location = self.location_u.get()
            biog = self.bio_u.get()
            photo = self.filepath

            # checking empty fields
            if username == "" or name == "" or password == "":
                raise AssertionError

            # check repetitive usernames
            handle = open("User.txt", "r")
            line = handle.readlines()
            for x in line:
                y = x.split(",")
                if y[0] == username:
                    raise ValueError

            user = User(username, name, password, birth, location, biog, photo)
            user.submit()
            self.new_window.destroy()

        except ValueError:
            messagebox.showwarning("User name taken", "This username is taken")

        except AssertionError:
            messagebox.showwarning("Empty fields", "User name, name and password are mandatory")

        # except:
        #     messagebox.showwarning("Empty field", "Profile not selected")


