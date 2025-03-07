def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_5 = print(factorial(5))

print("---Fibonacci---")
def fibonacci(n, iteration=0, cur=1, prev=0, sequence=[]):
    if n == 0:
        return sequence.append(0);
    if n == 1:
        sequence.append(0);
        sequence.append(1);
        return sequence
    iteration = n
    if iteration > 1 and len(sequence) < n:
        next_item = prev + cur
        cur_next = next_item
        prev_next = cur
        sequence.append(next_item)
        fibonacci(n,iteration-1,next_item,prev_next,sequence)
    return sequence

print(fibonacci(1))
