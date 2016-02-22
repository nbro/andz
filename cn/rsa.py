# RSA

from random import randint


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n**(0.5) + 1)):
        if n % i == 0:
            return False
    return True


# Note that p and q should be actually greater than 2^32 for RSA to be difficult to break

def pnq():
    p = 1
    while not is_prime(p):
        p = randint(10000, 1000000)

    q = 1
    while not is_prime(q) or q == p:
        q = randint(10000, 1000000)
    return p, q

# Step 1: choose primes p and 1
p, q = pnq()

print("p = ", p, ", q = ", q, sep="")

# Step 2: calculate n
n = p*q
print("n =", n)


# Step3: Calculate phi(n) = (p - 1)*(q - 1)

def get_phi(p, q):
    # phi is Euler's totient function
    # This value is kept private
    return (p - 1) * (q - 1)  # pq - p - q + 1 = n - p - q + 1 = n - (p + q - 1)

phi = get_phi(p, q)  # phi of n

print("phi(", n, ") = ", phi ,sep="")

# The following implementations are based on the Wikipedia article and
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
# this last post contains a nice proof...

def gcd_i(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def gcd_r(a, b):
    # Use this function rather than gcd_i because it seems to be faster
    if a == 0:
        return b
    if b == 0:
        return a
    r = a % b
    return gcd_r(b, r)


def test1():
    import time

    s2 = time.time()
    for i in range(10000):
        assert gcd_i(q, p) == 1
    e2 = time.time()
    f2 = e2 - s2

    s1 = time.time()
    for i in range(10000):
        assert gcd_r(q, p) == 1
    e1 = time.time()
    f1 = e1 - s1

    print("f1 =", f1, "| f2 =", f2, "| f1 < f2 =", f1 < f2)

# test1()    


# Step 4: Choose e, such that 1 < e < phi(n)
# and gcd(e, phi(n)) = 1, that is e and phi(n) are coprime
# variable is called k = phi(n)


def coprime(a, b):
    # returns true if a and b are coprime
    return gcd_r(a, b) == 1

def ge(k):
    #  Returns e such that 1 < e < phi(n) = k
    e = randint(2, k - 1)  # 1 < e < phi(n) = k
    while not coprime(k, e):
        e = randint(1 + 1, k - 1)
    return e

#e = ge(phi)
e = 17
print("e =", e)


def gd(e, k):
    # returns d, the modular multiplicative inverse of e (mod phi(n))
    return (1 % k) * (1/e)

#d = gd(e, 3120)
print("d =", d)
