import unittest
from person import Person

class Test(unittest.TestCase):
    def test_init(self):
        p = Person("yanmp", 22)
        self.assertEqual(p.name, "yanmp" ,"属性赋值有误")

    def test_getAge(self):
        p = Person("yanmp", 22)
        self.assertEqual(p.getName(), p.name, "getName函数有误")

if __name__ == "__main__":
    unittest.main()
