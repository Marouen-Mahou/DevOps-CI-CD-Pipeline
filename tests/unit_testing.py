import unittest
from unittest.mock import patch

from flask import current_app

from functions import Crack, Hash, Encode, Decode, All_Attacks

import sqlite3

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


    # TEST ENCODE FUNCTION with 16 base
    def test_9_encode_16(self):
        message = "Hello World"
        expected = "48656C6C6F20576F726C64"

        result = Encode("16",message)

        self.assertEqual(expected, result)

    # TEST ENCODE FUNCTION with 32 base
    def test_10_encode_32(self):
        message = "Hello World"
        expected = "JBSWY3DPEBLW64TMMQ======"

        result = Encode("32",message)

        self.assertEqual(expected, result)

    # TEST ENCODE FUNCTION with 64 base
    def test_11_encode_64(self):
        message = "Hello World"
        expected = "SGVsbG8gV29ybGQ="

        result = Encode("64", message)

        self.assertEqual(expected, result)

    # TEST ENCODE FUNCTION with invalid Type
    def test_12_encode_invalid(self):
        message = "Hello World"
        expected = "Invalid Type"

        result = Encode("125", message)

        self.assertEqual(expected, result)

    # TEST DECODE FUNCTION with 16 base
    def test_13_decode_16(self):
        message = "48656C6C6F20576F726C64"
        expected = "Hello World"

        result = Decode("16",message)

        self.assertEqual(expected, result)

    # TEST DECODE FUNCTION with 32 base
    def test_14_decode_32(self):
        message = "JBSWY3DPEBLW64TMMQ======"
        expected = "Hello World"

        result = Decode("32",message)

        self.assertEqual(expected, result)

    # TEST DECODE FUNCTION with 64 base
    def test_15_decode_64(self):
        message = "SGVsbG8gV29ybGQ="
        expected = "Hello World"

        result = Decode("64", message)

        self.assertEqual(expected, result)

    # TEST ENCODE FUNCTION with invalid Type
    def test_16_decode_invalid(self):
        message = "SGVsbG8gV29ybGQ="
        expected = "Invalid Type"

        result = Decode("125", message)

        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()