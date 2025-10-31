# RSA Decryption with Chinese Remainder Theorem (CRT)

## 1. Objective
Implement and compare two RSA decryption methods:
- **Standard RSA decryption:** `x = y^d mod n`
- **CRT-optimized RSA decryption:** compute two smaller exponentiations modulo `p` and `q`, then recombine via the **Chinese Remainder Theorem**.


## 2. Source Code
All required functions are implemented in **`rsa_crt.py`**:

| Function | Purpose |
|---|---|
| `rsa_decrypt(y, d, n)` | Standard RSA decryption |
| `rsa_decrypt_crt(y, d, p, q)` | RSA decryption accelerated with CRT |

**Run:**
```bash
python rsa_crt.py
```


## 3. Test Results

### (a) Small Primes

**Parameters**

* `p = 11`, `q = 13`, `n = 143`, `e = 7`, `d = 103`, `y = 15`

**Results**

| Method       | Decrypted Result |
| ------------ | ---------------- | 
| Standard RSA | 141              |
| CRT RSA      | 141              |



### (b) Large Primes

**Parameters**

* `p = 12345678901234567890123456869`
* `q = 98765432109876543210987654323`
* `e = 65537`
* `d = 183037555140763297287823421841341095154128759392745892977`
* `y = 12345678901234567890`

**Results**

| Method       | Decrypted Result (truncated) |
| ------------ | ---------------------------- | 
| Standard RSA | 324309952877571399564352792629998816095895977177801581031                  |
| CRT RSA      | 324309952877571399564352792629998816095895977177801581031                 |


