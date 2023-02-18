from bson import ObjectId


class PyObjectId(ObjectId):
    # https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


def make_message(message):
    return {"message": message}


def serializeDict(item) -> dict:
    return {
        **{i: str(item[i]) for i in item if i == "_id"},
        **{i: item[i] for i in item if i != "_id"},
    }
