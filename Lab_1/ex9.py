#deter daca un an citit de la tastatura  este bisect
# Citim anul de la utilizator
an = int(input("Introduceti un an: "))

# Verificăm dacă anul este bisect
if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print(an, "este an bisect.")
else:
    print(an, "nu este an bisect.")
