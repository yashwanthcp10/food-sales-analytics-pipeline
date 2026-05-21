from airflow import DAG

from airflow.operators.python import (
    PythonOperator
)

from datetime import datetime

from src.orchestration.run_pipeline import (
    run_pipeline
)

default_args = {

    "owner": "yashwanth",

    "start_date": datetime(
        2025,
        1,
        1
    ),

    "retries": 2
}


dag = DAG(

    dag_id="food_sales_pipeline",

    default_args=default_args,

    schedule_interval="0 2 2 * *",

    catchup=False
)


pipeline_task = PythonOperator(

    task_id="run_pipeline_task",

    python_callable=run_pipeline,

    op_kwargs={

        "file_path":
        "data/incoming/January_23.xlsx"

    },

    dag=dag
)