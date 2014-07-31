import os, sys
import random
import random1
import unittest

class TestRandom1(unittest.TestCase):
    def setUp(self):
        self.random1_instance = random1.Random1()
    
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_pass1(self):
        self.assertEqual(10, 7+3)

    def test_pass2(self):
        self.assertNotEqual(10, random.randint(0,9))

    #def test_fail(self):
    #    self.assertEqual(10, 7+4, "this is not equal")

    def test_returnBanner(self):
        self.assertEqual("Hello Jenkins", self.random1_instance.returnBanner())

if __name__ == "__main__":
    unittest.main()
