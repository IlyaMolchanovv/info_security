import numpy as np


def prime_factorization(number):
    factors = []
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    if number > 1:
        factors.append(number)

    return factors


def one_way_func(a, x, p):
    y = 1
    bin_x = str(bin(x))[2:][::-1]
    ost = a % p
    for k in bin_x:
        if k == '1':
            y = (y * ost) % p
        ost = (ost * ost) % p
    return y


def step2(g, n, t, S):
    count = 0
    equals = dict()
    k_start = 2
    if g in S:
        k_start += 1
    for k in range(k_start, n):
        gk = pow(g, k, n + 1)
        factors = prime_factorization(gk)
        if len(factors) != 0 and set(factors) <= S:
            count += 1
            equals[k] = factors
        if count == t:
            break

    return equals


def step3(equals, S):
    coef_matrix = []
    free_matrix = []

    for k in equals:
        free_matrix.append(k)
        row = []
        for elem_S in S:
            print(f"For k={k}, elem={elem_S}, count={equals[k].count(elem_S)}")
            count = equals[k].count(elem_S)
            row.append(count)
        coef_matrix.append(row)

    return coef_matrix, free_matrix


def solve_least_squares(coef_matrix, free_matrix):
    A = np.array(coef_matrix)
    b = np.array(free_matrix)
    x, residuals, _, _ = np.linalg.lstsq(A, b, rcond=None)
    return x


def step7(a, g, n, S):
    for k in range(1, n):
        agk = pow(a * pow(g, k), 1, n + 1)
        equals = prime_factorization(agk)
        if len(equals) != 0:
            row = []
            row_final = {}
            i = 0
            for elem_S in S:
                count = equals.count(elem_S)
                row.append(count)
                row_final[elem_S] = row[i]
                i += 1

            print(row_final)
            print(f"log{g}({a}) = ", end='')
            for key in row_final:
                if row_final[key] != 0:
                    print(f"{row_final[key]}log{g}({key})+", end='')

            print(f"(-1) (mod{n}), значит")
            return row_final


def poreadok(g, a, n):
    c = 10
    S = [2, 3, 5, 7]
    S = set(S)
    t = len(S)
    equals = step2(g, n, t, S)
    print(f"Факторная база = {equals}")
    coef_matrix, free_matrix = step3(equals, S)

    print(coef_matrix)
    print(free_matrix)

    # Создайте расширенную матрицу
    augmented_matrix = np.column_stack((coef_matrix, free_matrix))
    print(augmented_matrix)
    # Решите систему уравнений
    try:
        solution = np.linalg.solve(augmented_matrix[:, :-1], augmented_matrix[:, -1])
        # solution = solve_least_squares(coef_matrix, free_matrix)
    except np.linalg.LinAlgError:
        solution = [1, 1, 1, 1]
    solution_mod_n = [pow(int(x), 1, n) for x in solution]
    solution_final = {}
    i = 0
    for elem_S in S:
        solution_final[elem_S] = solution_mod_n[i]
        i += 1

    print("Решение системы: ")
    for key in solution_final:
        print(f"log{g}({key}) =", solution_final[key], f"(mod {n})")

    # solution_final = {2: 6, 3: 26, 5: 28, 7: 1}

    row_final = step7(a, g, n, S)
    print(f"log{g}({a}) = ", end='')
    for key in solution_final:
        if row_final[key] != 0:
            print(f"{row_final[key]}*{solution_final[key]}+", end='')
    print(f"(-1) (mod{n}), значит")

    print("Ответ:")
    lambo = -1
    for key in solution_final:
        lambo += row_final[key] * solution_final[key]
    lambo = pow(lambo, 1, n)
    print(f"log{g}({a}) = {lambo} (mod{n})")

    print("Проверка:")
    print(f"{g}^{lambo} mod {n + 1} = {pow(g, lambo, n + 1)}. Верно.")


poreadok(7, 26, 70)
