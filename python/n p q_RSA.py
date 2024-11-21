#Questo esercizio implementa un programma in Python che utilizza il multithreading per trovare due numeri primi, 𝑝 e 𝑞
#tali che il loro prodotto sia uguale a un numero n dato dall'utente.

import math
import threading

# Funzione per controllare se un numero è primo
def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Funzione per trovare due numeri primi p e q tali che p * q = n
def trova_fattori_primi_multithread(n, result):
    def cerca_fattore_in_thread(start, end):
        for p in range(start, end):
            if is_primo(p) and n % p == 0:
                q = n // p
                if is_primo(q):
                    result.append((p, q))
                    return

    threads = []
    num_threads = 4  # Numero di thread da utilizzare
    chunk_size = int(math.sqrt(n)) // num_threads

    for i in range(num_threads):
        start = 2 + i * chunk_size
        end = 2 + (i + 1) * chunk_size if i < num_threads - 1 else int(math.sqrt(n)) + 1
        thread = threading.Thread(target=cerca_fattore_in_thread, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Esempio di utilizzo
n = int(input("Inserisci un numero: "))
result = []
trova_fattori_primi_multithread(n, result)

if result:
    p, q = result[0]
    print(f"I due numeri primi p e q tali che p * q = {n} sono: {p} e {q}")
else:
    print("Non è possibile trovare due numeri primi p e q tali che p * q = n.")
