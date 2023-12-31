# ### Problem **8: Initialize dictionary with default values**
# In Python, we can initialize the keys with the same values.
# **Given**:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# **Expected output:**
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict = {}

for i in range(0,(len(employees)),1):
  dict[employees[i]]=defaults

print(dict)