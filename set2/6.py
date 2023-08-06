# ### Problem **6: Concatenate two lists in the following order**
# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```
# **Expected output:**
# ```
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# ```

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
n = len(list1)
m = len(list2)
for i in range(0,n,1):
  for j in range(0,m,1):
    list3.append(list1[i] + " " + list2[j])


print(list3)