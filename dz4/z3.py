import math
import random

random.seed(42)


def is_prime(n):
    if n <= 0:
        raise ValueError("n should be positive")

    if n != 2 and n % 2 == 0:
        return False

    if n < 9:
        return True

    if n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True


def _encrypt(K, x):
    n, e = K

    return (x ** e) % n


def _random_p_q():
    four_digit_primes = [x for x in range(1001, 10000, 2) if is_prime(x)]

    return random.sample(four_digit_primes, 2)


def _random_params():
    p, q = _random_p_q()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    five_digit_coprime_to_phi_n = [x for x in range(10000, 100000) if math.gcd(x, phi_n) == 1]
    e = random.choice(five_digit_coprime_to_phi_n)
    d = pow(e, -1, phi_n)

    return p, q, d, n, phi_n, e


def main(x, params=None):
    p, q, d, n, phi_n, e = params or _random_params()
    print(f"(p, q) = ({p}, {q})\n"
          f"n = {p} * {q} = {n}\n"
          f"e = {e}\n"
          f"d = {e}^-1 (mod {phi_n})= {d}"
          )
    return _encrypt((n, e), x)


if __name__ == '__main__':
    print(f"-----------TEST--------------")
    print(f"y = e_K({123645}) = {main(17, (3, 11, 3, 33, 20, 7))}")
    print(f"----------FINAL--------------")
    print(f"y = e_K({123645}) = {main(123645)}")


