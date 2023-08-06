# ### Problem **1: Print the following pattern**
# Write a program to print the following number pattern using a loop.
# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ```

n = 5

def printpattern(n):
  bag = ""
  for i in range(1,n+1,1):
    for _j in range (1,i+1,1):
      bag +=str(_j)+" "
    bag+= "\n"
  return bag

result = printpattern(n)
print(result)