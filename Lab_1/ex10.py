#scrieti un program care det suma si media unor sume de nr citite de la tastatura (med aritmetica)
# Citim numărul de valori de la utilizator
n = int(input("Introduceți câte numere doriți să adunați: "))
s = 0  # Inițializăm suma

# Parcurgem numerele de la 1 la n
for i in range(1, n + 1):
    a = int(input(f"Introduceți numărul {i}: "))  # Citim numărul de la utilizator
    s += a  # Adunăm numărul la sumă

# Calculăm media aritmetică
ma = s / n  # Nu este necesar să convertim suma la float, rezultatul va fi un float

# Afișăm media și suma
print(f"Media aritmetică este: {ma}, Suma este: {s}")
