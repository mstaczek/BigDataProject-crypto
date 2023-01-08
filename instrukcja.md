# Kroki do otworzenia

## Mateusz

1. Pliki `crypto_rates_api_to_master.xml` i `crypto_rates_master_to_hive.xml` mają schmaty nifi do pobierania wartości kryptowalut

2. Wgrać dane:

    * Importing Hive table
        
        * data in `hive_exported_table.zip`
        
        * copy folder in the zip file into VM, for example `/home/vagrant/`

        * create folder in HDFS, for example: `/user/vagrant/projekt/imported_hive_table`
        
        * copy from VM to HDFS. In /user/vagrant/projekt/imported_hive_table/ there is _metadata and 2 folders. hdfs dfs -copyFromLocal /home/vagrant/hive_exported_table/* /user/vagrant/projekt/imported_hive_table/

        * Import into a new table called crypto_rates_2 - This should take around 15 minutes. IMPORT TABLE crypto_rates_2 FROM '/user/vagrant/projekt/imported_hive_table/';

## Patryk

1. Plik `get_crypto_news_data.xml` ma schemat nifi do pobierania wiadomości

2. Wrzućić do `/home/vagrant/` pliki `spark_job.sh` i `transform_crypto_news.py`

3. W HBase zrobić tabelkę `create 'crypto_news', 'data', 'lang', 'count'`

4. Poustawiać zmienne środowiskowe (niektóre na podstawie `transform_crypto_news.py`)

5. Zainstalować moduł NLP -> pip install spark-nlp==4.2.6 \ spark-shell --packages com.johnsnowlabs.nlp:spark-nlp_2.12:4.2.6
