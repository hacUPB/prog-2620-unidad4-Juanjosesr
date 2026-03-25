from random import randint

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

lista = []

for i in range(12):
    dato = randint(20,80)
    lista.append(dato)

print(lista)

mayor = max(lista)
mes = lista.index(mayor)

print(f"Se vendieron más autos en {meses[mes]}")
print(f"Se vendieron {mayor} autos")


# ocho = lista.count(8)
# print(f"El número 8 se repite {ocho} veces")