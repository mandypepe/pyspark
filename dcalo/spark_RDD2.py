from pyspark import SparkConf, SparkContext
sc = SparkContext(master='local',appName="HOME")
#red from file
rdd_file = sc.textFile("/home/file.txt")

#writhe to file
rdd_file.saveAsTextFile("/dbfs/FileStore/tables/RDD_dir")