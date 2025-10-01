# tests/run_all.py — Seção 7
from miniunit import TestSuite, TestLoader, TestRunner
from tests.test_case_test import TestCaseTest
from tests.test_suite_test import TestSuiteTest
from tests.test_loader_test import TestLoaderTest

if __name__ == "__main__":
    loader = TestLoader()
    case_suite = loader.make_suite(TestCaseTest)
    suite_suite = loader.make_suite(TestSuiteTest)
    loader_suite = loader.make_suite(TestLoaderTest)

    master = TestSuite()
    master.add_test(case_suite)
    master.add_test(suite_suite)
    master.add_test(loader_suite)

    TestRunner().run(master)  # 15 run, 0 failed, 0 error
