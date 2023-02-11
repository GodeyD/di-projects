# Challenge 1

number = int(input('a number plz: '))
length = int(input('a length plz: '))
list_numbers = []

for n in range(length):
    list_numbers.append((n+1) * number)
print(f'number: {number} - length {length} ➞ {list_numbers}')

# Challenge 2
in_str: str = "bbbbbooommmbbbbbooonnn"

result_str = in_str[0]

for char in in_str[1:]:
    if result_str[-1] != char:
        result_str += char

print(result_str)  