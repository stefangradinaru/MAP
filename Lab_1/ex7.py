#determinati daca un nr de la tastatura e prim 
# Citim numărul de la utilizator
n = int(input("Introduceți un număr întreg: "))
p = 1  # Inițializarea variabilei pentru factorial

# Calculăm factorialul
for i in range(1, n + 1):
    p *= i  # p = p * i

# Afișăm rezultatul
print("Factorialul lui", n, "este:", p)

