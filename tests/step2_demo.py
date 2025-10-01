# tests/step2_demo.py — demo simples da Seção 2
from miniunit import TestCase

class MyTest(TestCase):
    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

if __name__ == "__main__":
    MyTest("test_a").run()
    MyTest("test_b").run()
