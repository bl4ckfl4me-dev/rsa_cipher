import random


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def generate_random_prime():
    num = random.randint(100, 500)

    while not(is_prime(num)):
        num = random.randint(100, 500)

    return num


def get_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def generate_keys():
    p = generate_random_prime()
    q = generate_random_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65_537
    while get_greatest_common_divisor(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)
    return e, d, n


def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]


def decrypt(encrypted_message, d, n):
    return ''.join(chr(pow(char, d, n)) for char in encrypted_message)
