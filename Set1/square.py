numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(numbers)
sq = []
for i in range(0,length,1):
    a = numbers[i] ** 2
    sq.append(a)

print(sq)