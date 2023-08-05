number = 13
def prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if prime(number):
  print(number, "is a prime number")
else:
    print(number, "is not a prime number")