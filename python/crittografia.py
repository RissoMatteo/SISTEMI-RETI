import math

# Funzione per calcolare il MCM (minimo comune multiplo)
def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Funzione per trovare un valore c tale che 1 < c < m e mcd(c, m) = 1
def trova_c(m):
    for c in range(2, m):
        if math.gcd(c, m) == 1:
            return c
    return None

# Funzione per trovare l'inverso di c modulo m (ovvero d)
def trova_d(c, m):
    def euclide_esteso(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = euclide_esteso(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y
    g, x, y = euclide_esteso(c, m)
    if g != 1:
        raise Exception("Non esiste l'inverso")
    else:
        return x % m

# Funzione per cifrare un messaggio (intero)
def cifra(a, c, n):
    return pow(a, c, n)

# Funzione per decifrare un messaggio (intero)
def decifra(b, d, n):
    return pow(b, d, n)

# Funzione per cifrare un intero (messaggio) in una stringa
def cifra_messaggio(messaggio, c, n):
    return [cifra(ord(carattere), c, n) for carattere in messaggio]

# Funzione per decifrare un messaggio cifrato (lista di numeri)
def decifra_messaggio(messaggio_cifrato, d, n):
    return ''.join([chr(decifra(b, d, n)) for b in messaggio_cifrato])

# Funzione principale che esegue l'intero processo RSA
def processo_rsa(p, q, a):
    # 2. Calcola n = p * q
    n = p * q
    
    # 3. Calcola m = mcm(p-1, q-1)
    m = mcm(p - 1, q - 1)
    
    # 4. Trova c tale che mcd(c, m) = 1
    c = trova_c(m)
    
    # 5. Trova d tale che (c * d) mod m = 1
    d = trova_d(c, m)
    
    # 6. Stampa delle chiavi pubblica e privata
    print(f"Chiave pubblica: (n = {n}, c = {c})")
    print(f"Chiave privata: (p = {p}, q = {q}, m = {m}, d = {d})")
    
    # 7. Cifra il messaggio intero
    b = cifra(a, c, n)
    print(f"Messaggio originale: {a}")
    print(f"Messaggio cifrato: {b}")
    
    # 8. Decifra il messaggio intero
    messaggio_decifrato = decifra(b, d, n)
    print(f"Messaggio decifrato: {messaggio_decifrato}")
    
    return c, n, d

# Funzione per gestire la cifratura di una frase
def gestisci_input_messaggio():
    messaggio_input = input("Inserisci una frase da cifrare: ")
    
    # 9. Cifrare la frase
    messaggio_cifrato = cifra_messaggio(messaggio_input, c, n)
    print(f"Messaggio cifrato (in numeri): {messaggio_cifrato}")
    
    # 10. Decifrare la frase
    messaggio_decifrato = decifra_messaggio(messaggio_cifrato, d, n)
    print(f"Messaggio decifrato: {messaggio_decifrato}")

p = 61  #numero primo
q = 53  #numero primo
a = 200  #messaggio (intero)
# Esecuzione del processo RSA
c, n, d = processo_rsa(p, q, a)
# Gestione della cifratura e decifratura della frase
gestisci_input_messaggio()
