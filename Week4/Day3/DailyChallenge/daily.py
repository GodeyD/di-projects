# Challenge 1
user_number: int = int(input("Your number: "))
user_length: int = int(input("Your length: "))

result = []

for multipler in range(1, user_length + 1):
    result.append(user_number * multipler)

print(result)

# Challenge 2
in_str: str = "bbbbbooommmbbbbbooonnn"

result_str = in_str[0]

for char in in_str[1:]:
    if result_str[-1] != char:
        result_str += char

print(result_str)        

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    sample_dict.pop(key, None)
   

print(sample_dict)