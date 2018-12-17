from operator import add
from pyspark import SparkConf, SparkContext


sc = SparkContext(master='local',appName="HOME")

#Crear un RDD que multiplique por 2 sus valores y sumar los resultados
rdd = sc.parallelize([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
rdd2 = rdd.map(lambda x: x*2)
tSum = rdd2.reduce(lambda x,y: x+y)
print (tSum)

#Crear un diccionario con elementos (x,1) y sumar las apariciones por elemento

rdd_text = sc.parallelize(['red', 'red', 'blue', 'green', 'green','yellow'])
rdd_aux = rdd_text.map(lambda x: (x,1))
rdd_result = rdd_aux.reduceByKey(lambda x,y: x+y)
print (rdd_result.collect())