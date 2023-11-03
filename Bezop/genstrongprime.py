import random
import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def is_strong_prime(p, q):
    if not is_prime(p) or not is_prime(q):
        return False
    if math.gcd((p - 1), (q - 1)) > 10:
        return False
    if math.gcd((p - 1), (q - 1)) <= 2:
        return False
    if math.gcd((p + 1), (q + 1)) > 10:
        return False
    if not is_prime((p - 1) // 2) or not is_prime((q - 1) // 2):
        return False
    return True


def generate_strong_prime():
    while True:
        p = random.randint(1000, 10000)
        if not is_prime(p):
            continue
        q = random.randint(1000, 10000)
        print(p, q)
        if not is_prime(q):
            continue
        if is_strong_prime(p, q):
            return p, q


# Пример использования генератора сильных простых чисел
p, q = generate_strong_prime()
print("Сгенерированные сильные простые числа:")
print("p =", p)
print("q =", q)