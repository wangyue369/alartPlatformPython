import uuid


def generate_id():
    return "".join(str(uuid.uuid1()).split("-"))
