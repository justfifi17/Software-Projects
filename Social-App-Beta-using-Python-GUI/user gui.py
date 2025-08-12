from user import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from register import Register               # imports register class from register.py
from tkinter import filedialog              # imported filedialog that enable us to choose files form user computer files


class Manager:
    """class that manages and displays information inorder to interact with the user"""
    # initializing data
    def __init__(self):
        self.username_now = ""                  # contains the username of the user that is currently using the interface
        self.user_followers = ""                 # contains the followers of the user that is currently using the interface

        # Creating window using Class Tk()
        self.window = Tk()
        self.window.title('Beta App')  # Providing title to the window
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.geometry("410x650")

        # ====================== MAIN PAGE===========================

        # Log in form that displays first
        self.frame_login = ttk.Frame(self.window)
        self.title = ttk.Label(self.frame_login, text="Log in form")
        self.title.grid(row=1, column=1)

        # takes inputs from the user and validate it
        self.label_1 = ttk.Label(self.frame_login, text="Username", width=10, font=("bold", 10))
        self.label_1.grid(row=2, column=0)
        self.name_user = ttk.Entry(self.frame_login)
        self.name_user.grid(row=2, column=1)

        self.label_3 = ttk.Label(self.frame_login, text="password", width=10, font=("bold", 10))
        self.label_3.grid(row=3, column=0)
        self.pass_user = ttk.Entry(self.frame_login)
        self.pass_user.grid(row=3, column=1)
        self.pass_user.config(show='*')

        # --- empty label
        self.free = ttk.Label(self.frame_login)
        self.free.grid(row=4, column=1)

        # gives a choice to log in or sign up to the user
        self.log_in_btn = ttk.Button(self.frame_login, text="Login",
                                     command=self.authenticate)  # to authenticate function
        self.log_in_btn.grid(row=5, column=1)
        self.register_btn = ttk.Button(self.frame_login, text="Sign Up",
                                       command=Register)  # to register class in register.py
        self.register_btn.grid(row=6, column=1)

        # --- empty label
        self.free = ttk.Label(self.frame_login)
        self.free.grid(row=7, column=1)

        # gives a choice to reset the fields or exit the window, both direct to functions
        self.exit = ttk.Button(self.frame_login, text="Reset", command=self.reset)
        self.exit.grid(row=8, column=1)
        self.exit = ttk.Button(self.frame_login, text="Exit", command=self.quitWindow)
        self.exit.grid(row=9, column=1)

        # ===============================SECOND PAGE===================================
        self.frame_main = ttk.Frame(self.window)
        # exit button in the main page
        self.exit = ttk.Button(self.frame_main, text="Exit", command=self.quitWindow)

        # we created notebook to show different windows of the main page
        self.page = ttk.Notebook(self.frame_main, height=550, width=500)
        self.page.pack()
        self.exit.pack()

        # ==========================PROFILE PAGE============================
        # user first finds their profile page
        self.frame_profile = ttk.Frame(self.page)
        self.profile_content = ttk.Frame(self.frame_profile)  # all profile contents are packed here
        self.profile_content.pack()

        # ==========================NEWSFEED PAGE============================
        self.frame_posts = ttk.Frame(self.page)
        # refresh button for the user to display the newsfeed
        self.post = ttk.Button(self.frame_posts, text="Refresh", command=self.get_post)
        self.post.pack(side=TOP)

        # we created a canvas to display all the posts for the user and it's followers
        self.post_content = Canvas(self.frame_posts)
        self.post_content.pack(side=LEFT, fill=BOTH, expand=5)
        self.scrollbar = ttk.Scrollbar(self.frame_posts, orient=VERTICAL, command=self.post_content.yview)
        # we created a scroll bar to scroll down to see all the posts
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.post_content.config(yscrollcommand=self.scrollbar.set)
        self.post_content.bind('<Configure>',
                               lambda e: self.post_content.configure(scrollregion=self.post_content.bbox("all")))

        # ------- ANOTHER FRAME WITHIN POST CANVAS ------
        # we add another frame within the canvas to put all the contents
        self.post_scroll = ttk.Frame(self.post_content)
        self.post_content.create_window((0, 0), window=self.post_scroll, anchor='nw')

        # ==========================CREATE POST PAGE============================
        self.frame_create = ttk.Frame(self.page)
        self.create_content = ttk.Frame(self.frame_create)
        # the interface gives the user to upload a photo or text
        self.image = ttk.Button(self.create_content, text="Image", command=self.open_image)
        self.image.pack()
        self.text1 = ttk.Button(self.create_content, text="Text", command=self.open_text)
        self.text1.pack()
        self.create_content.pack()

        # adding all the pages to the notebook
        self.page.add(self.frame_profile, text="Profile")
        self.page.add(self.frame_posts, text="News Feed")
        self.page.add(self.frame_create, text="Create")

        # we make only one page from the first and main pages to be displayed on the screen
        for frame in (self.frame_login, self.frame_main):
            frame.grid(row=0, column=0, sticky="nsew")

        # we called the function to show the first page at the beginning
        self.show_frame(self.frame_login)
        self.window.mainloop()

    # ==========================FUNCTIONS ==============================

    # shows the frame called
    def show_frame(self, frames):
        frames.tkraise()

    # quits the whole window whenever called
    def quitWindow(self):
        self.window.destroy()

    # resets all the fields that had data when called
    def reset(self):
        self.name_user.delete(0, END)
        self.pass_user.delete(0, END)

    # authenticates the user name and password when pressed login
    def authenticate(self):
        name = self.name_user.get()
        password = self.pass_user.get()
        handle = open("User.txt", "r")
        line = handle.readlines()
        for x in line:
            y = x.split(",")
            if y[0].strip() == name and y[1].strip() == password:
                self.show_frame(self.frame_main)
                self.show_profile(y[0])  # sends the username to the function that displays the profile page
                self.show_username(y[
                                       0])  # sends the username to the function that displays the user name of the user currently using the interface
                self.show_follow(y[
                                     7])  # sends the username to the function that displays the followers of the user currently using the interface

                break  # breaks the function when the user is found

        else:  # if there is a mistake in username and password, this shows a pop up message
            messagebox.showwarning("Incorrect input", "Invalid User Try again")

    # returns all the followers of the user
    def show_follow(self, index):
        self.user_followers = index.strip()

    # returns all the username of the user
    def show_username(self, index):
        self.username_now = index

    # function that lets the user to choose an image and sends the path to file handler and post it
    def open_image(self):
        self.label_9 = ttk.Label(self.create_content)
        filepath = filedialog.askopenfilename(title="select a file")  # returns the filepath of the file selected
        imagename = PhotoImage(
            file=filepath)  # use the PhotoImage to specify the filepath of the photo to the file selected
        small_image = imagename.subsample(5, 5)  # reduces the size of the image
        self.label_9.img = small_image  # select the image to the label
        self.label_9.config(image=self.label_9.img)  # save the image in the label
        self.label_9.pack()

        def save_p():
            name = self.username_now
            content = filepath
            post = Post(name, content)
            post.submit()
            self.label_9.destroy()
            self.save.destroy()

        self.save = ttk.Button(self.create_content, text="save", command=save_p)
        self.save.pack()

    # a function that lets the user to write a text and post it
    def open_text(self):
        self.label_10 = ttk.Entry(self.create_content)
        self.label_10.pack()

        def save_t():
            text = self.label_10.get()
            if text == "":
                messagebox.showwarning("Empty field", "Please enter a post")

            else:
                name = self.username_now
                content = self.label_10.get()
                post = Post(name, content)
                post.submit()
                self.label_10.destroy()
                self.save_btn.destroy()

        self.save_btn = ttk.Button(self.create_content, text="save", command=save_t)
        self.save_btn.pack()

    # gets all the post from the following users and itself/ the user
    def get_post(self):
        self.post = Post()

        def like_p():  # function to like a pic
            btn_text.set("Liked!")

        def like_t():  # function to like a text
            btn_text1.set("Liked!")

        handle_post = open("posts.txt", "r")
        line_post = handle_post.readlines()
        r = self.user_followers.split(":")

        for c in line_post:
            post = c.split(",")
            if post[1].strip() in r:  # checks if the post's user name is in user's followers list
                if "/" in post[0]:
                    self.frame = ttk.Frame(self.post_scroll, pad=10)
                    self.frame.config(relief=SOLID)
                    self.label1 = ttk.Label(self.frame, text="Username: " + str(post[1]))
                    self.label1.grid(row=1, column=1)
                    self.label = ttk.Label(self.frame)
                    image = PhotoImage(file=post[0])
                    small_image = image.subsample(5, 5)
                    self.label.img = small_image
                    self.label.config(image=self.label.img)
                    self.label.grid(row=2, column=1)
                    btn_text = StringVar()
                    self.like_btn = ttk.Button(self.frame, textvariable=btn_text, command=like_p)
                    btn_text.set("Like")
                    self.like_btn.grid(row=3, column=1, stick='e')
                    self.frame.pack(fill=BOTH)

                else:
                    self.frame1 = ttk.Frame(self.post_scroll, pad=10)
                    self.frame1.config(relief=SOLID)
                    self.label2 = ttk.Label(self.frame1, text="Username: " + str(post[1]))
                    self.label2.grid(row=1, column=1, stick='w')
                    self.label3 = ttk.Label(self.frame1, text=post[0], width=25)
                    self.label3.grid(row=2, column=2, stick=W)
                    btn_text1 = StringVar()
                    self.like_btn1 = ttk.Button(self.frame1, textvariable=btn_text1, command=like_t)
                    btn_text1.set("Like")
                    self.like_btn1.grid(row=3, column=1, stick='e')
                    self.frame1.pack(fill=BOTH)

    # a function that displays all the relevant information in the profile page
    def show_profile(self, index):
        handle = open("User.txt", "r")
        lines = handle.readlines()
        for x in lines:
            y = x.split(",")
            if str(y[0]) == str(index):
                # displays profile pic
                self.framep = ttk.Frame(self.profile_content)
                image = PhotoImage(file=y[3])
                small_image = image.subsample(5, 5)
                self.profile_show = ttk.Label(self.framep, text="Profile Pic: ", width=10, font=("bold", 16))
                self.profile_show.pack()
                self.pro_pic = ttk.Label(self.framep, justify=LEFT)
                self.pro_pic.img = small_image
                self.pro_pic.config(image=self.pro_pic.img)
                self.pro_pic.pack()
                self.framep.pack()

                # displays username
                self.frame1 = ttk.Frame(self.profile_content)
                self.username_text = ttk.Label(self.frame1, text="Username: ", width=10, font=("bold", 16))
                self.username_text.grid(row=1, column=1)
                self.username = ttk.Label(self.frame1, text=y[0], width=10, font=("bold", 16))
                self.username.grid(row=1, column=2)
                self.frame1.pack()

                # displays name
                self.frame2 = ttk.Frame(self.profile_content)
                self.name_text = ttk.Label(self.frame2, text="Name: ", width=10, font=("bold", 16))
                self.name_text.grid(row=2, column=1)
                self.name_print = ttk.Label(self.frame2, text=y[2], width=10, font=("bold", 16))
                self.name_print.grid(row=2, column=2)
                self.frame2.pack()

                # displays bio
                self.frame3 = ttk.Frame(self.profile_content)
                self.bio_text = ttk.Label(self.frame3, text="Bio: ", width=10, font=("bold", 16))
                self.bio_text.grid(row=3, column=1)
                self.bio_print = ttk.Label(self.frame3, text=y[4], width=10, font=("bold", 16))
                self.bio_print.grid(row=3, column=2)
                self.frame3.pack()

                # displays birthdate
                self.frame4 = ttk.Frame(self.profile_content)
                self.bd_text = ttk.Label(self.frame4, text="Birth date: ", width=10, font=("bold", 16))
                self.bd_text.grid(row=4, column=1)
                self.bd_print = ttk.Label(self.frame4, text=y[5], width=10, font=("bold", 16))
                self.bd_print.grid(row=4, column=2)
                self.frame4.pack()

                # displays location
                self.frame5 = ttk.Frame(self.profile_content)
                self.loc_text = ttk.Label(self.frame5, text="Location: ", width=10, font=("bold", 16))
                self.loc_text.grid(row=5, column=1)
                self.loc_print = ttk.Label(self.frame5, text=y[6], width=10, font=("bold", 16))
                self.loc_print.grid(row=5, column=2)
                self.frame5.pack()


main = Manager()
