from flask import Flask
from flask_restful import Api, Resource
from flask_socketio import SocketIO

from hashing import HashMD5, HashSHA1, HashSHA256
from cracking import CrackMD5, CrackSHA1, CrackSHA256



def create_app(name):
    app = Flask(__name__)
    api = Api(app)
    app.config['SECRET_KEY'] = 'INSAT'

    api.add_resource(HashMD5, "/hash/md5")
    api.add_resource(HashSHA1, "/hash/sha1")
    api.add_resource(HashSHA256, "/hash/sha256")

    api.add_resource(CrackMD5, "/crack/md5")
    api.add_resource(CrackSHA1, "/crack/sha1")
    api.add_resource(CrackSHA256, "/crack/sha256")

    return app


if __name__ == "__main__":
    app = create_app(__name__)
    socketio = SocketIO(app)
    socketio.run(app)

