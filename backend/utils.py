# FastAPI에서 사용할 유틸리티 함수들을 정의하는 모듈인 utils.py
from bson import ObjectId

# PyObjectId 클래스:
# MongoDB의 ObjectId를 Python에서 사용하기 쉽도록 Wrapping하여 FastAPI에서 쉽게 사용할 수 있도록 한다.
# 이 클래스는 bson.ObjectId 클래스를 상속하며,
# __get_validators__와 __modify_schema__ 메소드를 오버라이드하여 FastAPI에서 해당 클래스를 사용할 때 유효성 검사를 수행하도록 한다.

# 위에 내용을 더 쉬운표현으로 설명하자면,
# Python에서 MongoDB에서 사용되는 ObjectId는 일반적인 문자열과는 다른 형식을 갖고 있으며,
# 이를 FastAPI에서 바로 사용하면 유효성 검사를 통과하지 못할 수 있다.
# 따라서 PyObjectId 클래스는 해당 ObjectId를 Python에서 사용하기 쉬운 형태로 Wrapping하고,
# FastAPI에서 해당 클래스를 사용할 때 유효성 검사를 수행하도록 함으로써 이를 방지해준다.


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


# ObjectIdStr 클래스와 StrObjectId 클래스: ObjectId와 str 타입을 서로 변환하기 위한 유틸리티 클래스다.
# 이 클래스들도 __get_validators__와 validate 메소드를 오버라이드하여 FastAPI에서 해당 클래스를 사용할 때 유효성 검사를 수행하도록 한다.
# 결국 둘다 유효성 검사 기능을 한다.


class ObjectIdStr(str):
    # https://github.com/tiangolo/fastapi/issues/452
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class StrObjectId(str):
    # https://github.com/tiangolo/fastapi/issues/452
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise ValueError("Not a str")
        return ObjectId(v)


# make_message 함수: 문자열 메시지를 인자로 받아서 딕셔너리 형태로 변환하여 반환한다. 이 함수는 테스트 용도로 사용될 수 있다.
def make_message(message):
    return {"message": message}
