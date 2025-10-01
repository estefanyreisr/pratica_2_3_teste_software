# tests/step3_demo.py — demonstra TestResult
from miniunit import TestCase, TestResult

class TestStub(TestCase):
    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception("boom")

if __name__ == "__main__":
    result = TestResult()
    TestStub("test_success").run(result)
    TestStub("test_failure").run(result)
    TestStub("test_error").run(result)
    print(result.summary())  # 3 run, 1 failed, 1 error
