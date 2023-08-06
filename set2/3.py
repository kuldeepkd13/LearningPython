# ### Problem **3: Append new string in the middle of a given string**
# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.
# **Given**:
# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```
# **Expected Output**:
# ```
# AuKellylt
# ```
s1 = "Ault"
s2 = "Kelly"
n = len(s1)
m = len(s2)
mid= int(n/2)

s = ""

for i in range(0,mid,1):
  s+=s1[i]

s = s+s2

for i in range(mid,n,1):
  s+=s1[i]
  
print(s)