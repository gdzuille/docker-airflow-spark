FROM apache/airflow:2.7.1-python3.11

USER root

RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-17-jdk && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr
RUN export JAVA_HOME

USER airflow

# Installs needed packages, not using Poetry due to incompatibility issues, will be fixed in the future
RUN pip install apache-airflow apache-airflow-providers-apache-spark pyspark findspark apache-airflow-providers-mongo apache-airflow-providers-microsoft-mssql 