from airflow import DAG
from airflow.provider.http.sensors.http import HttpSensor
from datetime import datetime, timedelta
import json

api_key = open("../keys/weather.txt", "r").readline()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 8),
    'email': ['juliolimolisilva@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    'weather_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
    ) as dag:

    is_weather_api_ready = HttpSensor(
        task_id='is_weather_api_ready',
        http_conn_id='weathermap_api',
        endpoint=f'/data/2.5/weather?q=Antwerp&appid={api_key}'
    )