#Determina produsul primelor 10 nr naturale.
# Inițializăm variabila produs la 1
produs = 1

# Parcurgem numerele de la 1 la 10 și le înmulțim
for numar in range(1, 11):
    produs *= numar

# Afișăm produsul
print("Produsul primelor 10 numere naturale este:", produs)

