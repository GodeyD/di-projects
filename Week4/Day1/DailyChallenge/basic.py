user: str = input("Your input: ")

if len(user) < 10:
    print('string not long enough')
elif len(user) > 10:
    print('string is too long')
else:
    print('10 characters long string!')

first_char: str = user[0]
last_char: str = user[-1]

print(first_char)
print(last_char)

string: str = ''
for char in user:
    string += char
    print(string)

import random
user_list = list(user)
random.shuffle(user_list)
print(''.join(user_list))