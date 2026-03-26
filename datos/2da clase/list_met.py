from random import randint

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

lista = []

for i in range(12):
    dato = randint(20,80)
    lista.append(dato)

print(lista)

mayor = max(lista)
veces = lista.count(mayor)

if veces > 1:
    lista_meses = []
    for i in range(len(lista)):
        if lista [i] == mayor:
            lista_meses.append(i)
    print("Ventas mayores en:")
    for mes in lista_meses:
        print(f" {meses[mes]}")


else: 
    mes = lista.index(mayor)
    print(f"Mayor venta en {meses[mes]}")



# print(f"Se vendieron más autos en {meses[mes]}")
# print(f"El {mayor} está {veces} veces en la lista")
# print(f"Se vendieron {mayor} autos")


# ocho = lista.count(8)
# print(f"El número 8 se repite {ocho} veces")