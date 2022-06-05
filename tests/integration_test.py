import pytest
from main import create_app
from utils.create_db import create_db
import os


@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    create_db(database_filename)
    os.environ["DATABASE_FILENAME"] = str(database_filename)


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(__name__)
    testing_client = flask_app.test_client(use_cookies=False)
    context = flask_app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_create_user(test_client):
    # Given
    request_payload = {
        "username": "userTest",
        "phone": "213456",
        "email": "email@gmail.com",
        "password": "Hello"
    }

    expected_body = {
        "user_id": 1,
        "username": "userTest",
        "phone": 213456,
        "email": "email@gmail.com",
    }

    expected_status_code = 200

    expected_body_keys = ["user_id", "username", "phone", "email"]

    # When
    response = test_client.post('/register', json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json | expected_body == response.json
    assert set(expected_body_keys) == response.json.keys()
    assert int == type(response.json["user_id"])


# POST request to /hash/md5 returns hash of TEST
def test_hash_md5(test_client):
    #Given
    request_payload = {
        "message": "TEST",
    }

    expected_status_code = 200

    expected = b'\"033bd94b1168d7e4f0d644c3c95e35bf\"\n'

    #When
    response = test_client.post("/hash/md5", json=request_payload)
    print(response)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected


# POST request to /hash/sha1 returns hash of TEST
def test_2_hash_sha1(test_client):
    # Given
    request_payload = {
        "message": "TEST",
    }

    expected_status_code = 200

    expected = b"\"984816fd329622876e14907634264e6f332e9fb3\"\n"

    # When
    response = test_client.post("/hash/sha1", json=request_payload)
    print(response)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected


# POST request to /hash/sha256 returns hash of TEST
def test_hash_sha256(test_client):
    # Given
    request_payload = {
        "message": "TEST",
    }

    expected_status_code = 200

    expected = b"\"94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2\"\n"

    # When
    response = test_client.post("/hash/sha256", json=request_payload)
    print(response)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected


#POST request to /crack/md5 returns the hashed text TEST
def test_crack_md5_found(test_client):
    # Given
    request_payload = {
        "message": "033bd94b1168d7e4f0d644c3c95e35bf",
        "lines": ["Test", "Hello", "TEST"]
    }

    expected_status_code = 200

    expected = b"\"TEST\"\n"

    # When
    response = test_client.post("/crack/md5", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected

#POST request to /crack/md5 returns the hashed text TEST
def test_crack_md5_not_found(test_client):
    # Given
    request_payload = {
        "message": "033bd94b1168d7e4f0d644c3c95e35bf",
        "lines": ["Test", "Hello"]
    }

    expected_status_code = 200

    expected = b"\"Hash not found\"\n"

    # When
    response = test_client.post("/crack/md5", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected


#POST request to /crack/sha1 returns the hashed text TEST
def test_crack_sha1_found(test_client):
    # Given
    request_payload = {
        "message": "984816fd329622876e14907634264e6f332e9fb3",
        "lines": ["Test", "Hello", "TEST"]
    }

    expected_status_code = 200

    expected = b"\"TEST\"\n"

    # When
    response = test_client.post("/crack/sha1", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected

#POST request to /crack/sha1 returns the hashed text TEST
def test_crack_sha1_not_found(test_client):
    # Given
    request_payload = {
        "message": "984816fd329622876e14907634264e6f332e9fb3",
        "lines": ["Test", "Hello"]
    }

    expected_status_code = 200

    expected = b"\"Hash not found\"\n"

    # When
    response = test_client.post("/crack/sha1", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected


#POST request to /crack/sha256 returns the hashed text TEST
def test_crack_sha256_found(test_client):
    # Given
    request_payload = {
        "message": "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2",
        "lines": ["Test", "Hello", "TEST"]
    }

    expected_status_code = 200

    expected = b"\"TEST\"\n"

    # When
    response = test_client.post("/crack/sha256", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected


# POST request to /crack/sha1 returns the hashed text TEST
def test_crack_sha256_not_found(test_client):
    # Given
    request_payload = {
        "message": "94ee059335e587e501cc4bf90613e0814f00a7b08bc7c648fd865a2af6a22cc2",
        "lines": ["Test", "Hello"]
    }

    expected_status_code = 200

    expected = b"\"Hash not found\"\n"

    # When
    response = test_client.post("/crack/sha256", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.data == expected


# POST request to /encode/16
def test_encode_16(test_client):

    # Given
    request_payload = {
        "message": "Hello World"
    }

    expected_status_code = 200

    expected = {"text": "48656C6C6F20576F726C64"}

    # When
    response = test_client.post("/encode/16", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json == expected


# POST request to /decode/16
def test_decode_16(test_client):

    # Given
    request_payload = {
        "message": "48656C6C6F20576F726C64"
    }

    expected_status_code = 200

    expected = {"text": "Hello World"}

    # When
    response = test_client.post("/decode/16", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json == expected


# POST request to /encode/32
def test_encode_32(test_client):

    # Given
    request_payload = {
        "message": "Hello World"
    }

    expected_status_code = 200

    expected = {"text": "JBSWY3DPEBLW64TMMQ======"}

    # When
    response = test_client.post("/encode/32", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json == expected


# POST request to /decode/32
def test_decode_32(test_client):

    # Given
    request_payload = {
        "message": "JBSWY3DPEBLW64TMMQ======"
    }

    expected_status_code = 200

    expected = {"text": "Hello World"}

    # When
    response = test_client.post("/decode/32", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json == expected

# POST request to /encode/64
def test_encode_64(test_client):

    # Given
    request_payload = {
        "message": "Hello World"
    }

    expected_status_code = 200

    expected = {"text": "SGVsbG8gV29ybGQ="}

    # When
    response = test_client.post("/encode/64", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json == expected


# POST request to /decode/64
def test_decode_64(test_client):

    # Given
    request_payload = {
        "message": "SGVsbG8gV29ybGQ="
    }

    expected_status_code = 200

    expected = {"text": "Hello World"}

    # When
    response = test_client.post("/decode/64", json=request_payload)

    # Then
    assert expected_status_code == response.status_code
    assert response.json == expected

if __name__ == '__main__':
    pytest.main()