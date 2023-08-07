def fun(n):
  if(n<0):
    return 0
  elif(n==1 or n==0):
    return 1
  return fun(n-1)+fun(n-2)


n=3
step = fun(n)
print(step)