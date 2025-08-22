# Write a Python program to count how many times each character appears in a string.

mystr="jay patel"
my_dict={}

for ch in mystr:
    if ch not in my_dict:
        my_dict[ch]=mystr.count(ch)

print(my_dict.items())
