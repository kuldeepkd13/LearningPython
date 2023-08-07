n= 14

def fun(n):
    if n <= 0:
      return False
    return (n & (n - 1)) == 0


power = fun(n)
print(power)