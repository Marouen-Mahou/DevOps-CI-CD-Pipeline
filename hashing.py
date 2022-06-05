from flask_restful import Resource, reqparse
from functions import Hash

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class HashMD5(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        return Hash("md5",message)


class HashSHA1(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        return Hash("sha1", message)


class HashSHA256(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        return Hash("sha256", message)
