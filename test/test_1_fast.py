from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest
import time

from src.main import task_one
from test.test_logger import TestLogger

SUMMARY_TEST_LOG_FILE = "./test_results/task_1/test_summary.txt"
DETAILS_TEST_LOG_FILE = "./test_results/task_1/test_details.txt"


class TaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results(SUMMARY_TEST_LOG_FILE, DETAILS_TEST_LOG_FILE)

    def test_task_one(self):
        input_path = "./tests_input/numbers.txt"

        numbers = []
        with open(input_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                numbers.append(int(line))

        amount = len(numbers)
        sum_of_numbers = 0
        for number in numbers:
            sum_of_numbers += number
        expected_min = sorted(numbers)[0]
        expected_max: int = sorted(numbers)[amount - 1]
        expected_avg = sum_of_numbers / amount
        start = time.time()
        result = task_one()
        end = time.time()
        duration = end - start

        passed = expected_min == result[0]
        passed = passed and expected_max == result[1]
        passed = passed and expected_avg == result[2]

        TaskTest.logger.log_single_test_result("test_task_one_simple_test", passed, duration)
        self.assertEqual(expected_min, result[0])
        self.assertEqual(expected_max, result[1])
        self.assertEqual(expected_avg, result[2])


if __name__ == '__main__':
    unittest.main()
