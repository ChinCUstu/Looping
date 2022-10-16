#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Hello")
num_char = len("Hello")
print(num_char)


# In[ ]:


def my_function():
    print("Hello")
    print("Bye")


# In[ ]:


def my_function():
    print("Hello")
    print("Bye")

my_function()


# ### Defining Functions

# In[ ]:


def my_function():
#     Do this
#     Then do this
#     Finally do this


# In[ ]:


Calling Functions
# my_function()


# ### Challenge: REEGBOX

# In[ ]:


def turn_right:
    turn_left()
    turn_left()
    turn_left()

#Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()


# ### Reeborg's Hurdle Loop

# In[ ]:


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

jump()
jump()
jump()
jump()
jump()
jump()


# Using for loops

# In[ ]:


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()

