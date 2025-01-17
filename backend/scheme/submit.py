import re

from fastapi import Request

# fastapi.Request 클래스를 사용하여 HTTP 요청에서 전달받은 "폼 데이터"를 처리하는 SubmitForm 클래스를 정의하는 코드다.


class SubmitForm:
    """
    load_data()를 통해 아래 변수를 생성
    username: str
    email: EmailStr
    student_id: str
    python_skill: str
    motivation: str
    github: Optional[str]
    blog: Optional[str]
    ai_subject: Optional[str]
    study_want: Optional[str]
    project_want: Optional[str]
    course: Optional[str]
    project_exp: Optional[str]
    """

    def __init__(self, request: Request):  # SubmitForm 클래스의 생성자
        # Request 객체를 이용해서 폼 데이터를 받아온다.
        self.request = request  # Request 객체를 인자로 받아서 self.request 속성에 저장하고, self.errors 속성을 빈 리스트로 초기화한다.
        self.errors = []  # self.errors 속성은 폼 데이터를 처리하면서 "발생한 오류"를 저장하는 데 사용될 수 있다.

    async def load_data(self):  # load_data 메서드를 사용하여 전달받은 폼 데이터를 로드하고,
        form = await self.request.form()
        for k, v in form.items():
            setattr(self, k, v)

    def send_data(self) -> dict:
        send_list = {}
        for k, v in self.__dict__.items():
            if not (k == "request" or k == "errors"):
                send_list[k] = v
        return send_list

    def is_valid(self):  # is_valid 메서드는 데이터의 유효성을 검사하는 로직이 구현되어 있다.
        # SubmitForm 클래스의 username 속성이 "빈 문자열"인 경우 "False"를 반환하고, 그렇지 않은 경우 "True"를 반환한다.
        if self.username == "":
            return False

        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_pattern, self.email):  # 정규식을 사용하여 이메일 폼 확인
            return False

        if len(self.student_id) != 9:
            return False

        return True
