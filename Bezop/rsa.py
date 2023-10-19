from math import gcd


def fast_exponentiation_algorithm(a, n, m):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        p = 1
        ak = a
        i = n
        print(f"ak    i    s    p")
        while i > 0:
            s = i % 2
            if s == 1:
                p = p * ak % m
            ak = ak * ak % m
            i = (i - s) / 2
            print(f"{ak}    {i}    {s}    {p}")
        return p


# print(f"p = {fast_exponentiation_algorithm(12, 233761, 355207)}")


def euqlid(n, m):
    while n != 0 and m != 0:
        if (n > m):
            n %= m
        else:
            m %= n
    return n + m


# print(euqlid(233761, 355207))
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y


def encrypt(message, e, n):
    return pow(message, e, n)


def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)


p = 94483
q = 41521
n = p * q
m = (p - 1) * (q - 1)
e = []
for i in range(2, 10000):
    if gcd(i, m) == 1:
        print(i)
        e.append(i)

e = int(input("Выберите желаемый e: "))
k = euqlid(p - 1, q - 1)

d = pow(e, -1, m)
print("d = " + str(d))

d1 = int(d % (m / k))
print("d1 = " + str(d1))
M = 1032022

ciphertext = encrypt(M, e, n)
decrypted_message = decrypt(ciphertext, d1, n)

print("Шифровка сообщения:", ciphertext)
print("Расшифровка сообщения:", decrypted_message)

print("\nПроверим шифровку p: ")
ciphertext = encrypt(p, e, n)
decrypted_message = decrypt(ciphertext, d1, n)
print("Шифровка сообщения:", ciphertext)
print("Расшифровка сообщения:", decrypted_message)

print("\nПроверим шифровку 2p: ")
ciphertext = encrypt(2*p, e, n)
decrypted_message = decrypt(ciphertext, d1, n)
print("Шифровка сообщения:", ciphertext)
print("Расшифровка сообщения:", decrypted_message)

print("\nПроверим шифровку q: ")
ciphertext = encrypt(q, e, n)
decrypted_message = decrypt(ciphertext, d1, n)
print("Шифровка сообщения:", ciphertext)
print("Расшифровка сообщения:", decrypted_message)

print("\nПроверим шифровку 3q: ")
ciphertext = encrypt(3*q, e, n)
decrypted_message = decrypt(ciphertext, d1, n)
print("Шифровка сообщения:", ciphertext)
print("Расшифровка сообщения:", decrypted_message)