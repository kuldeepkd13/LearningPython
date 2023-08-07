list = [3,0,1]

max= float('-inf')

for i in range(0,(len(list)),1):
  if(list[i]>max):
    max=list[i]


sum = (max*(max+1))/2
for i in range(0,(len(list)),1):
  sum -=list[i]

print(sum)