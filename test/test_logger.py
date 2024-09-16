from datetime import datetime


class TestLogger:

    def __init__(self):
        self.results = dict()

    def log_single_test_result(self, test_name, passed, time):
        self.results[test_name] = (passed, time)

    def save_results(self, summary_file_path, details_file_path):
        self.save_summary_result(summary_file_path)
        self.save_detailed_results(details_file_path)

    def save_summary_result(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            overall_test_result = all(map(lambda x: x[0] is True, self.results.values()))
            file.write(f"TASK COMPLETED: {overall_test_result}\n")
            passed_tests_count = sum(map(lambda x: x[0] is True, self.results.values()))
            file.write(f"PASSED TESTS: {passed_tests_count} OF {len(self.results)}\n")

    def save_detailed_results(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            for key, value in self.results.items():
                file.write(f"{datetime.now()};{key};{value[0]};{round(value[1], 3)}\n")
