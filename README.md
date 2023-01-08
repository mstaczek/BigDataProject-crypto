# Gathering and analysis of cryptocurrency exchange rate
data

## Repository for version control of files for Big Data project

Project is about using Apache NiFi and other Big Data tools to gather and analyze data about cryptocurrencies. This data is compared with the results of NLP analysis of various news articles that are related to cryptocurrencies.

## Setup
All `.xml` are to be imported into Nifi. Files `transform_crypto_news.py` and `spark_job.sh` must be placed in the `/home/vagrant/` directory.
Additionally, a table in HBase needs to be created, as follows:
```
create 'crypto_news', 'data', 'lang', 'count'
```