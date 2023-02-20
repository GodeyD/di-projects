class Farm:

    def __init__(self, name: str):
        self.farm_name = name
        self.animals: dict = {}

    def add_animal(self, name: str, amount: int = 1) -> None:
        if name not in self.animals:
            self.animals[name] = amount 
        else: 
            self.animals[name] += amount

    def get_info(self):

        out_str: str = f"{self.farm_name}'s farm\n\n"
        for name, amount in self.animals.items():
            out_str += f'{name} : {amount}\n'
        strange_str = '\n     E-I-E-I-0!'
        out_str += strange_str
        return out_str

    def get_animal_types(self) -> list:
        
        animal_names = list(self.animals.keys())
        animal_names.sort()
        return animal_names

    def get_short_info(self):
        
        animals_joined: str = ', '.join(self.get_animal_types())
        print(f"{self.farm_name}'s farm has {animals_joined}.")

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5) 
macdonald.add_animal('sheep') 
macdonald.add_animal('sheep')       
macdonald.add_animal('goat', 12)
macdonald.add_animal('cat', 2)

print(macdonald.animals)
macdonald.get_short_info()