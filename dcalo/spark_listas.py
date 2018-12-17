lista = list()

lista = []

lista = [1, 2, 3, 4]

lista = [1, 2, 'Hola', [3, 4]]

for i in range(len(lista)):
    print(lista[i])

lista.append(5)
print(lista)

lista.append([6,7])
print(lista)
#adiciona los elementos como separados a diferencia del append
lista.extend([8,8,8])
print(lista)

lista.remove(2)
print(lista)

n = lista.count(8)
print(n)
 # find  element in list return position
n = lista.index(1)
print(n)

n = lista.index('Hola')
print(n)

lista.reverse()
print(lista)

#addeding NaN
lista.append(float('NaN'))
print(lista)

# eliminar nulos
import numpy
lista = ['A', 'B', numpy.nan, 'D']
lista = [x for x in lista if str(x) != 'nan']
print(lista)
# delet eduplicate
lista = ['A','B','C','D','A','A']
lista = set(lista)
print(sorted(lista)) # Es necesario ordenarlo

# replace strings
lista = ['pececin','pececillo','pececilla']
lista = [words.replace('pece', 'salmon') for words in lista]
print(lista)

# trim php  eliminar espace ini end
lista = ['pececin ',' pececillo ',' pececilla']
lista = [words.split() for words in lista]
print(lista)

# replace more one space
lista = ['pececin  primero',' pececillo   segundo',' pececilla tercera']
lista = [words.replace('   ', ' ') for words in lista]
lista = [words.replace('  ', ' ') for words in lista]
print(lista)

# dividir valores de lista a entre valores lista b
a = [10,20,30,40,50,60,70,80,90]
b = [10,20,30,40,50,60,70,80,90]
c = [x/y for x, y in zip(a, b)]
print(c)

# calcular prom todos los elementos mayores q 2
import numpy as np

l = np.array([1, 2, 3,5,6, 4])

print( l[l>2] )
print( np.mean(l[l>2]))

