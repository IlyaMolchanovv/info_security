from math import isqrt


def solve(g, a, p):
    k = isqrt(p) + 1
    gk = pow(g, k, p)
    y = gk
    h = {}  # словарь, ключи - элементы группы, значения - степени порождающего элемента
    for i in range(1, k + 1):
        h[y] = i
        y = y * gk % p

    for j in range(0, k):
        r = a * pow(g, j) % p
        i = h.get(r, -1)
        if i != -1: return i * k - j


def start():
    #print('g^(x) mod p = a:')
    g = 6
    a = 12
    p = 229
    x = solve(g, a, p)
    print(f'Проверка:\n{g}^{pow(x, 1, p-1)} mod {p} = {a}')
    print(f'Ответ:\nlog{g}_{a} mod {p-1} = {pow(x, 1, p-1)}')



# Запуск программы
start()
#
# def child_velikan(g, p):
#     m = k = round(sqrt(p)) + 1
#     b = pow(g, m)
#     u = [pow(b, i) for i in range(1, m+1)]
#     v = [a*pow(g, j) for j in range(1, m+1)]
