import findspark
findspark.init()
from pyspark.sql import SparkSession
import json
import os
import sys

filename = sys.argv[1]

spark = (
    SparkSession.builder
    .appName("News transformations")
    .config('spark.jars.packages', 'com.johnsnowlabs.nlp:spark-nlp_2.12:4.2.6')
    .getOrCreate()
)

news = (
    spark.read
    .parquet(f'hdfs://localhost:8020/user/vagrant/projekt/masterdataset/crypto_news/{filename}.parquet')
).filter("content is not NULL")

def save_column_family(name, data):
    (
        data.write
        .format("parquet")
        .mode("overwrite")
        .save(f'hdfs://localhost:8020/user/vagrant/projekt/to_process/crypto_news/{filename}__{name}.parquet')
    )
    
import sparknlp
from sparknlp.base import *
from sparknlp.annotator import *
from pyspark.sql.functions import *
from pyspark.ml import Pipeline

def get_sentiment():
    document = DocumentAssembler() \
    .setInputCol("content") \
    .setOutputCol("document")

    token = Tokenizer() \
    .setInputCols(["document"]) \
    .setOutputCol("token")

    normalizer = Normalizer() \
    .setInputCols(["token"]) \
    .setOutputCol("normal")

    vivekn =  ViveknSentimentModel.pretrained() \
    .setInputCols(["document", "normal"]) \
    .setOutputCol("result_sentiment")

    finisher = Finisher() \
    .setInputCols(["result_sentiment"]) \
    .setOutputCols("sentiment")

    pipeline = Pipeline().setStages([document, token, normalizer, vivekn, finisher])

    pipelineModel = pipeline.fit(news.select("content"))
    return pipelineModel.transform(news)

save_column_family("data", get_sentiment().select("link", "title", "source_id", col("pubDate").alias("date"), concat_ws(",",col("sentiment")).alias("sentiment")))

crypto={
    "BTC": ["bitcoin", "BTC"],
    "DOGE": ["dogecoin", "DOGE"],
    "USDT": ["tether", "USDT"],
    "DAI": ["multi-collateral-dai", "DAI"],
    "CRO": ["crypto-com-coin", "CRO"],
    "BNB": ["binance-coin", "BNB"],
    "DASH": ["dash", "DASH"],
    "DVPN": ["sentinel", "DVPN"],
    "QTUM": ["qtum", "QTUM"],
    "ETH": ["ethereum", "ETH"],
    "EOS": ["EOS"],
    "BCH": ["bitcoin-cash", "BCH"],
    "ZEC": ["zcash", "ZEC"],
    "RUNE": ["thorchain", "RUNE"],
    "WAVES": ["waves", "WAVES"],
    "XPRT": ["persistence", "XPRT"],
    "LTC": ["litecoin", "LTC"],
}
for key, val in crypto.items():
    regexp = "|".join(["("+v.replace('-','(-|\\s)')+")" for v in val]).lower()
    news = news.withColumn(f'count_{key}', size(split(col("content"), regexp)) - 1)
    

save_column_family("count", news.select("link", *[f'count_{key}' for key in crypto.keys()]))

save_column_family("lang", news.filter("country is not NULL and language is not NULL").select("link", "language", concat_ws(",",col("country")).alias("country")))