#ec gr 2
import math

# Citim coeficientii de la utilizator
a = float(input("Introduceți coeficientul a: "))
b = float(input("Introduceți coeficientul b: "))
c = float(input("Introduceți coeficientul c: "))

# Calculăm discriminantul
D = b**2 - 4 * a * c

# Verificăm discriminantul pentru a determina soluțiile
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)  # Prima soluție
    x2 = (-b - math.sqrt(D)) / (2 * a)  # A doua soluție
    print(f"Soluțiile ecuației sunt: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)  # Soluția dublă
    print(f"Soluția dublă a ecuației este: x = {x}")
else:
    print("Ecuația nu are soluții reale.")
