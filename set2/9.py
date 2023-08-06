### Problem **9: Create a dictionary by extracting the keys from a given dictionary**
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# **Given dictionary**:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# # Keys to extract
# keys = ["name", "salary"]
# **Expected output:**
# {'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
dict = {}
for k in sample_dict:
 for i in range(0,(len(keys)),1):
   if (k==keys[i]):
     dict[k]=sample_dict[k]


print(dict)