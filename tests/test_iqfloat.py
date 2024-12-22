import unittest
from iq import iqfloat

class TestIqFloat(unittest.TestCase):
    def test_init(self):
        test_filename = 'tests/data/iqsamples.float32'
        float32_file = iqfloat.IqFloat(test_filename)
        self.assertEqual(float32_file.filename, test_filename)        

if __name__ == '__main__':
    unittest.main()