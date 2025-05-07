print ("Calculadora de resultados y cuadrádos de la suma de dos números enteros\n")
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))
suma = a + b
cuadrado = (a**2 + 2*a*b + b**2)
Op = str(input ("Presiona S para ver el la suma de tus dígitos y C para ver su cuadrado: "))

if (Op == "s" or Op == "S"):
    print (suma)

elif (Op == "C" or Op == "c"):
        print (cuadrado)

else: print ("Ingresa una de las letras sugeridas.")

print ("\nThanks for using.")

