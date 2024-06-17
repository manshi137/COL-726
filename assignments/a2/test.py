
# // You are given coordinates of 6 points as below, but these coordinates have some errors in them. For each pair of distinct points, you are given (approximate) distance between them. Now, you have to replace these 6 points by more precise coordinates such that the discrepancy between the measured distances and the actual reported distances between the points in minimized. Here is how we shall rephrase this as a least-squares problem. For each point (xi,yi), we want to perturb them by (xi + δi, yi + εi), where δi and εi are the unknowns, but are assumed to be small. Now, given two points, the square of the Euclidean distance between them can be written as
# // (xi +δi −xj −δj)2 +(yi +εi −yj −εj)2.
# // Now expand the above terms and remove any term involving product or square of the δ or ε. Thus, we get a linear expression in the unknowns. Use this idea to frame the problem as a least squares problem. Explain clearly the formulation obtained. Use this to find the corrections to the following points:
# // (xi, yi) = (1, 2), (2, 4), (3, 5), (4, 6), (1.5, 5.5), (3.4, 2.7). The matrix showing the measured pair-wise distances is as follows:
# // D = [[0 4.674 11.349 25.632 13.075 5.806 ]
# // [0 0 1.981 9.360 3.009 4.036]
# // [ 0 0 0 2.955 4.064 4.105 ]
# // [ 0 0 0 0 8.596 11.614 ]
# // [ 0 0 0 0 0 12.845]
# // [0 0 0 0 0 0 ]
# // ]
# // 
#  (xi, yi) = (1, 2), (2, 4), (3, 5), (4, 6), (1.5, 5.5), (3.4, 2.7). The matrix showing the measured pair-wise distances is as follows:
x = [1, 2, 3, 4, 1.5, 3.4]
y = [2, 4, 5, 6, 5.5, 2.7]


# d = []
# for i in range(1, 7):
#     d.append([0]*6)

# print(d)

# for i in range(1 , 7):
#     for j in range(i+1, 7):
#         d[i-1][j-1] = ((x[i-1] - x[j-1])**2 + (y[i-1] - y[j-1])**2)


d = [0]*6
e = [0]*6
# xnew = [x[0], x[1], x[2], x[3], x[4], x[5]] + [d[0], d[1], d[2], d[3], d[4], d[5]]
# ynew = [y[0], y[1], y[2], y[3], y[4], y[5]] + [e[0], e[1], e[2], e[3], e[4], e[5]]
# we want to find d and e such that the following is minimized
# x[i] - x[j]) * (d[i] - d[j]) + (y[i] - y[j]) * (e[i] - e[j]) + (x[i]-x[j])**2 + (y[i]-y[j])**2 - D[i][j] = 0

# write the above equation for all i and j
# we get a system of equations
# Ax = b
# where A is a 15x12 matrix
# x is a 12x1 matrix
# b is a 15x1 matrix

# x =(d1, e1, d2, e2, d3, e3, d4, e4, d5, e5, d6, e6)

x = [1, 2, 3, 4, 1.5, 3.4]
y = [2, 4, 5, 6, 5.5, 2.7]
b = [4.674, 11.349, 25.632, 13.075, 5.806, 1.981, 9.360, 3.009, 4.036, 2.955, 4.064, 4.105, 8.596, 11.614, 12.845]
for i in range(0, 6):
    for j in range(i+1, 6):
        b[i*6+j] -= (x[i] - x[j])**2 + (y[i] - y[j])**2
        
print(b)

A = []
for i in range(0, 15):
    A.append([0]*12)
# x[i] - x[j]) * (d[i] - d[j]) + (y[i] - y[j]) * (e[i] - e[j])  = b[i*]
    


# for i in range(0, 6):
#     for j in range(i+1, 6):
#         A[i][i] = x[i] - x[j]
#         A[i][i+6] = y[i] - y[j]
#         A[i][j] = -1*(x[i] - x[j])
#         A[i][j+6] = -1*(y[i] - y[j])

# x =(d1, e1, d2, e2, d3, e3, d4, e4, d5, e5, d6, e6)

