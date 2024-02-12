# Test Dag to run an example Job

from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

gen_dag = DAG(
    dag_id='test_dag',
    default_args=default_args,
    schedule_interval=None
)

# Spark Job Example
spark_example_job = SparkSubmitOperator(
    task_id='spark_example_job',
    dag=gen_dag,
    application='ETL/spark_example.py',
    conn_id='spark_conn'
)

gen_start = PythonOperator(
    task_id='gen_start',
    python_callable=lambda: print('Start - Test Pipeline'),
    dag=gen_dag
)



gen_end = PythonOperator(
    task_id='gen_end',
    python_callable=lambda: print('Ended Successfully - Test Pipeline'),
    dag=gen_dag
)

gen_start >> gen_end