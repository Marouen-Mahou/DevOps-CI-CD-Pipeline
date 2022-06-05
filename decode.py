from flask_restful import Resource, reqparse
from functions import Decode

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class Decode16(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = Decode("16", message)
        return {"text": output}


class Decode32(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = Decode("32", message)
        return {"text": output}


class Decode64(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = Decode("64", message)
        return {"text": output}
