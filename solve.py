def rsa_decrypt(y, d, n):
    """Standard RSA decryption: x = y^d mod n"""
    return pow(y, d, n)


def rsa_decrypt_crt(y, d, p, q):
    """RSA decryption accelerated by Chinese Remainder Theorem (CRT)"""
    n = p * q

    # Step 1: Compute dp, dq
    dp = d % (p - 1)
    dq = d % (q - 1)

    # Step 2: Compute xp, xq
    xp = pow(y % p, dp, p)
    xq = pow(y % q, dq, q)

    # Step 3: Compute cp, cq (modular inverses)
    cp = pow(q, -1, p)
    cq = pow(p, -1, q)

    # Step 4: Recombine results
    x = (q * cp * xp + p * cq * xq) % n
    return x


if __name__ == "__main__":
    p = 12345678901234567890123456869
    q = 98765432109876543210987654323
    n = p * q
    e = 65537
    d = 183037555140763297287823421841341095154128759392745892977
    y = 12345678901234567890

    x_std = rsa_decrypt(y, d, n)

    x_crt = rsa_decrypt_crt(y, d, p, q)

    print("Standard RSA decryption result:", x_std)
    print("CRT RSA decryption result:", x_crt)
    print("Same result?", x_std == x_crt)
