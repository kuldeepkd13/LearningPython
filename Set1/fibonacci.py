def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    return sequence

n = 5
fib = fibonacci(n)
print("Fibonacci sequence:", fib)
