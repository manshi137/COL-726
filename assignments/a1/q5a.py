import matplotlib.pyplot as plt
import numpy as np

# Generate Fibonacci numbers up to a certain limit
limit = 100  # You can adjust this limit as needed
# c = 1 + np.float32(np.sqrt(3)/100)
c = 1 + np.float64(np.sqrt(3)/100)

# Function to generate Fibonacci numbers up to n
def generate_fibonacci(n):
    # fib_numbers = [np.float32(1.0), np.float32(1.0)]
    fib_numbers = [np.float64(1.0), np.float64(1.0)]
    while len(fib_numbers) < n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers


def generate_pib(n):
    # pib_numbers = [np.float32(1.0), np.float32(1.0)]
    pib_numbers = [np.float64(1.0), np.float64(1.0)]
    while len(pib_numbers) < n:
        pib_numbers.append(c*pib_numbers[-1] + pib_numbers[-2])
    return pib_numbers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

pib_numbers = generate_pib(limit)
fibonacci_numbers = generate_fibonacci(limit)
for i in range(70, 80):
    print("pib({}) = {}".format(i, pib_numbers[i]))
    print("fib({}) = {}".format(i, fibonacci_numbers[i]))
print(type(pib_numbers[0]))
print(type(fibonacci_numbers[0]))
# Plot Fibonacci numbers and pib numbers in a log scale
plt.plot(fibonacci_numbers, label='Fibonacci Numbers')
plt.plot(pib_numbers, label='Pib Numbers')
plt.yscale('log')  # Set y-axis to log scale

# Mark 1/εmach for single and double precision
eps_single = np.finfo(np.float32).eps
eps_double = np.finfo(np.float64).eps
print(1/eps_single)
print(1/eps_double)
plt.axhline(y=1/eps_single, color='red', linestyle='--', label='1/εmach (Single Precision)')
plt.axhline(y=1/eps_double, color='blue', linestyle='--', label='1/εmach (Double Precision)')

plt.xlabel('Value in log scale')
plt.ylabel('Fib and Pib Numbers')
plt.title('Fibonacci and Pib Numbers in Log Scale Plot')
plt.legend()
plt.grid(True)
plt.show()
