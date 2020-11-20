def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if (a * x) % m == 1:
            return x
    return 1

def encrypt(text, k, a, n):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            x = ord(char) - 65
            y = (k * x + a) % n + 65
            result += chr(y)
        else:
            x = ord(char) - 97
            y = (k * x + a) % n + 97
            result += chr(y)

    return result

def decrypt(text, k, a, n):
    result = ""

    kInv = modInverse(k, n)

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            y = ord(char) - 65
            x = (kInv * (y + n - a) % n) + 65
            result += chr(x)
        else:
            y = ord(char) - 97
            x = (kInv * (y + n - a) % n) + 97
            result += chr(x)

    return result


encrypted = encrypt("NIGHT", 3, 5, 26)
decrypted = decrypt(encrypted, 3, 5, 26)

print(encrypted)
print(decrypted)