from flask import Flask
from flask_restful import Api, Resource
from flask_socketio import SocketIO

from encode import Encode16, Encode32, Encode64
from decode import Decode16, Decode32, Decode64

from encrypt import EncryptDES, EncryptAES, EncryptRSA, EncryptGamal
from decrypt import DecryptDES, DecryptAES, DecryptRSA, DecryptGamal

from hashing import HashMD5, HashSHA1, HashSHA256
from cracking import CrackMD5, CrackSHA1, CrackSHA256

from authentification import Register, Login

from attacks import Attacks

import os
import sqlite3


def create_app(name):
    app = Flask(__name__)
    api = Api(app)
    app.config['SECRET_KEY'] = 'INSAT'

    database_filename = os.environ.get('DATABASE_FILENAME', 'pentracker.db')
    db_connection = sqlite3.connect(database_filename, check_same_thread=False)

    app.config.from_mapping(
        DATABASE_CON=db_connection
    )

    api.add_resource(Encode16, "/encode/16")
    api.add_resource(Encode32, "/encode/32")
    api.add_resource(Encode64, "/encode/64")

    api.add_resource(Decode16, "/decode/16")
    api.add_resource(Decode32, "/decode/32")
    api.add_resource(Decode64, "/decode/64")

    api.add_resource(EncryptDES, "/encrypt/des")
    api.add_resource(EncryptAES, "/encrypt/aes")
    api.add_resource(EncryptRSA, "/encrypt/rsa")
    api.add_resource(EncryptGamal, "/encrypt/gamal")

    api.add_resource(DecryptDES, "/decrypt/des")
    api.add_resource(DecryptAES, "/decrypt/aes")
    api.add_resource(DecryptRSA, "/decrypt/rsa")
    api.add_resource(DecryptGamal, "/decrypt/gamal")

    api.add_resource(HashMD5, "/hash/md5")
    api.add_resource(HashSHA1, "/hash/sha1")
    api.add_resource(HashSHA256, "/hash/sha256")

    api.add_resource(CrackMD5, "/crack/md5")
    api.add_resource(CrackSHA1, "/crack/sha1")
    api.add_resource(CrackSHA256, "/crack/sha256")

    api.add_resource(Register, "/register")
    api.add_resource(Login, "/login")

    api.add_resource(Attacks, "/attacks")
    return app


if __name__ == "__main__":
    app = create_app(__name__)
    socketio = SocketIO(app)
    socketio.run(app)

