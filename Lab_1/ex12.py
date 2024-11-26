#se citeste un sir de nr de la tastatura sa se afiseze sirul sortat folosind metoda bubble sort
def bubbles(v):
    n = len(v)  # Obținem lungimea listei
    k = 0
    while not k:
        k = 1
        for i in range(1, n):  # Corectat pentru a evita accesarea v[-1]
            if v[i - 1] > v[i]:
                # Schimbăm elementele
                v[i - 1], v[i] = v[i], v[i - 1]
                k = 0

# Citim lungimea și elementele listei de la utilizator
n = int(input("Introduceti lungimea sirului: "))
v = []  # Inițializăm o listă goală
print("Introduceti elementele sirului: ")

for i in range(n):
    element = int(input())  # Citim fiecare element
    v.append(element)  # Adăugăm elementul în listă

# Sortăm lista folosind sortarea Bubble Sort
bubbles(v)

# Afișăm lista sortată
print("Sirul sortat este: ")
print(" ".join(map(str, v)))  # Afișăm elementele listei separate prin spațiu
