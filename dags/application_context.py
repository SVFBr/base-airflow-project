import os

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

ROOT_PATH = os.path.abspath(os.path.join(ABS_PATH, os.pardir))
DAGS_PATH = ROOT_PATH + "/dags"
MOCKS_PATH = ROOT_PATH + "/tests/mocks"
DAGS_TESTS_ROOT_PATH = ROOT_PATH + "/tests/dags"
