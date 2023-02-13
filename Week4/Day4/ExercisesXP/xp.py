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

make_shirt("Small", "I love to code")

def make_shirt(size="Small", text="I love Python"):
    print(f'The size of the shirt is {size} and the text is {text}')

make_shirt()

def make_shirt(size, text="I love Python"):
    print(f'The size of the shirt is {size} and the text is {text}')

make_shirt("Large")
make_shirt("Medium")
make_shirt("Small", "Diferent")

# 🌟 Exercise 6 : Magicians …
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for name in magician_names:
        print(name)

def make_great():
    for i, name in enumerate(magician_names):
        magician_names[i] = f'the Great {name}'

make_great()
show_magicians()

# 🌟 Exercise 7 : Temperature Advice
def get_random_temp(season):
    if season == 'winter':
        return random.randint(-10,15)
    elif season == 'autumn':
        return random.randint(16,23)
    elif season == 'spring':
        return random.randint(24,31)
    elif season == 'summer':
        return random.randint(32,40)
    



def main():
    season = input('which season? ‘summer’, ‘autumn’, ‘winter’, or ‘spring’: ')
    celsius = get_random_temp(season)
    print(f'The temperature right now is {celsius} degrees Celsius')
    if celsius < 0:
        print(f'Brrr, that’s freezing! Wear some extra layers today')
    elif celsius < 16:
        print(f'Quite chilly! Don’t forget your coat')
    elif celsius < 24:
        print(f'Felts nice')
    elif celsius < 32:
        print('Its hot drink water')
    else: print('Is to hot dont go where is sunny')

main()