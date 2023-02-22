# iterate over three lists
import itertools

list_one = ['a', 'b', 'c']
list_two =['d', 'e', 'f']
list_three = ['1', '2', '3']

result = itertools.chain(list_one, list_two, list_three)
print(result)

for element in result:
  print (element)