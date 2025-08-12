from datetime import *  # import module datetime to manipulate date and time


class User:
    """class user that is an account, has profile information and followers information"""

    def __init__(self, user="", name="", pas="", bd=datetime, loc="", bio="", photo=""):  # constructor
        self.__userName = user  # attribute representing user name of a user
        self.__birthdate = bd  # attribute representing birthdate of a user
        self.__location = loc  # attribute representing location of a user
        self.__biography = bio  # attribute representing bio of a user
        self.__name = name  # attribute representing full name of a user
        self.__password = pas  # attribute representing password of a user
        self.__profile_photo = photo  # attribute representing a profile pic of a user
        self.__followers = [self.__userName]  # by default every user follows himself/herself
        self.__posts = []  # a list that will collect posts

    def set_username(self, name1):  # setter of name
        self.__userName = name1

    def get_username(self):  # getter of name
        return self.__userName

    def set_birthdate(self, birth):  # setter of birthdate
        self.__birthdate = datetime.strptime(birth, '%d/%m/%Y')  # method to represent time according to format

    def get_birthdate(self):  # getter of birthdate
        return self.__birthdate

    def set_location(self, loc):  # setter of location
        self.__location = loc

    def get_location(self):  # getter of location
        return self.__location

    def set_follower(self, other):  # setter of a followers
        self.__followers.append(other.get_name())

    def get_follower(self):  # getter of followers
        return ":".join(self.__followers)

    def set_biography(self, bio):  # setter of bio
        self.__biography = bio

    def get_biography(self):  # getter of bio
        return self.__biography

    def set_name(self, name1):  # setter of name
        self.__name = name1

    def get_name(self):  # getter of name
        return self.__name

    def set_password(self, pass1):  # setter of password
        self.__password = pass1

    def get_password(self):  # getter of password
        return self.__password

    def set_profile(self, photo):  # setter of profile
        self.__profile_photo = photo

    def get_profile(self):  # getter of profile
        return self.__profile_photo

    def add_post(self):  # function that adds posts to list self.post(composition)
        Post1 = Post()  # object of class Post
        Post1.set_name()  # setting attributes here
        Post1.set_content()  # setting attributes here
        self.__posts.append(Post1)  # appending post to the list

    def display_post(self):  # function to display posts in the list
        for post in self.__posts:  # post in self post list
            print(post)  # display each post

    def submit(self):  # submit button (when clicked will open file and append information)
        handle = open("User.txt", "a")  # open file user.txt
        handle.write("{},{},{},{},{},{},{},{} \n".format(self.get_username(), self.get_password(), self.get_name(),
                                                         self.get_profile(),
                                                         self.get_biography(), self.get_birthdate(),
                                                         self.get_location(),
                                                         self.get_follower()))  # write in the file handle those user informations


class Individual(User):
    """class that inherits from user representing a user that does not post"""

    def __init__(self):  # constructor
        User.__init__(self)  # Parent constructor
        self.marital_status = ("Married", "Single")  # status of individual
        self.marital_default = 0  # default statues will be single

    def set_marital_status(self):  # setter
        self.marital_default = 0

    def get_marital_status(self):  # geter
        return self.marital_status[self.marital_default]

    def __str__(self):  # print when object is called
        return "Marital status:{}".format(self.get_marital_status())


class BusinessUser(User):  # child of user class
    """class that represents a business user that can post advertisements"""

    def __init__(self):  # constructor
        User.__init__(self)  # constructor of parent
        self.website_link = ""  # link of advertisers website
        self.ads = []  # composition

    def set_website_link(self, link):  # setter
        self.website_link = link

    def get_website_link(self):  # getter
        return self.website_link

    def add_ads(self):
        ADS1 = ADS()  # object of advertising class
        self.ads.append(ADS1)  # appending ads to the list

    def display_ads(self):  # object to show ads in the list
        for ad_post in self.ads:  # for ads in the list
            print(ad_post)  # print ads

    def __str__(self):  # print when object is called
        return "Website link:{}".format(self.get_website_link())


