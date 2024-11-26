#se citesc 3 nr de la tastatura sa se afiseze un mesaj daca acestea pot reprezenta unghiurile unui triunghi.

# Citim unghiurile de la utilizator
a = int(input("Introduceți unghiul a: "))  # Citim unghiul a
b = int(input("Introduceți unghiul b: "))  # Citim unghiul b
c = int(input("Introduceți unghiul c: "))  # Citim unghiul c

# Verificăm dacă suma unghiurilor este 180
if a + b + c == 180:
    print("Da, numerele pot reprezenta unghiurile unui triunghi")  
else:
    print("Nu, numerele pot reprezenta unghiurile unui triunghi")  
