import hashlib
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




