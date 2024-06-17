import numpy as np
import matplotlib.pyplot as plt

limit = 100
def generate_fibonacci(n):
    # fib_numbers = [np.float32(1.0), np.float32(1.0)]
    fib_numbers = [np.float64(1.0), np.float64(1.0)]
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers



def recompute_fibonacci(n):
    refib_numbers = [fibonacci_numbers[n-1], fibonacci_numbers[n-2]]
    while len(refib_numbers) < n:
        refib_numbers.append(refib_numbers[-2] - refib_numbers[-1])
    return refib_numbers


fibonacci_numbers = generate_fibonacci(limit)
diff_values = []
print(type(fibonacci_numbers[0]))
for i in range(2, limit):
    recompute_fibonacci_numbers = recompute_fibonacci(i)
    # print(recompute_fibonacci_numbers)
    recomputed_f0= recompute_fibonacci_numbers[i-1]
    diff_values.append(recomputed_f0-1)

for i in range(2, 90):
    # print("fib({}) = {}".format(i, fibonacci_numbers[i]))
    print("diff({}) = {}".format(i, diff_values[i]))
plt.plot(diff_values, label='Difference b/w Recomputed and Original f(0)')
plt.xlabel('n')
plt.ylabel('Difference Values')
plt.title('Difference b/w Recomputed and Original f(0) in single precision')
plt.legend()
plt.grid(True)
plt.show()


