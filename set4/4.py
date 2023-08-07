def get(s):
    if len(s) == 1:
        return [s]

    permutations = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        sub = get(remaining)
        for perm in sub:
            permutations.append(char + perm)

    return permutations

input_string = "abc"
permutations = get(input_string)
print(permutations)
