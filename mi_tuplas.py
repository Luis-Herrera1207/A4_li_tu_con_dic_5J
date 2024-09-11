print("--Ejemplo de tuplas--")
canciones=("te amo","El NoNoa","amor eterno")
print(canciones)
y = list(canciones)
print(y)
y[1] = "La puerta negra"
x = tuple(y)
print(x)
print("--Listado de elementos de la tupla canciones con ciclo for--")
for herrera in canciones:
    print(herrera)