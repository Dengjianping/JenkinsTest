import ctypes, os.path, platform
import unittest


class DLL:
    def __init__(self, path):
        self.dll = ctypes.cdll.LoadLibrary(path)

class SimpleMath(DLL):
    def __init__(self, path):
        DLL.__init__(self, path)

    def sub(self, a, b):
        a = ctypes.c_int(a)
        b = ctypes.c_int(b)
        self.dll.sub.retypes = ctypes.c_int
        result = self.dll.sub(a, b)
        return result

    def add(self, a, b):
        a = ctypes.c_int(a)
        a = ctypes.pointer(a)
        b = ctypes.c_int(b)
        b = ctypes.pointer(b)
        self.dll.add.retypes = ctypes.c_int
        result = self.dll.add(a, b)
        return result

class TestMath(unittest.TestCase):
    def setUp(self):
        test_py_dir = os.path.dirname(os.path.realpath(__file__))
        dll_path = os.path.join(os.path.dirname(test_py_dir), 'build', 'Debug', 'simplemath.dll')
        self.test_dll = SimpleMath(dll_path)

    def testSub(self):
        a, b = 90, 5
        self.assertEqual(85, self.test_dll.sub(a, b))

    @unittest.expectedFailure
    def testSub(self):
        a, b = 90, 5
        self.assertEqual(30, self.test_dll.sub(a, b))

    def testAdd(self):
        a, b = 34, 6
        self.assertEqual(40, self.test_dll.add(a, b))

    def tearDown(self):
        self.test_dll = None


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMath)
    unittest.TextTestRunner(verbosity=2).run(suite1)