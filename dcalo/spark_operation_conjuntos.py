
from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")
# union
group1 = sc.parallelize(['A','B','C','D'])
group2 = sc.parallelize(['C','D','E','F'])
rdd_aux = group1.union(group2)
print (rdd_aux.collect())

# intersecion
rdd_aux = group1.intersection(group2)
rdd_aux.collect()

