# returns: n, e, d
def genRSAkeys(p, q):
    phi = (p-1)*(q-1)
    # public key
    e = findcop(phi)
    d = modinv(e, phi)
    return p * q, e, d

def encrypt(m, e, n):
    return (m**e) % n

def decrypt(k, d, n):
    return (k**d) % n

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

#find first coprime number != 0
def findcop(n):
    for i in range(2, n):
        if egcd(i, n)[0] == 1:
            return i
    return None

if __name__ == '__main__':
    print("Insert prime number: ")
    p = int(input())
    print("Insert prime number: ")
    q = int(input())
    n, e, d = genRSAkeys(p, q)
    print("\nn: " + str(n))
    print("encryption key: " + str(e))
    print("decryption key: " + str(d) + "\n")
    print("Enter a message to encrypt: ")
    m = int(input())
    k = encrypt(m, e, n)
    print("\nEncrypted message: " + str(k))
    md = decrypt(k, d, n)
    print("Decrypted message: " + str(md))
    print()
