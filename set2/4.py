# ### Problem **4: Arrange string characters such that lowercase letters should come first**
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# **Given**:
# ```
# str1 = PyNaTive
# ```
# **Expected Output**:
# ```
# yaivePNT
# ```

str1 = "PyNaTive"

s1 = ""  
s2 = ""  

for char in str1:
    if char.islower():
        s1 = s1 + char
    else:
        s2 = s2 + char

result = s1 + s2  

print(result)
