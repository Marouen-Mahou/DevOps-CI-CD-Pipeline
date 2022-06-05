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


class EncryptDES(Resource):
    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        key = encrypt_post_args.parse_args()["key"]
        key = key.encode('ascii')
        if len(key) < 16:
            key = key + str.encode((16 - len(key)) * '\x00')
        m = hashlib.md5(key)
        key = m.digest()
        (dk, iv) = (key[:8], key[8:])
        cipher = DES.new(dk, DES.MODE_CBC, iv)
        message += '\x00' * (8 - len(message) % 8)
        ciphertext = cipher.encrypt(message.encode('ascii'))
        encode_string = base64.b32encode(ciphertext)
        return encode_string.decode("utf-8")


class EncryptAES(Resource):
    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        key = encrypt_post_args.parse_args()["key"]
        message = self._pad(message)

        iv = Random.new().read(AES.block_size)

        key = hashlib.sha256(key.encode()).digest()


        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = base64.b64encode(iv + cipher.encrypt(message.encode()))

        return encrypted.decode("utf-8")


class EncryptRSA(Resource):

    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        pubKey = encrypt_post_args.parse_args()["key"]
        encryptor = PKCS1_OAEP.new(pubKey)
        encrypted = encryptor.encrypt(bytes(message, 'utf-8'))
        out=binascii.hexlify(encrypted)

        return out


class EncryptGamal(Resource):

    def post(self):
        message = encrypt_post_args.parse_args()["message"]
        pubKey = encrypt_post_args.parse_args()["key"]
        cipher = elgamal.encrypt(pubKey, message)

        return cipher