class Post:  # class post that allows user to post content with their name
    def __init__(self, name="", content=""):  # constructor
        self.name = name  # setting the name of person who is posting the content
        self.content = content  # content that is being posted
        self.content_type = ("Image", "Text")
        self.content_type_default = 0
        self.like = bool  # button to either like or not(neutral)

    def set_name(self, name=User()):  # setter name of person posting the content
        self.name = name.get_username()  # getting the user name from the user class and setting it here

    def get_name(self):  # getter of name
        return self.name

    def set_content(self, content):  # setter content
        self.content = content

    def get_content(self):  # getter content
        return self.content

    def set_content_type(self):  # setter content type
        self.content_type_default = 0

    def get_content_type(self):  # getter of content
        return self.content_type[self.content_type_default]  # by default will be Image

    def submit(self):  # function representing what will happen after submit button is clicked
        handle = open("posts.txt", "a")  # open file posts and append there
        handle.write("{},{}\n".format(self.get_content(), self.get_name()))  # write them in this format


class ADS(Post):  # class ADS child class of class post
    def __init__(self):  # constructor of class ads(child)
        Post.__init__(self)  # constructor of class post(parent)
        self.link_to_advertised_content = ""  # ads contain link that redirect you to advertised content site
        self.ad_to_be_sent = []  # list of people that the add will be sent to

    def set_link(self, link):  # setting redirecting link here
        self.link_to_advertised_content = link

    def get_link(self):  # getter of link
        return self.link_to_advertised_content

    def pay_for_ads(self):  # function that will allow user if she/he is an advertiser(to send ads to number of users)
        x = int(input(
            "press 0 for basic plan, 1 for silver plan and 2 for golden plan: "))  # asking advertiser to choose from plans
        if x == 0:  # if user chooses basic plan
            pay = int(input(
                "Press 1 and pay 10 AED, or press 0 to choose another plan"))  # pressing 1 would mean paying and ads will be sent to 5 users
            print(
                "You are preceding with a Basic plan ad will be sent to this 5 users")  # statement informing user that ads are being sent to 5 users
            if pay == 0:  # 0 is pressed if user wants to choose another plan
                self.pay_for_ads()  # function to choose from the plans
            else:  # else user will be shown list of the users that the ad has been sent to
                file = open("User.txt", "r")  # open user file and read from it
                limit = 0  # set limit to 0
                for i in file:  # for line in file
                    limit += 1  # increment limit by 1
                    new_name = i.split(",")  # split line divide sting to list
                    x = new_name[0]  # name in the users file has index 0 therefore
                    print(x)  # print name of users
                    self.ad_to_be_sent.append(i)  # send user to the list that the ads will be sent to
                    if limit == 5:  # basic plan only sends it to 5 users
                        exit()  # exit after sending it to 5 users

        elif x == 1:

            pay = int(input("Press 1 and pay 30 AED, or press 0 to choose another plan"))
            print("" * 5 + " You are preceding with a Silver plan ad will be sent to this 10 users " + "" * 5)
            if pay == 0:
                self.pay_for_ads()
            else:
                file = open("User.txt", "r")
                limit = 0  # see comments of the above one (same as above one)
                for i in file:
                    limit += 1
                    new_name = i.split(",")
                    x = new_name[0]
                    self.ad_to_be_sent.append(i)
                    print(x)
                    if limit == 10:  # limit of users in silver plan is 10
                        exit()

        elif x == 2:
            pay = int(input("Press 1 and pay 40 AED, or press 0 to choose another plan"))
            print(" You are preceding with a Basic plan your post will be sent to 15 users ")
            if pay == 0:
                self.pay_for_ads()
            else:
                file = open("User.txt", "r")
                line = file.readlines()
                limit = 0
                for i in line:
                    limit += 1  # see comments of the above one (same as above one)
                    new_name = i.split(",")
                    x = new_name[0]
                    self.ad_to_be_sent.append(i)
                    print(x)
                    if limit == 15:  # limit of users in the golden plan is 15
                        exit()

    def advertise(self):  # function that send ads to users according to plan
        for x in range(len(self.ad_to_be_sent)):  # sending ads to users in the list ad_to_be_sent
            self.get_content()  # display content of advertisers to users

    def submit(self):  # submit button that appends name, content of advertiser in posts
        handle = open("ads.txt", "a")  # appends in the file posts
        handle.write("{},{},{}\n".format(self.get_name(), self.get_content(), self.get_link()))  # write in the files
