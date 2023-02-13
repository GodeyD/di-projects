# Exercise 1 : What Are You Learning ?
def display_message():
    print('I am learning phyton')

display_message()

# 🌟 Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('Dune')


# 🌟 Exercise 3 : Some Geography
def describe_city(cty, ctry ='Argentina' ):
    print(f'{cty} is in {ctry}')

describe_city('bsas')    

# Exercise 4 : Random
import random

def rand(num):
    r = random.randint(1,100)
    if r == num : print('Success')
    else : print(f'fail! your num is {num} and the pc num is {r}')

rand(10)    

# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
def make_shirt(size, text):
    print(f'The size of the shirt is {size} and the text is {text}')