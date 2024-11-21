# Classe Testo deve poter vedere sia testo codificato che non

diz_let = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "l", 10: "m", 11: "n", 12: "o", 13: "p", 14: "q", 15: "r", 16: "s", 17: "t", 18: "u", 19: "v", 20: "z"}
diz_num = {}
for numero in diz_let:
    diz_num[diz_let[numero]] = numero  # creo dizionario opposto

class Testo:
    def __init__(self, testo, chiave, codifica):
        self.testo = testo
        self.chiave = chiave
        self.codifica = codifica

    def cifra_cod(self):
        if not self.codifica:
            lista_chiave = [diz_num[c] for c in self.chiave]
            cifra = []
            for k, c in enumerate(self.testo):
                cifra.append((diz_num[c] + lista_chiave[k]) % 21)
            self.codifica = True
            print(cifra)
        else:
            print("La stringa è già cifrata")
            
    def decod(self):
        if self.codifica:
            lista_chiave = [diz_num[c] for c in self.chiave]
            testo_decodificato = []
            for k, c in enumerate(self.testo):
                testo_decodificato.append(diz_let[(diz_num[c] - lista_chiave[k]) % 21])
            self.codifica = False
            print("".join(testo_decodificato))
        else:
            print("La stringa non è cifrata")

def main():
    str_input = input("Inserire una stringa: ")
    chiave = input("Inserire la chiave per cifrare: ")

    # Creiamo un oggetto Testo e cifriamo il testo
    testo_codificato = Testo(str_input, chiave, codifica=False)
    testo_codificato.cifra_cod()
    
    # Ora decodifichiamo
    testo_codificato.decod()

if __name__ == "__main__":
    main()
