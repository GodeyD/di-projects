# 🌟 Exercise 1 : Set
my_fav_numbers = {5, 7, 9}
my_fav_numbers.add(4)
my_fav_numbers.add(8)
my_fav_numbers.discard(9)

friend_fav_numbers = {1, 2, 3}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# 🌟 Exercise 2: Tuple
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# No, you can't because tuples are immutable and therefore the sum can not be modified.

# 🌟 Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0, 'Apples')
count = basket.count('Apples')
basket.clear()

print(basket)

# 🌟 Exercise 4: Floats
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
list_floats = [1.5]
while list_floats[-1] != 5: 
    list_floats.append(list_floats[-1] + 0.5)

for i, num in enumerate(list_floats):
    if int(num) == num:
        list_floats[i] = int(num)


print(list_floats) 

# 🌟 Exercise 5: For Loop
for nun in range(1, 21): print(nun)

for nun in range(1, 21):
    if (nun - 1) % 2 == 0: print(nun)

# 🌟 Exercise 6 : While Loop
my_name = 'Diego'
user_name = input ('Put your name, i hope is Diego: ')
while user_name != my_name : user_name = input ('Put your name, i hope is Diego: ')

# 🌟 Exercise 7: Favorite Fruits
user_fruits = input('Put favorite fruit(s) (one or several fruits) plz separate whit spaces: ')
user_list_of_fruits = user_fruits.split()
print(user_list_of_fruits)
user_select_fruit = input('chouse one fruit: ')
if  user_select_fruit in user_list_of_fruits: 
    print('You chose one of your favorite fruits! Enjoy!')
else :
    print('You chose a new fruit. I hope you enjoy!')

# Exercise 8: Who Ordered A Pizza ?
topping = input('whtat pizza toppings want? put quit when finish: ')
topping_list = ''
while topping != 'quit': 
    topping_list += f'{topping}, '
    print(f'you’ll add {topping} to your pizza')
    topping = input('whtat pizza toppings want? put quit when finish: ')

print(topping_list)
total_cost = 10 + 2.5*len(topping_list.split())
print(f'Your pizza will have {topping_list}and cost ${total_cost}')

# Exercise 9: Cinemax
ages = input('what the age of you? then put your family ones. Put quit when finish: ')
ages_list = []
while ages != 'quit': 
    ages_list.append(int(ages))
    ages = input('what the age of you? then put your family ones. Put quit when finish: ')

total_ticket_cost = 0
for age in ages_list:
    if age >= 3 and age <= 12:
        total_ticket_cost += 10
    elif age > 12:
        total_ticket_cost += 15
    else:
        None

print(f'The total cost of the family is ${total_ticket_cost}')

names = ['Gil', 'Rita', 'Emi', 'Alejandro']

for name in names: 
    teen_age = int(input(f'hi {name} give me your age: '))
    if teen_age >= 16 and teen_age <= 21:
        names.remove(name)

print(names)   

# Exercise 10 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
list_number = 0
for sandwich in sandwich_orders:
    list_number += 1
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)
    print(f'{list_number}.- I made your {sandwich}')

# Exercise 11 : Sandwich Orders#2
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
print('deli has run out of pastrami')

pastrami = "Pastrami sandwich"
while pastrami in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    
print(sandwich_orders)