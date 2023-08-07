list = [1,2,4,3]
n = len(list)
def fun(n,list):
  for i in range(0,n,1):
    for j in range(i+1,n,1):
      if(list[i]==list[j]):
        return True
  return False

result = fun(n,list)
print(result)