# Objective
# Today, we will extend what we learned yesterday about Inheritance to Abstract Classes. Because this is a very specific object oriented concept, submissions are limited to the few languages that use this construct. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given a Book class and a Solution class, write a MyBook class that does the following:

# Inherits from Book
# Has a parameterized constructor taking these 3 parameters:
# string title
# string author
# int price
# Implements the Book class' abstract display() method so it prints these  lines:
# Title:, a space, and then the current instance's title.
# Author:, a space, and then the current instance's author.
# Price:, a space, and then the current instance's price.
# Input Format

# You are not responsible for reading any input from stdin. The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments). It then calls the display method on the Book object.


from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",price)
        

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
