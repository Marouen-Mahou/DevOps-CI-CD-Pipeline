import hashlib
import base64
import sqlite3
from flask import current_app


### CRACK FUNCTIONS
def Crack(type, message, lines):
    if(type == 'md5'):
        for line in lines:
            hash_object = hashlib.md5(bytes(line.strip(), encoding='utf-8'))
            if message == hash_object.hexdigest():
                return line
        return "Hash not found"

    if(type == 'sha1'):
        for line in lines:
            hash_object = hashlib.sha1(bytes(line.strip(), encoding='utf-8'))
            if message == hash_object.hexdigest():
                return line
        return "Hash not found"

    if (type == 'sha256'):
        for line in lines:
            hash_object = hashlib.sha256(bytes(line.strip(), encoding='utf-8'))
            if message == hash_object.hexdigest():
                return line
        return "Hash not found"

    return "Invalid Type"

### HASH Functions
def Hash(type, message):
    if(type == 'md5'):
        hash_object = hashlib.md5(bytes(message, encoding='utf-8'))
        return hash_object.hexdigest()

    if (type == 'sha1'):
        hash_object = hashlib.sha1(bytes(message, encoding='utf-8'))
        return hash_object.hexdigest()

    if (type == 'sha256'):
        hash_object = hashlib.sha256(bytes(message, encoding='utf-8'))
        return hash_object.hexdigest()

    return "Invalid Type"


## ENCODE Functions
def Encode(type, message):
    if(type=="16"):
        output = base64.b16encode(message.encode()).decode()
        return output
    if(type=="32"):
        output = base64.b32encode(message.encode()).decode()
        return output
    if(type=="64"):
        output = base64.b64encode(message.encode()).decode()
        return output

    return "Invalid Type"

## DECODE Functions
def Decode(type, message):
    if (type == "16"):
        output = base64.b16decode(message.encode('ascii')).decode('ascii')
        return output
    if (type == "32"):
        output = base64.b32decode(message.encode('ascii')).decode('ascii')
        return output
    if (type == "64"):
        output = base64.b64decode(message.encode('ascii')).decode('ascii')
        return output

    return "Invalid Type"


# Attacks
def All_Attacks(cursor):
    data = cursor.fetchall()

    attacks = []

    for d in data:
        dict_data = dict(d)
        attacks.append({"name": dict_data["name"], "description": dict_data["description"]})

    return attacks



