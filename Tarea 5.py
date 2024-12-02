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

# Calculamos el total de lluvia
total_lluvia = 0.0
for lluvia in precipit:
    total_lluvia += lluvia

# Calculamos el promedio
promedio = total_lluvia / len(precipit)

# Encontramos el máximo y el mínimo
maximo = precipit[0]
minimo = precipit[0]
for lluvia in precipit:
    if lluvia > maximo:
        maximo = lluvia
    if lluvia < minimo:
        minimo = lluvia

# Ordenamiento por burbuja
for i in range(len(precipit) - 1):
    for j in range(len(precipit) - i - 1):
        if precipit[j] < precipit[j+1]:
            precipit[j], precipit[j+1] = precipit[j+1], precipit[j]


# Imprimimos los resultados
print("Total de lluvia en el periodo registrado:", total_lluvia)
print("Promedio de lluvia por día:", promedio)
print("Máximo de lluvia registrado en el periodo:", maximo)
print("Mínimo de lluvia registrado en el periodo:", minimo)
print("Valores de lluvia por día, ordenados de mayor a menor:", precipit)