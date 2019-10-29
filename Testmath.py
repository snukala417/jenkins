import unittest
import math
class Testmath(unittest.TestCase):
    def test_add(self):
      A = maths.maths()
      x = A.add(10,2)
      self.assertEqual(x,12)

    def test_sub(self):
      A = maths.maths()
      x = A.sub(10,2)
      self.assertEqual(x,8)

    def test_mul(self):
      A = maths.maths()
      x = A.mul(10,2)
      self.assertEqual(x,20)
     

if __name__ == '__main__': 
    unittest.main() 
