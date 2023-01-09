# Analysis of cryptocurrency exchange rates in regard to published news articles

## Repository for version control of files for Big Data project

Project is about using Apache NiFi and other Big Data tools to gather and analyze data about cryptocurrencies. This data is then analysed together with the results of NLP analysis of news articles that are related to cryptocurrencies.

## Setup (part)
All `.xml` are to be imported into Nifi. Files `transform_crypto_news.py` and `spark_job.sh` must be placed in the `/home/vagrant/` directory.
Additionally, a table in HBase needs to be created, as follows:
```
create 'crypto_news', 'data', 'lang', 'count'
```
