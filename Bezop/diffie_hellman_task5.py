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


def encrypt_word(word, shared_secret):
    # Преобразование слова в числовое значение
    numeric_values = [ord(c) for c in word]

    # Шифрование
    encrypted_values = [chr(numeric_value ^ 2) for numeric_value in numeric_values]
    encrypt = ''.join(encrypted_values)

    return encrypt


def task5():
    p = 23  # Простое число
    alpha = 5  # Первообразный корень по модулю p
    a = 6  # Закрытый ключ Алисы
    b = 15  # Закрытый ключ Боба

    shared_secret = diffie_hellman(p, alpha, a, b)
    print("Общий секретный ключ:", shared_secret)

    word = "группа"

    encrypted_word = encrypt_word(word, shared_secret)
    print("Зашифрованное слово:", encrypted_word)


task5()
