import unittest
import coolify as cl

class Test_coolify(unittest.TestCase):
    def test_name(self):
        name = "kev"
        self.assertTrue(cl.coolify(name) == "kev")
        self.assertFalse(cl.coolify(name) == "kev is cool")

if __name__ == '__main__':
    unittest.main()