# Challenge 1
# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
word = input('Give me a good word: ')

index = []
letter_key = []


def indices(lst, item):
   return [i for i, x in enumerate(lst) if x == item]

for letter in word:
    letter_key.append(letter)    
    new = indices(word, letter)
    index.append(new)
    
new_dict = dict(zip(letter_key, index))

print(new_dict)

# Challenge 2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

for key in items_purchase:
    item: str = items_purchase[key]
    item_list: list = list(item)
    del item_list[0]
    item: str = "".join(item_list)
    item: str =  item.replace(',','')
    item: int = int(item)
    items_purchase[key] = item


wallet: int = int(wallet[1:])

items_afford = []

for x in items_purchase.values():   
    if x < wallet: 
        items_afford.append(list(items_purchase.keys())[list(items_purchase.values()).index(x)])
print(items_afford)

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

for key in items_purchase:
    item: str = items_purchase[key]
    item_list: list = list(item)
    del item_list[0]
    item: str = "".join(item_list)
    item: str =  item.replace(',','')
    item: int = int(item)
    items_purchase[key] = item


wallet: int = int(wallet[1:])

items_afford = []

for x in items_purchase.values():   
    if x <= wallet: 
        items_afford.append(list(items_purchase.keys())[list(items_purchase.values()).index(x)])
print(items_afford)

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

for key in items_purchase:
    item: str = items_purchase[key]
    item_list: list = list(item)
    del item_list[0]
    item: str = "".join(item_list)
    item: str =  item.replace(',','')
    item: int = int(item)
    items_purchase[key] = item


wallet: int = int(wallet[1:])

items_afford = []

for x in items_purchase.values():   
    if x <= wallet: 
        items_afford.append(list(items_purchase.keys())[list(items_purchase.values()).index(x)])

if items_afford == []: print('Nothing')
else : print(items_afford)