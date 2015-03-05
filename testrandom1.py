import os, sys
import random
import random1
import unittest

class TestRandom1(unittest.TestCase):
    def setUp(self):
        self.random1_instance = random1.Random1()
    
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        print "Test skipped"
        self.fail("shouldn't happen")

    def test_pass1(self):
        print "Test 1"
        self.assertEqual(10, 7+3)

    def test_pass2(self):
        print "Test 2"
        self.assertNotEqual(10, random.randint(0,9))

    def test_fail(self):
        print "Test 3"
        self.assertEqual(10, 7+4, "this is not equal")

    def test_returnBanner(self):
        print "Test 4"
        self.assertEqual("Hello Jenkins", self.random1_instance.returnBanner())

    def tearDown(self):
        del self.random1_instance

if __name__ == "__main__":
    unittest.main()
