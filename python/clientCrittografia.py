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

# Funzione per cifrare un messaggio (intero)
def cifra(a, c, n):
    return pow(a, c, n)

# Funzione per cifrare un intero (messaggio) in una stringa
def cifra_messaggio(messaggio, c, n):
    return [cifra(ord(carattere), c, n) for carattere in messaggio]

# Funzione per gestire l'interazione con il server
def client():
    # Connessione al server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))  # Connettersi al server sulla porta 5000
    
    # Ricevi la chiave pubblica (n, c)
    public_key = client_socket.recv(1024).decode()
    n, c = map(int, public_key.split(','))
    print(f"Chiave pubblica ricevuta: (n = {n}, c = {c})")
    
    # Chiedi al client di inserire un messaggio
    message = input("Inserisci una frase da cifrare: ")
    
    # Cifra il messaggio
    encrypted_message = cifra_messaggio(message, c, n)
    encrypted_message_str = ','.join(map(str, encrypted_message))  # Converte la lista in stringa
    
    # Invia il messaggio cifrato al server
    client_socket.send(encrypted_message_str.encode())
    
    # Chiude la connessione
    client_socket.close()

# Esegui il client
if __name__ == "__main__":
    client()
