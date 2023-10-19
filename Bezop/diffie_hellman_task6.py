def diffie_hellman(p, g, a, b):
    # Вычисление открытых ключей
    A = (g ** a) % p
    B = (g ** b) % p

    # Вычисление общего секретного ключа
    secret_key_a = (B ** a) % p
    secret_key_b = (A ** b) % p

    # Проверка совпадения секретных ключей
    if secret_key_a == secret_key_b:
        return secret_key_a
    else:
        raise Exception("Ошибка: секретные ключи не совпадают")


def find_primitive_root(p):
    # Проверка, что p является простым числом
    if not is_prime(p):
        raise ValueError("p должно быть простым числом")

    # Вычисление phi(p)
    phi = p - 1

    # Поиск первообразного корня
    for alpha in range(2, p):
        is_primitive = True

        # Проверка критерия для каждого простого делителя q числа (p - 1)
        for q in prime_factors(phi):
            if pow(alpha, phi // q, p) == 1:
                is_primitive = False
                break

        if is_primitive:
            return alpha

    raise ValueError("Не удалось найти первообразный корень")


def is_prime(n):
    # Проверка, что число n является простым
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def prime_factors(n):
    # Получение списка простых делителей числа n
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_primitive_root(g, p):
    # Проверка, что g является первообразным корнем по модулю p
    phi = p - 1
    powers = []
    for i in range(1, phi + 1):
        power = pow(g, i, p)
        if power in powers:
            return False
        powers.append(power)
    return True


def task6():
    p = 97
    alpha = find_primitive_root(p)
    print(alpha)
    x = 4
    y = 13

    shared_secret_key_k = diffie_hellman(p, alpha, x, y)
    print("Общий секретный ключ:", shared_secret_key_k)


task6()
