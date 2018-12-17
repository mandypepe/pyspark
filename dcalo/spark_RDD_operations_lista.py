from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")
#Visualizar una lista de RDD
rdd = sc.parallelize([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
print (rdd.collect())

# number of element
print (rdd.count())

# first element
print (rdd.first())

#Diccionario con la frecuencia de cada elemento
# cuenta cada uno de los elementos y los retorna {1: 4, 2: 3, 3: 2, 4: 1}) elemento : cantidad , elemento1 : cantidad1
print (rdd.countByValue())

# return  first 4 element
print (rdd.take(4))

# calcular promedio
print (rdd.mean())

# variance varianza
print (rdd.variance())

# deviacion tipica
print (rdd.stdev())