
##################################################
#  Python Operator
##################################################

# https://github.com/apache/airflow/blob/master/airflow/operators/python_operator.py




##################################################
#  S3 to Redshift Operator
##################################################

# https://github.com/apache/airflow/blob/master/airflow/operators/s3_to_redshift_operator.py

from typing import List, Optional, Union

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.utils.decorators import apply_defaults

