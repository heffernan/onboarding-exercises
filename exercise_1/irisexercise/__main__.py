#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:23:40 2020

"""

from pyspark.sql import SparkSession

import pandas as pd
from irisexercise.basic_stats import get_stats, get_plot

def main():
	url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
	names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
	iris = pd.read_csv(url, names=names)

	print('this')

	spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
	df = spark.createDataFrame(iris)

	get_stats(df).show()
	get_plot(df).show()

	print('end')
	
if __name__ == "__main__":
	main()

