#
import numpy as np
matrix_aux = [[1,2,3],[4,5,6]]
m = np.array(matrix_aux)

#matriz de ceros
l = np.zeros((3, 3))
print(l)

#matriz de 1
l = np.ones([3,3])
print(l)

# binary array
l = np.diag([1,1,1])
print(l)

#Acceder a elementos de la matriz
print(m[1,1])
print(m[:,2])
print(m[0,:])
print(m[0,::-1])

#Sumar todos los elementos array
print(m.sum())
#Sumar de una fila de la matriz
print(m[0,:].sum())
#Aplanar una matrix hacerla un array
print(m.flatten())

#Concat matriz 2
print( np.concatenate((m,m), axis=0) )
print( np.concatenate((m,m), axis=1) )

#Operaciones aritméticas
#Tienen la peculiaridad de broadcasting o
# redifusión, que consite en que si una de las dimensiones a
# la hora de aplicar la operación no tiene una dimensión correcta
# pero es unitaria se redifusiona hasta completar la matriz.

m = np.array([[1,2,3],
     [4,5,6]])
v = np.array([[1,2,3]])
print( m * v)