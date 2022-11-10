#!/usr/bin/env python
# coding: utf-8

# In[2]:



# Import a library
import random

# creating python __all__ variable
__all__ = ['__MODEL__', '__CARS__', 'Car', 'random_car', 'random','get_random_name']

# Define constants
__MODEL__ = (2014, 2016, 2018, 2020, 2022)
__CARS__ = ("BMW", "Toyota")


# Define a custom class
class Car:

    #init method
    def __init__(self, model: str, name: str):
        self.model = model
        self.name = name
        
    def __str__(self):
        return f"Name: {self.name},  Model:  {self.model}"
    
    
# Define a custom function
def get_random_name():
    
    # returning random names and colors
    return Car(random.choice(__MODEL__), random.choice(__CARS__))

# Create a random object
random_car = get_random_name()


# In[ ]:




