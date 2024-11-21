import ipaddress

# Funzione per calcolare la wildcard mask
def calcola_wildcard_mask(subnet_mask):
    wildcard = ipaddress.IPv4Address(int(ipaddress.IPv4Address(subnet_mask)) ^ 0xFFFFFFFF)
    return wildcard

# Funzione per calcolare i dati per ogni VLAN all'interno della stessa rete
def calcola_vlan(indirizzo_iniziale, cidr_iniziale, dispositivi):
    num_ip_necessari = dispositivi + 2  # Aggiungiamo 2 per l'indirizzo di rete e broadcast

    # Calcola il numero di bit necessari per ospitare il numero di dispositivi richiesti
    for subnet_size in range(32, cidr_iniziale, -1):
        if 2 ** (32 - subnet_size) >= num_ip_necessari:
            subnet_size = 32 - (32 - subnet_size)
            break

    # Crea la subnet con il CIDR calcolato
    rete = ipaddress.IPv4Network(f"{indirizzo_iniziale}/{subnet_size}", strict=False)

    # Calcola indirizzi di rete, broadcast, primo e ultimo IP utile
    indirizzo_network = rete.network_address
    indirizzo_broadcast = rete.broadcast_address
    primo_ip_utile = indirizzo_network + 1
    ultimo_ip_utile = indirizzo_broadcast - 1
    subnet_mask = rete.netmask
    wildcard_mask = calcola_wildcard_mask(subnet_mask)

    return {
        'indirizzo_network': indirizzo_network,
        'indirizzo_broadcast': indirizzo_broadcast,
        'subnet_mask': subnet_mask,
        'wildcard_mask': wildcard_mask,
        'primo_ip_utile': primo_ip_utile,
        'ultimo_ip_utile': ultimo_ip_utile,
        'next_start_ip': indirizzo_broadcast + 1  # Prossimo IP di partenza
    }

# Funzione principale
def main():
    # Input iniziale
    indirizzo_iniziale = input("Inserisci l'indirizzo di partenza (es. 192.168.1.0): ")
    cidr = int(input("Inserisci la barra (es. 24): "))
    numero_vlans = int(input("Inserisci il numero di VLAN: "))

    # Creiamo una lista per contenere i dettagli delle VLAN
    vlans = []
    for i in range(numero_vlans):
        print(f"\nInserisci i dettagli per la VLAN {i+1}:")
        nome_vlan = input(f"Inserisci il nome della VLAN {i+1}: ")
        dispositivi_vlan = int(input(f"Inserisci il numero di dispositivi per la VLAN {i+1}: "))
        vlans.append({
            'nome': nome_vlan,
            'dispositivi': dispositivi_vlan
        })

    # Ordiniamo le VLAN per numero di dispositivi, dal maggiore al minore
    vlans.sort(key=lambda x: x['dispositivi'], reverse=True)

    # Per ogni VLAN, calcoliamo le informazioni di rete
    start_ip = indirizzo_iniziale
    for i, vlan in enumerate(vlans):
        print(f"\nCalcolo per VLAN {i+1} ({vlan['nome']}):")
        vlan_info = calcola_vlan(start_ip, cidr, vlan['dispositivi'])
        
        # Stampa i risultati per la VLAN corrente
        print(f"Indirizzo di rete: {vlan_info['indirizzo_network']}")
        print(f"Indirizzo broadcast: {vlan_info['indirizzo_broadcast']}")
        print(f"Subnet mask: {vlan_info['subnet_mask']}")
        print(f"Wildcard mask: {vlan_info['wildcard_mask']}")
        print(f"Primo IP utile: {vlan_info['primo_ip_utile']}")
        print(f"Ultimo IP utile: {vlan_info['ultimo_ip_utile']}")
        
        # Aggiorna l'indirizzo di partenza per la prossima VLAN
        start_ip = vlan_info['next_start_ip']

if __name__ == "__main__":
    main()
