# miniunit/__init__.py — Seção 3 (TestResult integrado ao TestCase)

class TestResult:
    RUN_MSG = 'run'
    FAILURE_MSG = 'failed'
    ERROR_MSG = 'error'

    def __init__(self, suite_name=None):
        self.run_count = 0
        self.failures = []
        self.errors = []

    def test_started(self):
        self.run_count += 1

    def add_failure(self, test_name):
        self.failures.append(test_name)

    def add_error(self, test_name):
        self.errors.append(test_name)

    def summary(self):
        return f"{self.run_count} {self.RUN_MSG}, " \
               f"{len(self.failures)} {self.FAILURE_MSG}, " \
               f"{len(self.errors)} {self.ERROR_MSG}"


class TestCase:
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result: TestResult):
        result.test_started()
        self.set_up()
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()
        except AssertionError:
            result.add_failure(self.test_method_name)
        except Exception:
            result.add_error(self.test_method_name)
        finally:
            self.tear_down()
            
            
class TestSuite:
    def __init__(self):
        self.tests = []
    def add_test(self, test):
        self.tests.append(test)
    def run(self, result: TestResult):
        for test in self.tests:
            test.run(result)

