from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")

# Filtering  Numeric RDD
rdd_num = sc.parallelize([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
rdd_num = rdd.filter(lambda x : x < 3)
print (rdd_num.collect())

#Filterin by TEXT RDD
rdd_text = sc.parallelize(['Delete entry lines', '', '', '', '','No more'])
rdd_aux = rdd_text.filter(lambda x : x != '')
print (rdd_aux.collect())
