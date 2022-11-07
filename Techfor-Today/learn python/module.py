#!/usr/bin/env python
# coding: utf-8

# In[2]:



# Import a library
import random

__all__ = ['__COLORS__', '__NAMES__', 'Person', 'random_person', 'random','__get_random_name__']

# Define constants
__COLORS__ = ("red", "blue", "yellow", "green")
__NAMES__ = ("jake", "alam", "DK")


# Define a custom class
class Person:

    #init method
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        
    def __str__(self):
        return f"Name: {self.name},  Fav color is:  {self.color}"
    
    
# Define a custom function
def __get_random_name__():
    
    # returning random names and colors
    return Person(random.choice(__COLORS__), random.choice(__NAMES__))

# Create a random object
random_person = get_random_name()


# In[ ]:




