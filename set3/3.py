list = [2,7,11,15]
target=9

i=0
j=len(list)-1
while(i<j):
  if(list[i]+list[j]==target):
    print([i,j])
    break
  elif(list[i]+list[j]>target):
    j=j-1
  else:
    i=i+1