number = 6
def factorial(num):
  sum=1
  for i in range(1,num+1):
    sum = sum*i
  return sum

fact = factorial(number)
print(fact)