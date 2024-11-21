lista = ["4o", "4o-Mini", "o1-preview", "o1-Min"]

#c style, da NON usare
for i in range (len(lista)):
    print("ChatGBT" + lista[i])
   
print()
    
#py style, da USARE
for versione in lista:
    print(f"CharGBT {versione}")
   
print()
 
for indice, versione in enumerate(lista):   #enumerate è una funziona, si usa per numerare la lista
    print(f"La versione {indice + 1} di ChatGBT è {versione}")

print()

nomi = ["Giorgis", "Ansa", "Busso", "Ciobi"]

for nome, versione in zip(nomi, lista):   #zip è una funzione che mi affianca le liste
    print(f"{nome} usa ChatGBT {versione}")
    
#se ho liste di dimensioni diverse il ciclo di ferma alla lista più corta "tagliando" la parte rimanente della lista più lunga
    
#nomi.append("Matteo")  append aggiunge un qualcosa
#print(nomi)

print()

print(f"Il primo nome è {nomi[0]}")
print(f"Il penultimo nome è {nomi[-2]}")
print(f"Stampa da 0 a 2 escluso {nomi[0:2]}")
print(f"Stampa tutti i nomi tranne l'ultimo {nomi[0:-1]}")
print(f"Stampa solo gli ultimi 2 {nomi[-2:]}")  
print(f"Stampa i nomi solo in posizione pari {nomi[::2]}") #dopo il secondo ":" scrivo il numero di quanto voglio che salta (2 in 2 in questo casos)