# tests/test_case_test.py — Seção 4 + atualização da Seção 8 (usa self.assert_*)
from miniunit import TestCase, TestResult

# Dublês
class TestStub(TestCase):
    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception


class TestSpy(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.was_run = False
        self.was_set_up = False
        self.was_tear_down = False
        self.log = ""

    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"


class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    def test_result_success_run(self):
        TestStub('test_success').run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 0 failed, 0 error')

    def test_result_failure_run(self):
        TestStub('test_failure').run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 1 failed, 0 error')

    def test_result_error_run(self):
        TestStub('test_error').run(self.result)
        self.assert_equal(self.result.summary(), '1 run, 0 failed, 1 error')

    def test_result_multiple_run(self):
        TestStub('test_success').run(self.result)
        TestStub('test_failure').run(self.result)
        TestStub('test_error').run(self.result)
        self.assert_equal(self.result.summary(), '3 run, 1 failed, 1 error')

    def test_was_set_up(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_set_up)

    def test_was_run(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_run)

    def test_was_tear_down(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_true(spy.was_tear_down)

    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        self.assert_equal(spy.log, "set_up test_method tear_down")

    # ---------- Testes dos asserts (Seção 8) ----------
    def test_assert_true(self):
        self.assert_true(True)

    def test_assert_false(self):
        self.assert_false(False)

    def test_assert_equal(self):
        self.assert_equal("", "")
        self.assert_equal("foo", "foo")
        self.assert_equal([], [])
        self.assert_equal(['foo'], ['foo'])
        self.assert_equal((), ())
        self.assert_equal(('foo',), ('foo',))
        self.assert_equal({}, {})
        self.assert_equal({'foo'}, {'foo'})

    def test_assert_in(self):
        animals = {'monkey': 'banana', 'cow': 'grass', 'seal': 'fish'}
        self.assert_in('a', 'abc')
        self.assert_in('foo', ['foo'])
        self.assert_in(1, [1, 2, 3])
        self.assert_in('monkey', animals)


# Runner simples desta seção (opcional para rodar diretamente este arquivo)
if __name__ == "__main__":
    result = TestResult()
    for name in [
        'test_result_success_run',
        'test_result_failure_run',
        'test_result_error_run',
        'test_result_multiple_run',
        'test_was_set_up',
        'test_was_run',
        'test_was_tear_down',
        'test_template_method',
        'test_assert_true',
        'test_assert_false',
        'test_assert_equal',
        'test_assert_in',
    ]:
        TestCaseTest(name).run(result)
    print(result.summary())  # esperado: 12 run, 0 failed, 0 error
