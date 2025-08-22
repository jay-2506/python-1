# Write a Python program to convert two lists into one
# dictionary using a for loop. 

list1=["name","age","city"]
list2=["Jay",20,"Dehgam"]

merged_dict={}

for i in range(len(list1)):
    merged_dict[list1[i]]=list2[i]

print(merged_dict)

