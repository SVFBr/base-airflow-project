import unittest
from unittest.case import TestCase

from airflow.models import DagBag
from application_context import DAGS_PATH


class TestHelloWorldDAG(TestCase):
    dag_id = 'hello_world'

    def setUp(self):
        self.dagbag = DagBag(
            dag_folder=DAGS_PATH
        )

    def test_task_count(self):
        dag = self.dagbag.get_dag(self.dag_id)
        self.assertEqual(len(dag.tasks), 3)

    def test_contain_tasks(self):
        dag = self.dagbag.get_dag(self.dag_id)
        tasks = dag.tasks
        task_ids = list(map(lambda task: task.task_id, tasks))
        self.assertListEqual(task_ids, ['dummy_task', 'hello_task', 'multiplyby5_task'])

    @unittest.skip
    def test_dependencies_of_dummy_task(self):
        dag = self.dagbag.get_dag(self.dag_id)
        dummy_task = dag.get_task('dummy_task')

        upstream_task_ids = list(map(lambda task: task.task_id, dummy_task.upstream_list))
        self.assertListEqual(upstream_task_ids, [])
        downstream_task_ids = list(map(lambda task: task.task_id, dummy_task.downstream_list))
        self.assertListEqual(sorted[downstream_task_ids], sorted['hello_task', 'multiplyby5_task'])

    def test_dependencies_of_hello_task(self):
        dag = self.dagbag.get_dag(self.dag_id)
        hello_task = dag.get_task('hello_task')

        upstream_task_ids = list(map(lambda task: task.task_id, hello_task.upstream_list))
        self.assertListEqual(upstream_task_ids, ['dummy_task'])
        downstream_task_ids = list(map(lambda task: task.task_id, hello_task.downstream_list))
        self.assertListEqual(downstream_task_ids, [])


suite = unittest.TestLoader().loadTestsFromTestCase(TestHelloWorldDAG)
unittest.TextTestRunner(verbosity=2).run(suite)
