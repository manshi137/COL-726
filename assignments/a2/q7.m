% matlab code
m = 21;
n = 12;
eps = 10^(-10);

t = zeros(m, 1);
A = zeros(m, n);
y = zeros(m, 1);

for i = 1:m
  t(i) = (i-1)/(m-1);
end

for j = 0:n-1
  A(:, j+1) = t.^j;
end

for i = 1:m
  tmp = 1;
  for j = 1:n-1
    tmp = tmp + t(i)^j;
  end
  y(i) = tmp;
end

fprintf('original y: \n');
disp(y);

u = rand(m, 1);

y_perturbed = zeros(m, 1);
for i = 1:m
  y_perturbed(i) = y(i) + (2*u(i)-1)*eps;
end

fprintf('y perturbed:\n');
disp(y_perturbed);


chol = chol_least_square(A, y);
fprintf('Result of Cholesky factorization:\n');
disp(chol);
fprintf('Error in Cholesky factorization: \n');
disp(norm(A*chol - y));


qr = leastSquare(A, y);
fprintf('Result of QR :\n');
disp(qr);
fprintf('Error in  QR factorization: \n');
disp(norm(A*qr - y));


chol_perturbed = chol_least_square(A, y_perturbed);
fprintf('Result of Cholesky factorization when y is perturbed:\n');
disp(chol_perturbed);
fprintf('Error in  Cholesky factorization when y is perturbed: \n');
disp(norm(A*chol_perturbed - y_perturbed));

qr_perturbed = leastSquare(A, y_perturbed);
fprintf('Result of QR when y is perturbed');
disp(qr_perturbed);
fprintf('Error in QR factorization when y is perturbed: \n');
disp(norm(A*qr_perturbed - y_perturbed));


fprintf('Condition number of A: \n');
disp(cond(A));
delta


% -------------------------------------------------------------
function x = chol_least_square(A, b)
    L = chol(A'*A, 'lower');
    y = L'\(A'*b);
    x = L\y;
end
% -------------------------------------------------------------
function x = leastSquare(A, b)
    [W, R] = house(A); % Compute QR factorization using Householder reflections
    Q = formQ(W); % Reconstruct Q matrix
    % Solve Rx = Q'b using back substitution
    x = R \ (Q' * b);
end
function [W, R] = house(A)
    [m, n] = size(A);
    W = zeros(m, n);
    R = A;

    for k = 1:n
        x = R(k:m, k);
        vk = sign(x(1)) * norm(x) * eye(length(x), 1) + x;
        vk = vk / norm(vk);
        R(k:m, k:n) = R(k:m, k:n) - 2 * vk * (vk' * R(k:m, k:n));
        W(k:m, k) = vk;
    end
end
function Q = formQ(W)
    [m, n] = size(W);
    Q = eye(m);

    for k = n:-1:1
        vk = W(k:m, k);
        Q(k:m, :) = Q(k:m, :) - 2 * vk * (vk' * Q(k:m, :));
    end
end
