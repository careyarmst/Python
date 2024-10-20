# Program Title: Create person class & customer subclass and display/print the results
# Author: Carey Armstrong IDE: Pycharm Professional Edition
# Date: 2024-10-08
# Version: 1.0
# Purpose: This program is designed to demonstrate the creation of a Python class and extend it with a subclass
# Pseudocode: (1) Set up Person class with defined attributes for name, address & telephone number
# (2) Set up a Customer subclass under person that extends that class to include a customer number and indicate
# (3) whether or not it is OK to mail the customer
# (4) Print out the person and customer data using lists & for loops (simple program)

# Initialize Person class, attributes are name, address, telephone number
class Book:
    def __init__(self, title, author_name, publisher_name):
        self.title = title
        self.author_name = author_name
        self.publisher_name = publisher_name

    def get_title(self):
        return self.__title

    def get_author_name(self):
        return self.__author_name

    def get_publisher_name(self):
        return self.__publisher_name


    def set_title(self, title):
        self.__title = title

    def set_author_name(self, author_name):
        self.__author_name = author_name

    def set_publisher_name(self, publisher_name):
        self.__publisher_name = publisher_name


    def __str__(self):
        return f" This is what this is doing at the moment: {self.title}, {self.author_name}, {self.publisher_name}"

goingon = Book("Geraldine", "Bob Smith", "Scribner's")
print(goingon)