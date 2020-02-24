# -*- coding: utf-8 -*-

import pytest

from pyspark.sql import SparkSession, dataframe

import pandas as pd
from irisexercise.basic_stats import get_stats, get_plot

import matplotlib.pyplot as plt
from matplotlib import figure

def test_df_type():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    iris = pd.read_csv(url, names=names)
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    df = spark.createDataFrame(iris)

    assert isinstance(get_stats(df), dataframe.DataFrame)
    
def test_get_plot():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    iris = pd.read_csv(url, names=names)
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    df = spark.createDataFrame(iris)

    assert isinstance(get_plot(df), figure.Figure)

#TO DO
#Break out data frame creation into initialization function
