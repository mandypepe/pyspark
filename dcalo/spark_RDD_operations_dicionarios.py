from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")

#Visualizar un diccionario
a = sc.parallelize(['a','b','c','a'])
b = sc.parallelize([1,2,3,4])
rdd_kv = a.zip(b)
print (rdd_kv.collect())

#Ver las llaves del dic
print (rdd_kv.keys().collect())

# ver los valores del dic
print (rdd_kv.values().collect())

# multiplicar*2  con lambda los valores del un dic
print (rdd_kv.mapValues(lambda x : x*2).collect())

#Sumar por llave los valores de un diccionario
print (dd_kv.reduceByKey(lambda x,y: x + y).collect())

#ordenar  por valores
print (rdd_kv.sortByKey(False).collect())

#Ordenar por llaves
print (rdd_kv.sortByKey(True).collect())
