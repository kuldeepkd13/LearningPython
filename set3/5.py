list = [64, 25, 12, 22, 11]
n = len(list)
for i in range(0,n,1):
  min = i
  for j in range(i+1,n,1):
    if(list[j]<list[min]):
      min = j

  temp = list[i]
  list[i]=list[min]
  list[min]=temp

print(list)