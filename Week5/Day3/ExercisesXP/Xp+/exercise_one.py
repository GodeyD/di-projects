# 🌟 Exercise 1: Import
# from func import sum_two_numbers
# sum_two_numbers(1, 2)

# 🌟 Exercise 3: String Module
import random

def ran_1_100():
    number = int(input('A number betwin 1 and 100 plz: '))
    pc_chose = random.randint(1, 100)
    if pc_chose != number:
        print (f'You lose the pc number is {pc_chose}')
    if pc_chose == number:
        print ('You win')      

ran_1_100()

# 🌟 Exercise 3: String Module
import string

rand_string = ''
for i in range(5):
    rand_string += random.choice(string.ascii_uppercase)

print(rand_string)

# 🌟 Exercise 4 : Current Date
from datetime import datetime
now = datetime.now()
print(now)

# Exercise 5 : Amount Of Time Left Until January 1st
str_d1 = str(now.date())
str_d2 = '2023-3-11'


d1 = datetime.strptime(str_d1, "%Y-%m-%d")
d2 = datetime.strptime(str_d2, "%Y-%m-%d")

delta = d2 - d1
print(f'Difference is {delta.days} days')

# Exercise 6 : Birthday And Minutes
str_d1 = str(now.date())
str_d2 = '1986-3-11'


d1 = datetime.strptime(str_d1, "%Y-%m-%d")
d2 = datetime.strptime(str_d2, "%Y-%m-%d")

delta = d1 - d2
print(f'Difference is {delta.days*60*60} minutes')

# Exercise 7 : Upcoming Holiday
holy_name = 'Navidad'
date_now = str(now)

d1 = datetime(2023,12,24,00,00)
d2 = datetime.strptime(date_now, f"%Y-%m-%d %H:%M:%S.%f")

delta = d1 - d2
print(f'Difference beteen now and {holy_name} is {delta}')

# Exercise 8 : How Old Are You On Jupiter?


def old_in_seconds(sec):
    Earth_old_sec = sec / (365.25 * 24 * 60 * 60)
    print(f'is {round(Earth_old_sec, 2)} Earth-years old')
    Mercury_old_sec = (sec / (365.25 * 24 * 60 * 60)) / 0.2408467
    print(f'is {round(Mercury_old_sec, 2)} Mercury-years old')
    Venus_old_sec = (sec / (365.25 * 24 * 60 * 60)) / 0.61519726
    print(f'is {round(Venus_old_sec, 2)} Venus-years old')
    Mars_old_sec = (sec / (365.25 * 24 * 60 * 60)) / 1.8808158
    print(f'is {round(Mars_old_sec, 2)} Mars-years old')
    Jupiter_old_sec = (sec / (365.25 * 24 * 60 * 60)) / 11.862615
    print(f'is {round(Jupiter_old_sec, 2)} Jupiter-years old')
    Saturn_old_sec = (sec / (365.25 * 24 * 60 * 60)) / 29.447498
    print(f'is {round(Saturn_old_sec, 2)} Saturn-years old')
    Uranus_old_sec = (sec / (365.25 * 24 * 60 * 60)) / 84.016846
    print(f'is {round(Uranus_old_sec, 2)} Uranus-years old')
    Neptune_old_sec = (sec / (365.25 * 24 * 60 * 60)) / 164.79132
    print(f'is {round(Neptune_old_sec, 2)} Neptune-years old')

old_in_seconds(1000000000)

# Exercise 9 : Faker Module
# import faker
# fake = Faker()

# i have problems to import faker
