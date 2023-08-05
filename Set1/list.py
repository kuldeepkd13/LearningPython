numbers = []
for i in range(1, 10):
    numbers += [i]

print(numbers) 

#add a Number
numbers.append(11)
print(numbers) 
del numbers[1]
print(numbers) 

#sort
sorted_list_desc = sorted(numbers, reverse=True)
print(sorted_list_desc)