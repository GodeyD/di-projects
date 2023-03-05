from anagram_checker import *

D = AnagramChecker()

user_choice = ''
user_choice = input('put a word or exit: ')  

while user_choice.lower() != 'exit':
    if AnagramChecker.is_valid_word(user_choice):
        if len(user_choice.split()) > 1:
            print("must be a single word")
    else:
        print('put a normal word')
    D.get_anagrams(user_choice)
    for w in D.get_anagrams(user_choice):
        is_anagram(user_choice, w)

    result = ''
    for w in D.get_anagrams(user_choice):
        result += f'{w}, '
    result = result[:-2]    
    result += '.'
    print(f'''    YOUR WORD: ”{user_choice}”
    this is {D.not_english} a valid English word.
    Anagrams for your word: {result}''')
    user_choice = input('put a word or exit: ')



# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


