# FizzBuzz: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".

for i in range(1,100,1):
  if(i%3==0 and i%5==0):
    print("FizzBuzz")
  elif(i%3==0):
    print("Fizz")
  elif(i%5==0):
    print("Buzz")
  else:
    print(i)