#determinati daca un nr de la tastatura e prim
# Citim un număr de la utilizator
n = int(input("Introduceți un număr întreg: "))

k = 1  # Variabila pentru a verifica dacă numărul este prim

# Verificăm dacă numărul este prim
for i in range(2, n // 2 + 1):
    if n % i == 0:
        print("nu e prim")
        k = 0
        break

if k == 1 and n > 1:  # Verificăm dacă k este 1 și numărul este mai mare de 1
    print("prim")
elif n == 1:  # 1 nu este considerat număr prim
    print("1 nu e prim")
