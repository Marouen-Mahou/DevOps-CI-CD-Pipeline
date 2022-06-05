import sqlite3

from flask_restful import Resource, reqparse
from flask import current_app
from functions import Hash

register_post_args = reqparse.RequestParser()
register_post_args.add_argument("username", type=str, help="username is needed!")
register_post_args.add_argument("email", type=str, help="email is needed!")
register_post_args.add_argument("phone", type=str, help="phone is needed!")
register_post_args.add_argument("password", type=str, help="password is needed!")


class Register(Resource):
    def post(self):
        ## Get the request_body
        username = register_post_args.parse_args()["username"]
        email = register_post_args.parse_args()["email"]
        phone = register_post_args.parse_args()["phone"]
        password = Hash('sha256',register_post_args.parse_args()["password"])

        db_connection = current_app.config["DATABASE_CON"]
        cursor = db_connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password, phone) VALUES (?,?,?,?)",
            (username, email, password, phone)
        )

        db_connection.commit()

        user_id = cursor.lastrowid

        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()

        cursor.execute(
            "SELECT * FROM users where user_id =?", (user_id,)
        )

        data = cursor.fetchone()
        dict_data = dict(data)
        return {
            'user_id': dict_data['user_id'],
            'username': dict_data['username'],
            'email': dict_data['email'],
            'phone': dict_data['phone']
        }

class Login(Resource):
    def post(self):
        ## Get the request_body
        email = register_post_args.parse_args()["email"]
        password = Hash('sha256',register_post_args.parse_args()["password"])

        db_connection = current_app.config["DATABASE_CON"]

        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()

        cursor.execute(
            "SELECT * FROM users where email =?", (email,)
        )

        data = cursor.fetchone()

        if data == None:
            return {
                "message":"Wrong email"
            }

        dict_data = dict(data)

        if dict_data['password'] == password:
            return {
                "message": "Logged in"
            }

        return {
                "message": "Wrong password"
            }

