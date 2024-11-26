#Se citesc 5 numere de la tastatura sa se afiseze  cel mai mare numar
# Inițializăm o listă pentru a stoca cele 5 numere
numere = []

# Citim 5 numere de la utilizator
print("Introduceți 5 numere:")
for i in range(5):
    numar = float(input(f"Numărul {i + 1}: "))  # Citim fiecare număr
    numere.append(numar)  # Adăugăm numărul în listă

# Găsim cel mai mare număr folosind funcția max()
cel_mai_mare = max(numere)
 
# Afișăm cel mai mare număr
print("Cel mai mare număr este:", cel_mai_mare)
