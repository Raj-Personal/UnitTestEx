import unittest as ut
import cal

class TestCal(ut.TestCase):

    def test_add(self):
        result=cal.add(10,5)
        self.assertEqual(result,15)

    def test_sub(self):
        result=cal.sub(10,5)
        self.assertEqual(result,5)

    def test_mul(self):
        result=cal.mul(10,5)
        self.assertEqual(result,50)

    def test_div(self):
        self.assertEqual(cal.div(10,5),2)
        self.assertRaises(ValueError,cal.div,10,0)

        with self.assertRaises(ValueError):
            cal.div(10,0)


if __name__ =='__main__':
    unittest.main()