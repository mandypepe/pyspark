
from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")
# order first 5 element
print (rdd.takeOrdered(5))

# ordenar de reversa los 5 primeros elementos
print(rdd.takeOrdered(5, lambda x: -x))

# order all eRDD
rdd_aux = rdd.sortBy(lambda x: x)
print(rdd_aux.collect())

# order reverse  RDD and return all  RDD
rdd_aux = rdd.sortBy(lambda x:-x)
print(rdd_aux.collect())

