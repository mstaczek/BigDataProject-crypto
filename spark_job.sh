#!/bin/bash
HADOOP_USER_NAME=root /usr/local/spark/bin/spark-submit --packages com.johnsnowlabs.nlp:spark-nlp_2.12:4.2.6 transform_crypto_news.py $1 &> spark_log.txt