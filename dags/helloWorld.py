from airflow import DAG
from airflow.operators import PythonOperator, DummyOperator
from datetime import datetime, timedelta

def hello():
    print('hello world')

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 9, 27),
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}

dag = DAG('hello_world', default_args=default_args)

task1 = DummyOperator(task_id='Start_task',dag=dag)
task2 = PythonOperator(task_id='Hello_task',python_callable=hello,dag=dag)
task3 = DummyOperator(task_id='End_task',dag=dag)\

task1 >> [task2, task3]
