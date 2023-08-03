def is_prime(number: int):
    square_root = int(number ** 0.5) + 1
    for factor in range(2, square_root):
        if number % factor == 0:
            return False
    return True


factors = []
factor = 2

number = 600851475143

while number > 1:
    while number % factor == 0:
        factors.append(factor)
        number /= factor
    factor += 1

prime_factors = [factor for factor in factors if is_prime(number=factor)]
max_prime_factor = max(prime_factors)
print(max_prime_factor)
