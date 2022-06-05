from flask_restful import Resource, reqparse
from Crypto.Cipher import DES, AES, PKCS1_OAEP
import hashlib
import base64
import binascii
from Crypto import Random
import elgamal

encrypt_post_args = reqparse.RequestParser()
encrypt_post_args.add_argument("message", type=str, help="Message to be encrypted")
encrypt_post_args.add_argument("key", type=str, help="Key")


class DecryptDES(Resource):
    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        key = encrypt_post_args.parse_args()["key"]
        key = key.encode('ascii')
        if len(key) < 16:
            key = key + str.encode((16 - len(key)) * '\x00')
        m = hashlib.md5(key)
        key = m.digest()
        (dk, iv) = (key[:8], key[8:])
        decoded_string = base64.b32decode(message)
        cipher2 = DES.new(dk, DES.MODE_CBC, iv)
        decrypted_string = cipher2.decrypt(decoded_string)
        return decrypted_string.decode("utf-8")


class DecryptAES(Resource):
    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        key = encrypt_post_args.parse_args()["key"]
        message = base64.b64decode(message)
        iv = message[:AES.block_size]
        key = hashlib.sha256(key.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_text = self._unpad(cipher.decrypt(message[AES.block_size:])).decode('utf-8')

        return plain_text


class DecryptRSA(Resource):

    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        keypair = encrypt_post_args.parse_args()["key"]
        decryptor = PKCS1_OAEP.new(keypair)
        decrypted = decryptor.decrypt(binascii.unhexlify(message))
        return decrypted

class DecryptGamal(Resource):

    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        privateKey = encrypt_post_args.parse_args()["key"]
        cipher = elgamal.decrypt(privateKey, message)
        return cipher

