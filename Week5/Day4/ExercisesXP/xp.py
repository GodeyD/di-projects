# # 🌟 Exercise 1 – Random Sentence Generator
# import random

# f = 'word_list.txt'

# with open(f, 'r') as f:
#     secret_data = f.read()

# def get_words_from_file():
#     pre = []
#     pre_collection = []
#     collection = []
#     for word in secret_data:
#         pre.append(word)
#     pre_collection = ''.join(pre)
#     collection = pre_collection.split('\n')
#     return collection    

# get_words_from_file()

# def get_random_sentence(length):
#     rand_phrase = ''
#     for i in range(length):
#         ran = str(random.choice(get_words_from_file()))
#         rand_phrase += f'{ran} '
#     print(rand_phrase.lower())

# def main():
#     print('You will get a random words')
#     length_input = input('Chose a interger  between 2 and 20: ')
#     length = int(length_input)
#     if type(length) == int:
#         return get_random_sentence(length)
#     else:
#         print ("Thats not a interger")
#         return
# main()

# 🌟 Exercise 2: Working With JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

print(data['company']['employee']['payable']['salary'])
data['company']['employee']['birth_date'] = '11-03-1986'
print(data)

json_file = "index.json"

with open(json_file, 'w') as file_obj:
    json.dump(data, file_obj, indent = 2, sort_keys=True)

