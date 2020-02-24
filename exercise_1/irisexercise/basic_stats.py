#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:22:19 2020

"""
import matplotlib.pyplot as plt

def get_stats(df):
    return df.describe().filter("summary== 'mean'").drop('species')
    
def get_plot(df):
    print('show plot')
    fig, ax = plt.subplots()
    pandas_df = df.toPandas()
    ax.scatter(pandas_df.sepal_length,pandas_df.sepal_width)
    return fig
