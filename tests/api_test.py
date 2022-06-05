import unittest
import requests

class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/"

    #POST request to /hash/md5 returns hash of TEST
    def test_1_hash_md5(self):
        message = "TEST"
        r = requests.post("{}/hash/md5".format(ApiTest.API_URL), {"message": message})

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"033bd94b1168d7e4f0d644c3c95e35bf\"\n")

    #POST request to /hash/sha1 returns hash of TEST
    def test_2_hash_sha1(self):
        message = "TEST"
        r = requests.post("{}/hash/sha1".format(ApiTest.API_URL), {"message": message})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"984816fd329622876e14907634264e6f332e9fb3\"\n")

    #POST request to /hash/sha256 returns hash of TEST
    def test_3_hash_sha256(self):
        message = "TEST"
        r = requests.post("{}/hash/sha256".format(ApiTest.API_URL), {"message": message})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2\"\n")

    #POST request to /crack/md5 returns the hashed text TEST
    def test_4_crack_md5(self):
        # When Hash exists
        message = "033bd94b1168d7e4f0d644c3c95e35bf"
        lines = ["Test","Hello","TEST"]
        r = requests.post("{}/crack/md5".format(ApiTest.API_URL), json={"message": message, "lines": lines})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"TEST\"\n")

        # When Hash doesn't exist
        message = "033bd94b1168d7e4f0d644c3c95e35bf"
        lines = ["Test","Hello"]
        r = requests.post("{}/crack/md5".format(ApiTest.API_URL), json={"message": message, "lines": lines})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"Hash not found\"\n")

    #POST request to /crack/sha1 returns the hashed text TEST
    def test_5_crack_sha1(self):
        message = "984816fd329622876e14907634264e6f332e9fb3"
        #When Hash exists
        lines = ["Test","Hello","TEST"]
        r = requests.post("{}/crack/sha1".format(ApiTest.API_URL), json={"message": message, "lines": lines})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"TEST\"\n")

        #When Hash doesn't exist
        lines = ["Test","Hello"]
        r = requests.post("{}/crack/sha1".format(ApiTest.API_URL), json={"message": message, "lines": lines})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"Hash not found\"\n")

    #POST request to /crack/sha256 returns the hashed text TEST
    def test_6_crack_sha256(self):
        message = "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2"

        # When Hash exists
        lines = ["Test","Hello","TEST"]
        r = requests.post("{}/crack/sha256".format(ApiTest.API_URL), json={"message": message, "lines": lines})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"TEST\"\n")

        # When Hash doesn't exist
        lines = ["Test","Hello"]
        r = requests.post("{}/crack/sha256".format(ApiTest.API_URL), json={"message": message, "lines": lines})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"Hash not found\"\n")

    #POST request to /encode/16
    def test_7_encode_decode_16(self):
        message = "Hello World"

        r = requests.post("{}/encode/16".format(ApiTest.API_URL), json={"message": message})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"48656C6C6F20576F726C64\"\n")

        r = requests.post("{}/decode/16".format(ApiTest.API_URL), json={"message": "48656C6C6F20576F726C64"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text.replace('"', '').strip(), message)

    #POST request to /encode/32
    def test_8_encode_decode_32(self):
        message = "Hello World"

        r = requests.post("{}/encode/32".format(ApiTest.API_URL), json={"message": message})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text, "\"JBSWY3DPEBLW64TMMQ======\"\n")

        r = requests.post("{}/decode/32".format(ApiTest.API_URL), json={"message": "JBSWY3DPEBLW64TMMQ======"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text.replace('"', '').strip(), message)

    #POST request to /encode/64
    def test_9_encode_decode_64(self):
        message = "Hello World"

        r = requests.post("{}/encode/64".format(ApiTest.API_URL), json={"message": message})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text.replace('"', '').strip(), "SGVsbG8gV29ybGQ=")

        r = requests.post("{}/decode/64".format(ApiTest.API_URL), json={"message": r.text})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.text.replace('"', '').strip(), message)

if __name__ == '__main__':
    unittest.main()