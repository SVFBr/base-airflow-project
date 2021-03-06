import logging

from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin

log = logging.getLogger(__name__)


class MultiplyBy5Operator(BaseOperator):
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(MultiplyBy5Operator, self).__init__(*args, **kwargs)

    def execute(self, context):
        return self.operator_param * 50


class MultiplyBy5Plugin(AirflowPlugin):
    name = "multiplyby5_plugin"
