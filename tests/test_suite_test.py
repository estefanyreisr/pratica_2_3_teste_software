# tests/test_suite_test.py — Seção 5
from miniunit import TestCase, TestResult, TestSuite
from tests.test_case_test import TestStub  # reutiliza o dublê

class TestSuiteTest(TestCase):
    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        assert len(suite.tests) == 3

    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.run(result)
        assert result.summary() == '1 run, 0 failed, 0 error'

    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        suite.run(result)
        assert result.summary() == '3 run, 1 failed, 1 error'

if __name__ == "__main__":
    result = TestResult()
    for name in ['test_suite_size', 'test_suite_success_run', 'test_suite_multiple_run']:
        TestSuiteTest(name).run(result)
    print(result.summary())  # 3 run, 0 failed, 0 error
