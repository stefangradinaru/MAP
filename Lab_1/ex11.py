#faceti un vector de elemente de tip string si afisati elementele
# Creăm o listă de elemente de tip string
vector = []

print("Introduceți elemente de tip string (apăsați 'Enter' fără a scrie nimic pentru a încheia):")

while True:
    element = input()  # Citim elementul de la utilizator
    if element == '':  # Dacă utilizatorul apasă 'Enter' fără a introduce nimic, ieșim din buclă
        break
    vector.append(element)  # Adăugăm elementul în listă

# Afișăm elementele din listă
print("\nElementele din vector sunt:")
for elem in vector:
    print(elem)

