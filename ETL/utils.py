# Description: This file contains the utility functions for the ETL processes.

import pandas as pd
import numpy as np
import os
from pyspark.sql import SparkSession

def create_sparksession():
    """
    Initialize Spark Session
    """
    return SparkSession.builder \
        .appName('airflow_demo') \
        .config('spark.sql.sources.partitionColumnTypeInference.enabled', 'false') \
        .config('spark.sql.parquet.compression.codec', 'snappy') \
        .getOrCreate()

def read_csv(spark, path, header=True, inferSchema=True):
    """
    Read CSV file into Spark DataFrame
    """
    return spark.read.csv(path, header=header, inferSchema=inferSchema)
