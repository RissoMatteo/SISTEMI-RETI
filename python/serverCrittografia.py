import socket
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

# Funzione per eseguire il processo RSA
def processo_rsa(p, q):
    # Calcola n = p * q
    n = p * q
    
    # Calcola m = mcm(p-1, q-1)
    m = mcm(p - 1, q - 1)
    
    # Trova c tale che mcd(c, m) = 1
    c = trova_c(m)
    
    # Trova d tale che (c * d) mod m = 1
    d = trova_d(c, m)
    
    return c, n, d

# Configurazione del server
def server():
    p = 61  # esempio di numero primo
    q = 53  # esempio di numero primo

    c, n, d = processo_rsa(p, q)  # Generazione delle chiavi
    
    # Creazione del socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))  # Bind al localhost sulla porta 5000
    server_socket.listen(1)  # Ascolta per una connessione
    
    print("Server in ascolto...")
    
    # Accetta la connessione dal client
    client_socket, client_address = server_socket.accept()
    print(f"Connessione ricevuta da {client_address}")
    
    # Invia la chiave pubblica al client (n, c)
    client_socket.send(f"{n},{c}".encode())
    
    # Ricevi il messaggio cifrato dal client
    encrypted_message = client_socket.recv(1024)
    encrypted_message = list(map(int, encrypted_message.decode().split(',')))  # Decodifica i numeri
    
    # Decifra il messaggio
    decrypted_message = decifra_messaggio(encrypted_message, d, n)
    print(f"Messaggio decifrato: {decrypted_message}")
    
    # Chiude la connessione
    client_socket.close()

# Esegui il server
if __name__ == "__main__":
    server()
