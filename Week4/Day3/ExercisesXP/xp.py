# 🌟 Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))

# 🌟 Exercise 2 : Cinemax 
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_ticket_cost = 0
ages_list = [*family.values()]
for age in ages_list:
    if age >= 3 and age <= 12:
        total_ticket_cost += 10
    elif age > 12:
        total_ticket_cost += 15
    else:
        None

print(total_ticket_cost)

# 🌟 Exercise 3: Zara
brand = {
    'name': 'Zara', 
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': 'men, women, children, home', 
    'international_competitors': 'Gap, H&M, Benetton', 
    'number_stores': 7000, 
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': 'pink, green',
    }
}

brand['number_stores'] = 2

print(f'''Saras clients are ones ho likes clothes of {brand['type_of_clothes']}''')
   
country = {'country_creation': 'Spain',}
brand.update(country)

if brand.setdefault('international_competitors'):
    brand['international_competitors'] += ', Desigual'
   
del brand['creation_date']
print((brand['international_competitors']).split()[-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

more_on_zara = {
    'creation_date': 1975,  
    'number_stores': 10000,
}
brand.update(more_on_zara)
print(brand['number_stores']) 


# Exercise 4 : Disney Characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
cuantity = []

for n in range(len(users)):
    cuantity.append(n)
disney_users_A = dict(zip(users, cuantity))

print(disney_users_A)

disney_users_B = dict(zip(cuantity, users))
print(disney_users_B)

disney_users_C = dict(zip(sorted(users), cuantity))
print(disney_users_C)

users_i = []
for char in users:
    for letter in  char:
        if letter == 'i': users_i.append(char) 
        

disney_users_AA =  dict(zip(users_i, cuantity))
print(disney_users_AA)

users_i = []
for char in users:
    if char[0] == 'M' or char[0] == 'P':
        users_i.append(char)

disney_users_AB =  dict(zip(users_i, cuantity))
print(disney_users_AB)