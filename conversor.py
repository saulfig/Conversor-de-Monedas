valorFinal = int(input("Escoge un numero para convertir : \n1.Mexico \n 2.Dolar \n3.Euro \n4.Libra \n5.Chino \n:"))

PesoDominicanoMexicano = 3.14
PesoDominicanoDolar = 57.5
PesoDominicanoEuro = 62.15
PesoDominicanochino = 7.98 
PesoDominicanolibra = 71.82

valorx = int(input("Ingresa un valor:"))
if valorFinal == 1:
    resultado = valorx / PesoDominicanoMexicano
    print(resultado)
elif valorFinal == 3:
    resultado = valorx / PesoDominicanoEuro
    print(resultado)
elif valorFinal == 5:
    resultado = valorx / PesoDominicanochino
    print(resultado)
elif valorFinal == 4:
    resultado = valorx / PesoDominicanolibra
    print(resultado)
elif valorFinal == 2:
    resultado = valorx / PesoDominicanoDolar
    print(resultado)
