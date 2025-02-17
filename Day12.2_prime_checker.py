import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # Only check divisibility up to the square root of num
    for i in range(3, int(math.sqrt(num)) + 1, 2):  # Skip even numbers
        if num % i == 0:
            return False

    return True

# Test cases
print(is_prime(2))   # Should return True (2 is prime)
print(is_prime(3))   # Should return True (3 is prime)
print(is_prime(4))   # Should return False (4 is not prime)
print(is_prime(73))  # Should return True (73 is prime)
print(is_prime(15))  # Should return False (15 is not prime)