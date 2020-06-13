import unittest
import proxytools

class TestFormatProxy(unittest.TestCase):
    def test_formatproxy(self):
        returned_output = proxytools.formatproxy("162.10.10.10:3128").format_request()
        expected_output = {'http': 'http://162.10.10.10:3128', 'https': 'https://162.10.10.10:3128'}
        self.assertEqual(returned_output, expected_output)




if __name__ == '__main__':
    unittest.main()
    