# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

input_new = ['without','hello','bag','world']
ouput_new = [x for x in sorted(input_new)]

print(ouput_new)