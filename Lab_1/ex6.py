#. sa se creeze un program care determina cel mai mare divizor comun pt 2 nr intregi citite de la tastatura
def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Citim cele două numere de la utilizator
numar1 = int(input("Introduceți primul număr întreg: "))
numar2 = int(input("Introduceți al doilea număr întreg: "))

# Calculăm CMMD
rezultat = cmmdc(numar1, numar2)

# Afișăm rezultatul
print(f"Cel mai mare divizor comun pentru {numar1} și {numar2} este: {rezultat}")

