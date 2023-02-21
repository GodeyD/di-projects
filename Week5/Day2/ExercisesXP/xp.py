class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [Bengal('Garfield', 4), Chartreux('DonGato', 10), Siamese('Cleo', 8)]
sara_pets  = Pets(all_cats)
sara_pets.walk()

class Dog: 

    def __init__(self, name: str, age: int, weight: int):
        
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self) -> str:
        return f'{self.name} is barking'

    def run_speed(self) -> int:
        return self.weight/self.age*10

    def fight(self, other_dog) -> str:

        winner = None

        if self.run_speed() * self.weight > other_dog.run_speed() * self.weight:
            winner = self
        else:
            winner = other_dog

        return f'{winner.name} has won!'

if __name__ == '__main__':
    
    rex = Dog('Rex', 4, 20)
    bob = Dog('Bob', 6, 15)
    laki = Dog('Laki', 5, 17)
    
