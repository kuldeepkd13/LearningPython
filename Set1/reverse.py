str = "Python"
bag = ""
n = len(str)
for i in range(n - 1, -1,-1):
    bag += str[i]

print(bag)
