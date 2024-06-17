x = [1, 2, 3, 4, 1.5, 3.4];
y = [2, 4, 5, 6, 5.5, 2.7];
b = [4.674, 11.349, 25.632, 13.075, 5.806, 1.981, 9.360, 3.009, 4.036, 2.955, 4.064, 4.105, 8.596, 11.614, 12.845];

// % Calculate elements of b
// for i in range(0, 6):
//     for j in range(i+1, 6):
//         b[i*6+j] -= (x[i] - x[j])**2 + (y[i] - y[j])**2
// write b in matlab

d = [];
for i in 1:6
    for j in i+1:6
        push!(d, (x[i] - x[j])^2 + (y[i] - y[j])^2);
    end
end

// # for i in range(0, 6):
// #     for j in range(i+1, 6):
// #         A[i][i] = x[i] - x[j]
// #         A[i][i+6] = y[i] - y[j]
// #         A[i][j] = -1*(x[i] - x[j])
// #         A[i][j+6] = -1*(y[i] - y[j])

A = zeros(15, 12);
for i in 1:6
    for j in  i+1:6
        A[i, i] = x[i] - x[j];
        A[i, i+6] = y[i] - y[j];
        A[i, j] = -1*(x[i] - x[j]);
        A[i, j+6] = -1*(y[i] - y[j]);
    end
end
