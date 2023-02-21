from xp import Dog
import random

class PetDog(Dog):

    def __init__(self, name: str, age: int, weight: int):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self) -> None:
        print(self.bark())
        self.trained = True

    def play(self, *dogs: tuple) -> None: 
        other_dogs_names = [dog.name for dog in dogs]
        other_dogs_names_str = ", ".join(other_dogs_names)
        print(f'{self.name} and {other_dogs_names_str} all are playing!')
    
    def do_a_trick(self) -> None:
        tricks = [f"{self.name} does a barrel roll", 
        f"{self.name} stands on his back legs", 
        f"{self.name} shakes your hand",
        f"{self.name} plays dead"]

        if self.trained:
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained!")


if __name__ == '__main__':

    rex = Dog('Rex', 4, 20)
    bob = Dog('Bob', 6, 15)
    laki = Dog('Laki', 5, 17)

    pet = PetDog('Ross', 2, 10)

    pet.play(rex, bob, laki)
    pet.do_a_trick()    
    pet.train()
    print(pet.trained)
    pet.do_a_trick()