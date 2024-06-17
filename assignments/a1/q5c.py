import matplotlib.pyplot as plt
import numpy as np

limit = 100 
c = np.float32(1.0) + np.float32(np.sqrt(3)/100)
# c = np.float64(1.0) + np.float64(np.sqrt(3)/100)

def generate_pib(n):
    pib_numbers = [np.float32(1.0), np.float32(1.0)]
    # pib_numbers = [np.float64(1.0), np.float64(1.0)]
    while len(pib_numbers) < n:
        pib_numbers.append(c*pib_numbers[-1] + pib_numbers[-2])
    return pib_numbers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

pib_numbers = generate_pib(limit)

def recompute_pib(n):
    repib_numbers = [pib_numbers[n-1], pib_numbers[n-2]]
    while len(repib_numbers) < n:
        repib_numbers.append(repib_numbers[-2] - c*repib_numbers[-1])
    return repib_numbers

fibonacci_numbers = generate_pib(limit)
diff_values = []
for i in range(2, limit):
    recompute_pib_numbers = recompute_pib(i)
    # print(recompute_fibonacci_numbers)
    recomputed_p0= recompute_pib_numbers[i-1]
    diff_values.append(recomputed_p0-1)
for i in range(0, 90):
    # print("fib({}) = {}".format(i, fibonacci_numbers[i]))
    print("diff({}) = {}".format(i, diff_values[i]))
print(type(recompute_pib_numbers[0]))
plt.plot(diff_values, label='Difference b/w Recomputed and Original pib(0)')
plt.xlabel('n')
plt.ylabel('Difference Values')
plt.title('Difference b/w Recomputed and Original pib(0) in single precision')
plt.legend()
plt.grid(True)
plt.show()

