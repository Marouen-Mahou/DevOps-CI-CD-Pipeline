from flask_restful import Resource, reqparse
from functions import Encode

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class Encode16(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = Encode("16", message)
        return {"text":output}


class Encode32(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = Encode("32", message)
        return {"text":output}


class Encode64(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        output = Encode("64", message)
        return {"text":output}
