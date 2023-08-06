st= "madam"
s = ""
for i in range(-1,-(len(st))-1,-1):
  s= s+st[i]

if(s==st):
  print("The word madam is a palindrome")
else:
  print("The word madam is not a palindrome")