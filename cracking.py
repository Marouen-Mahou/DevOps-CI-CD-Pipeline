from flask_restful import Resource, reqparse
from flask import request
from functions import Crack

encode_post_args = reqparse.RequestParser()
encode_post_args.add_argument("message", type=str, help="Message to be encoded")


class CrackMD5(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        lines= request.json["lines"]

        return Crack("md5",message,lines)


class CrackSHA1(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        lines = request.json["lines"]
        return Crack("sha1",message,lines)


class CrackSHA256(Resource):
    def post(self):
        message = encode_post_args.parse_args()["message"]
        lines= request.json["lines"]
        return Crack("sha256",message,lines)
