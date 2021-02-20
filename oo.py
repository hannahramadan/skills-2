"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

- Encapsulation: enclosing related data, functions, and variables into a single space.
The space we're learning about is called a Class. 

- Abstraction: hiding uncessary information or providing only necessary details 
to your user. We don't need to know all the details of how a method words to use it. 

- Polymorphism: the same data types (from the same class) can have many 
different behaviors. We can redefine attributes and methods to fit instances of 
one class. 
-------------------------------------
2. What is a class?

A Class is a custom data type. We can give these custom data types their own functions
(methods).
-------------------------------------
3. What is a method?

A method is a function that inside a class. It makes it so that you can 
reuse this function on other instances of your class. 
-------------------------------------
4. What is an instance in object orientation?

An instance is an occurance of a class.
-------------------------------------
5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute that you want all instances of that class to have, 
   while an instance attribute is an attribute only that particualr instance gets. 

   For example, a if you had a class that contained food, a class attribute might be "is edible".
   An instance of the class Food might be fruit, which might have an attribute "contains seeds".


"""


"""2. Road Class"""

class Road:
    num_lanes = 2
    speed_limit = 25

road_1 = Road
road_1.num_lanes = 4
road_1.speed_limit = 60

road_2 = Road

"""3. Update Password"""

class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password
    
    def update_password(self, current_password, new_password):

        i = True
        j = True 

        while i == True:
            username_1 = input("What is your username?: ")
            if username_1 != self.username:
                print("Username not recognzied.")
            else:
                i = False
                while j == True:
                    self.current_password = input("What is your current password?: ") 
                    if self.current_password == self.password:
                        self.new_password = input("Please enter your new password: ") 
                        self.password = self.new_password
                        print("Password updated")
                        j = False
                    else:
                        print("Invalid password")


# """4. Build a Library"""


# class Book(object):
#     """A Book object."""

#     def __init__(self, title, author):
#         """Create a book with the given title and author."""

#         self.title = title
#         self.author = author

# class Library:

    # def __init__(self, book):

    #     self.book = []

    # def create_and_add_book(self, title, author):

    # def find_books_by_author(self, author):
    #     return(books)

# We have given you a class, Book. You’ll use it build a new Library class. 
# Your Library class needs to meet these specifications:

# Each Library object needs an instance attribute called books which 
# starts off as an empty list

# We also need two methods:

# create_and_add_book, which takes in the title and author of a book (as strings). 
# It should instantiate a Book object and add it to the Library’s books list

# find_books_by_author, which takes in an author’s name (as a string) and 
# returns a list of all books by that author

# """5. Rectangle"""


# class Rectangle:
#     """A rectangle."""

#     def __init__(self, length, width):
#         """Create a rectangle with the given length and width."""

#         self.length = float(length)
#         self.width = float(width)

#     def calculate_area(self):
#         """Return the area of the rectangle."""

#         return self.length * self.width
