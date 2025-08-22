# Write a Python program to merge two lists into one dictionary using a loop.
keys=["name","age","address"]
values=["Jay",20,"Dehgam"]

merged_dict={}

for i in range(len(keys)):
     merged_dict[keys[i]] = values[i]

     
print(merged_dict)