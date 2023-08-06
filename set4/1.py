from collections import Counter

st = "cinema"
st1 = "iceman"

counter_st = Counter(st)
counter_st1 = Counter(st1)

are_anagrams = counter_st == counter_st1

print(are_anagrams)
