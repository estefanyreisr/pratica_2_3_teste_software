# tests/test_loader_test.py — Seção 6
from miniunit import TestCase, TestSuite, TestLoader
from tests.test_case_test import TestStub, TestSpy

class TestLoaderTest(TestCase):
    def test_create_suite(self):
        loader = TestLoader()
        suite = loader.make_suite(TestStub)
        assert len(suite.tests) == 3

    def test_create_suite_of_suites(self):
        loader = TestLoader()
        stub_suite = loader.make_suite(TestStub)
        spy_suite = loader.make_suite(TestSpy)
        suite = TestSuite()
        suite.add_test(stub_suite)
        suite.add_test(spy_suite)
        assert len(suite.tests) == 2

    def test_get_multiple_test_case_names(self):
        loader = TestLoader()
        names = loader.get_test_case_names(TestStub)
        assert names == ['test_error', 'test_failure', 'test_success']

    def test_get_no_test_case_names(self):
        class Test(TestCase):
            def foobar(self):
                pass
        loader = TestLoader()
        names = loader.get_test_case_names(Test)
        assert names == []

if __name__ == "__main__":
    from miniunit import TestRunner
    loader = TestLoader()
    suite = loader.make_suite(TestLoaderTest)
    TestRunner().run(suite)  # 4 run, 0 failed, 0 error
