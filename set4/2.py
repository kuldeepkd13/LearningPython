list =  [64, 34, 25, 12, 22, 11, 90]
n = len(list)

for i in range(0,n-2,1):
  for j in range(0,n-i-1,1):
    if(list[j]>list[j+1]):
      temp = list[j]
      list[j] =list[j+1]
      list[j+1]=temp


print(list)