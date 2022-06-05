import sqlite3
from functions import All_Attacks

from flask import current_app

from flask_restful import Resource, reqparse



class Attacks(Resource):

    def get(self):
        db_connection = current_app.config["DATABASE_CON"]

        db_connection.row_factory = sqlite3.Row
        cursor = db_connection.cursor()

        cursor.execute(
            "SELECT * FROM attacks"
        )
        attacks = All_Attacks(cursor)

        return {
            "data": attacks
        }

