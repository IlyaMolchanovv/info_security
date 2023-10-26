def perebor(g, p, a):
    x = 0
    while True:
        x = x + 1
        if pow(g, x, p) == a:
            print(f'{x}')
            break

perebor(2, 443, 103)





































# from math import isqrt
#
#
# def fermat(n, verbose=True):
#     a = isqrt(n)
#     b2 = a * a - n
#     b = isqrt(n)
#     count = 0
#     while b * b != b2:
#         if verbose:
#             print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
#         a = a + 1
#         b2 = a * a - n
#         b = isqrt(b2)  # int(b2**0.5)
#         count += 1
#     p = a + b
#     q = a - b
#     assert n == p * q
#     print('a=', a)
#     print('b=', b)
#     print('p=', p)
#     print('q=', q)
#     print('pq=', p * q)
#     return p, q
#
#
# n = 8
# fermat(n)
