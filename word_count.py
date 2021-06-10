# hdfs dfs -put heart_failure_clinical_records_dataset.csv /tmp

from __future__ import print_function
import sys, re
from operator import add
from pyspark.sql import SparkSession

spark = SparkSession\
  .builder\
  .appName("PythonWordCount")\
  .getOrCreate()

# Access the file
lines = spark.read.text("/tmp/heart_failure_clinical_records_dataset.csv").rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(' ')) \
  .map(lambda x: (x, 1)) \
  .reduceByKey(add) \
  .sortBy(lambda x: x[1], False)
output = counts.collect()
for (word, count) in output:
  print("%s: %i" % (word, count))

spark.stop()