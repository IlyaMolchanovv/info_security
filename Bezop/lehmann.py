import random


def is_prime_lehmann(n, k):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, (n - 1) // 2, n)
        if x != 1 and x != n - 1:
            return False
    return True


n = 9336915522723349066610316226699531894519280664284845643863751185456374972624565207528148138716709204273382546786121917024443446073681486569052083583571498321075906767938955949883322408554982639561658156529897733139107202878855374089905392080395409982502974825147302668072139
k = 500
result = is_prime_lehmann(n, k)

if result:
    print(f"n={n}\nпростое число.")
else:
    print(f"n={n}\nне простое число.")
