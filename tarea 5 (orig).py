# Iniciamos el arreglo con 5 elementos
precipit = [0.0] * 5

# Leemos los datos de precipitación y los almacenamos en el arreglo
for i in range(5):
    while True:
        valor = float(input("Introduzca la cantidad de precipitación para el día" + str(i+1) + ":"))
        if valor >= 0:
            precipit[i] = valor
            break
        else:
            print("Valor inválido. Debe ser mayor o igual a 0.")