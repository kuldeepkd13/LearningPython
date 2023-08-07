def longest(strings):
    if not strings:
        return ""
    
    shortest = min(strings, key=len)
    
    for i, char in enumerate(shortest):
        for string in strings:
            if string[i] != char:
                return shortest[:i]
    
    return shortest


input = ["flower", "flow", "flight"]
output = longest(input)
print(output)  
