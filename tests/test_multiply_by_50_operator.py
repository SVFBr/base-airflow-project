from datetime import datetime
from unittest.case import TestCase

from airflow import DAG
from airflow.models import TaskInstance

from operators.multply_by_50_operator_sample import MultiplyBy5Operator


class TestMultiplyBy5Operator(TestCase):

    def test_execute_okay(self):
        dag = DAG(dag_id='hello_world', start_date=datetime.now())

        task = MultiplyBy5Operator(my_operator_param=10, dag=dag, task_id='multiplyby5_task')
        ti = TaskInstance(task=task, execution_date=datetime.now())
        result = task.execute(ti.get_template_context())
        self.assertEqual(result, 500)

    def test_execute_nOkay(self):
        dag = DAG(dag_id='hello_world', start_date=datetime.now())

        task = MultiplyBy5Operator(my_operator_param=10, dag=dag, task_id='multiplyby5_task')
        ti = TaskInstance(task=task, execution_date=datetime.now())
        result = task.execute(ti.get_template_context())
        self.assertNotEquals(result, 10)

