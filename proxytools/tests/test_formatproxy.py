import unittest
import proxytools

class TestFormatProxy(unittest.TestCase):
    def test_formatproxy_noauth(self):
        returned_output = proxytools.formatproxy("162.10.10.10:3128").format_request()
        expected_output = {'http': 'http://162.10.10.10:3128', 'https': 'https://162.10.10.10:3128'}
        self.assertEqual(returned_output, expected_output)
    def test_formatproxy_auth(self):
        returned_output = proxytools.formatproxy("162.10.10.10:3128:username:password").format_request()
        expected_output = {'http': 'http://username:password@162.10.10.10:3128', 'https': 'https://username:password@162.10.10.10:3128'}
        self.assertEqual(returned_output, expected_output)




if __name__ == '__main__':
    unittest.main()
    