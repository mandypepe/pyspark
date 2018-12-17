from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")

rdd = sc.parallelize([1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 32, 34, 45])

#Selecionar una muestra de 5 elementos con repeticion “True”
print(rdd.takeSample(True, 5))
#Selecionar datos con repetición con un tamaño de muestra de el doble
print (rdd.sample(True, 2).collect())

