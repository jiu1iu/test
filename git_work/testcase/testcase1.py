import unittest
import HTMLTestRunner
class Unittest_case01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有的潜质条件')

    @classmethod
    def tearDownClass(cls):
        print('所有的后置')

    def setUp(self):
        self.a = 1
        print('潜质条件')

    def tearDown(self):
        self._out
        print('后置条件')

    def test001(self):
        print('第一个case')
        self.assertEqual(2, self.a, 'sdf')

    def test002(self):
        print('第二个case')
        self.assertNotEqual(2, self.a, 'llkk')

if __name__ == "__main__":
    flie_path = 'E:/gitcode/git_work/report/first_case.html'
    f = open(flie_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(Unittest_case01("test002"))
    suite.addTest(Unittest_case01("test001"))

    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='sss', description='aaa', verbosity=2)
    runner.run(suite)
