import unittest
from unittest.mock import patch

from functions import Crack, Hash, Encode, Decode


class UnitTest(unittest.TestCase):

    #TEST CRACK FUNCTION with md5 type
    def test_1_crack_md5(self):
        #When exists
        message = "033bd94b1168d7e4f0d644c3c95e35bf"
        lines = ["Test", "Hello", "TEST"]
        expected = "TEST"

        result = Crack('md5', message, lines)
        self.assertEqual(expected, result)

        #When doesn't exist
        message = "033bd94b1168d7e4f0d644c3c95e35bf"
        lines = ["Test", "Hello"]
        expected = "Hash not found"

        result = Crack('md5', message, lines)
        self.assertEqual(expected, result)


    # TEST CRACK FUNCTION with sha1 type
    def test_2_crack_sha1(self):
        # When exists
        message = "984816fd329622876e14907634264e6f332e9fb3"
        lines = ["Test", "Hello", "TEST"]
        expected = "TEST"

        result = Crack('sha1', message, lines)
        self.assertEqual(expected, result)

        # When doesn't exist
        message = "984816fd329622876e14907634264e6f332e9fb3"
        lines = ["Test", "Hello"]
        expected = "Hash not found"

        result = Crack('sha1', message, lines)
        self.assertEqual(expected, result)

    # TEST CRACK FUNCTION with sha256 type
    def test_3_crack_sha256(self):
        # When exists
        message = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"
        lines = ["Test", "Hello", "TEST"]
        expected = "TEST"

        result = Crack('sha256', message, lines)
        self.assertEqual(expected, result)

        # When doesn't exist
        message = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"
        lines = ["Test", "Hello"]
        expected = "Hash not found"

        result = Crack('sha256', message, lines)
        self.assertEqual(expected, result)

    # TEST CRACK FUNCTION with wrong type
    def test_4_crack_wrongType(self):
        # When exists
        message = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"
        lines = ["Test", "Hello", "TEST"]
        expected = "Invalid Type"

        result = Crack('sha512', message, lines)
        self.assertEqual(expected, result)

    # TEST HASH FUNCTION with sha256 type
    def test_5_hash_md5(self):
        message = "TEST"
        expected = "033bd94b1168d7e4f0d644c3c95e35bf"

        result = Hash('md5', message)
        self.assertEqual(expected, result)

    # TEST HASH FUNCTION with sha256 type
    def test_6_hash_sha1(self):
        message = "TEST"
        expected = "984816fd329622876e14907634264e6f332e9fb3"

        result = Hash('sha1', message)
        self.assertEqual(expected, result)

    # TEST HASH FUNCTION with sha256 type
    def test_7_hash_sha256(self):
        message = "TEST"
        expected = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"

        result = Hash('sha256', message)
        self.assertEqual(expected, result)

    # TEST HASH FUNCTION with invalid type
    def test_8_hash_invalid(self):
        message = "TEST"
        expected = "Invalid Type"

        result = Hash('sha512', message)
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()