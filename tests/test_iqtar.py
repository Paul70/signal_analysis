import unittest
from iq import iqtar

class TestIqTar(unittest.TestCase):
    def test_init(self):
        test_filename = 'tests/data/dummy.iq.tar'
        iqtar_file = iqtar.IqTar(test_filename)
        self.assertEqual(iqtar_file.iqtar.filename, test_filename)

    def test_getSampleRate(self):
        test_filename = 'tests/data/dummy.iq.tar'
        iqtar_data = iqtar.IqTar(test_filename)
        self.assertEqual(10000.0, iqtar_data.getSampleRate())

    def test_getNofSamples(self):
        test_filename = 'tests/data/dummy.iq.tar'
        iqtar_data = iqtar.IqTar(test_filename)
        self.assertEqual(2, iqtar_data.getNofSamples())        
        

if __name__ == '__main__':
    unittest.main()