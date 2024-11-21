#calcolare x^y mod p
def potenza_mod(x, y, p):
    return pow(x, y, p)

# Parametri pubblici
p = 23  # Numero primo
g = 5   # Generatore

# 1. Scelta delle chiavi private (a e b) per Alice e Bob
a = 6  # Chiave privata di Alice
b = 15 # Chiave privata di Bob

# 2. Calcolo delle chiavi pubbliche
A = potenza_mod(g, a, p)  # Chiave pubblica di Alice
B = potenza_mod(g, b, p)  # Chiave pubblica di Bob

# 3. Scambio delle chiavi pubbliche

# 4. Calcolo della chiave segreta condivisa
chiave_alice = potenza_mod(B, a, p) # Alice usa la chiave pubblica di Bob e la sua chiave privata
chiave_bob = potenza_mod(A, b, p) # Bob usa la chiave pubblica di Alice e la sua chiave privata

# Stampa delle chiavi
print(f"Chiave pubblica di Alice: {A}")
print(f"Chiave pubblica di Bob: {B}")
print(f"Chiave segreta condivisa calcolata da Alice: {chiave_alice}")
print(f"Chiave segreta condivisa calcolata da Bob: {chiave_bob}")

# Verifica che le chiavi segrete siano uguali
if chiave_alice == chiave_bob:
    print("Le chiavi segrete corrispondono!")
else:
    print("Le chiavi segrete non corrispondono!")
