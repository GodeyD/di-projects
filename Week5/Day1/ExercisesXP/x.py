import string

animals = ['Perro', 'Gato']

def add_animal(new_animal):
        if new_animal not in animals:
            animals.append(new_animal)
        print(animals)

add_animal('loro')
add_animal("Ape")
add_animal("Baboon")
add_animal("Bear")
add_animal('Cougar')
add_animal('Eel')
add_animal('Emu')

ej = { 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}
direct = {i: animals[i] for i in range(0, len(animals))}
order_animals = []
new_animmals = []
def order():
    for i in range(0, len(string.ascii_letters)):
        globals()['animal_first_letter%s' % i] = []
        for word in animals:
            if word[0] == string.ascii_letters[i]:
                globals()['animal_first_letter%s' % i].append(word)        
        order_animals.append(globals()['animal_first_letter%s' % i]) 
    new_animmals.append([x for x in order_animals if x])
    new_animmals_dict = {}
    for i, item in enumerate(new_animmals[0]):
        new_animmals_dict[i+1] = item
    print(new_animmals_dict)    
order()


# print()            

print(string.ascii_letters)