#3. sa se afiseze primele 10 de nr impare
# Inițializăm o listă pentru numerele impare
numere_impare = []

# Parcurgem numerele de la 1 la 20 (suficient pentru a obține primele 10 numere impare)
for numar in range(1, 20, 2):
    numere_impare.append(numar)

# Afișăm primele 10 numere impare
print("Primele 10 numere impare sunt:", numere_impare)
