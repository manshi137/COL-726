import numpy as np

def generate_sequence(n):
    x_values = np.zeros(n, dtype=np.float32)
    # x_values[0] = np.float32(11)/np.float32(2)
    # x_values[1] = np.float32(61)/np.float32(11)
    x_values[1] = 11/2
    x_values[2] = 61/11
    for k in range(2, n-1):
        # x_values[k+1] =  111- (1130-3000/x_values[k-1])/x_values[k]
        x_values[k+1] = np.float32(111) - (np.float32(1130) - np.float32(3000)/x_values[k-1]) / x_values[k]
        
        
    return x_values


n = 11
sequence = generate_sequence(n)
print(sequence)

def f(x, y):
    return (111 -(1130 -3000/y)/x , x )
            
print(f(5, 5))
print(f(6 , 6))
print(f(5, 100))
print(f(100, 100))

for i in range(0, n):
    print("x", i," = ", sequence[i])