# 🌟 Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

garfiel = Cat(cat_name='Garfiel', cat_age=4)
michi = Cat(cat_name='Michi', cat_age=3)
pecas = Cat(cat_name='Pecas', cat_age=5)

def oldest_cat(*cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat

    print(f"Oldest cat: {oldest_cat.name}, and is {oldest_cat.age} years old")

oldest_cat(pecas, garfiel, michi)

# 🌟 Exercise 2 : Dogs
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    
def bark(dog):
    print(f'{dog.name} goes woof!')

def jump(dog):
    print(f'“{dog.name} jumps {dog.height*2} cm high!”.')

davids_dog = Dog(dog_name='Rex', dog_height=50)

bark(davids_dog)
jump(davids_dog)

sarahs_dog = Dog(dog_name='Teacup', dog_height=20)

bark(sarahs_dog)
jump(sarahs_dog)

if davids_dog.height > sarahs_dog.height:
    print(f'The bigger dog is {davids_dog.name}')
else:
    print(f'The bigger dog is {sarahs_dog.name}')

# 🌟 Exercise 3 : Who’s The Song Producer?
class Song:
    def __init__(self, lyrics):
        self.song = lyrics

def sing_me_a_song(song):
    for st in song.song:
        print(st)    
    
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

sing_me_a_song(stairway)

# Exercise 4 : Afternoon At The Zoo
import string
class Zoo:
    def __init__(self, zoo_name= str):
        self.animals = []
        self.name = zoo_name 
    
    def add_animal(new_animal):
        if new_animal not in new_animal.animals:
            new_animal.animals.append(new_animal.name)

    def get_animals(*animals):
        print(animals)

    def sell_animal(animal_sold):
        if animal_sold in animal_sold.animals:
            animal_sold.animals.remove(animal_sold)

    def sort_animals(self):
        order_animals = []
        new_animmals = []
        for i in range(0, len(string.ascii_letters)):
            globals()['animal_first_letter%s' % i] = []
            for word in self.animals:
                if word[0] == string.ascii_letters[i]:
                    globals()['animal_first_letter%s' % i].append(word)        
            order_animals.append(globals()['animal_first_letter%s' % i]) 
        new_animmals.append([x for x in order_animals if x])
        new_animmals_dict = {}
        for i, item in enumerate(new_animmals[0]):
            new_animmals_dict[i+1] = item
        return new_animmals_dict 

    def get_groups(self):
        for group in self.sort_animals():
            print(group)

ramat_gan_safari =  Zoo('zookeeper')
new_dog = Zoo(zoo_name='perro')
new_cat = Zoo(zoo_name='gato')

ramat_gan_safari.add_animal()
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
