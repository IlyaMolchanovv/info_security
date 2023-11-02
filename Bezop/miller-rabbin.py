from random import randint

def milrab(p):
    if p == 1: return False
    if p == 2: return True
    if p % 2 == 0: return False
    m, k = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = randint(2, p - 1)
    z = pow(a, m, p)
    if z == 1 or z == p - 1: return True
    while k > 1:
        z = pow(z, 2, p)
        if z == 1: return False
        if z == p - 1: return True
        k = k - 1
    return False

def is_prime(p, r=10):
    for i in range(r):
        if not milrab(p):
            return False
    return True


print(is_prime(28))
