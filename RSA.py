from sys import argv

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a, b) * b

def fast_pow(b, p, mod):
    if p == 0:
        return 1
    elif p % 2 == 1:
        return fast_pow(b, p - 1, mod) * b % mod 
    else:
        temp = fast_pow(b, p / 2, mod) % mod
        return temp ** 2 % mod

def key_gen(PRIME):
    N = PRIME[0] * PRIME[1]
    L = lcm(PRIME[0] - 1, PRIME[1] - 1)
    for E in range(2, L):
        if gcd(E, L) == 1:
            break
    from random import randint
    D = randint(2, L - 1)
    while D < L:
        if E * D % L == 1:
            break
        D += 1
    return (E, N), (D, N)

def encrypt(plain, pub_key):
    return fast_pow(plain, pub_key[0], pub_key[1])

def decrypt(cipher, pvt_key):
    return fast_pow(cipher, pvt_key[0], pvt_key[1])
try:
    if argv[1] == "keygen":
        PRIME = (int(input("type in the first prime:")), int(input("\ntype in the second prime:")))
        print("\npublic key:", key_gen(PRIME)[0], "\nprivate key:", key_gen(PRIME)[1])
except IndexError:
    pass

print(encrypt(255, (3, 101284087)))