def single_number(nums):
    numsf = {}
    for num in nums:
        if num in numsf:
            numsf[num] += 1
        else:
            numsf[num] = 1
    
    for num, frequency in numsf.items():
        if frequency == 1:
            return num


input = [4, 1, 2, 1, 2]
output = single_number(input)
print(output)  
