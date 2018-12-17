from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")

#RDD Creación a partir de colecciones Python
lista = ['uno','dos','dos','tres','cuatro']
listardd = sc.parallelize(lista)
listardd = sc.parallelize(lista,4) # Incluir el número de cluster en lo que dividir el RDD
print(listardd.collect()) # Visualizar la colección RDD

#Creación a partir de diccionarios
dicRDD = sc.parallelize([("autor","Fernando de Rojas"),
                         ("titulo","La celestina"),
                         ("anio",1499)]) # Importantes los corchetes []
print(dicRDD.collect()) # Visualizar la colección RDD

#Creación a partir de diccionarios 2
a = sc.parallelize(['a','b','c','a'])
b = sc.parallelize([1,2,3,4])
rdd_kv = a.zip(b)
print (rdd_kv.collect())

