# 맨위에 Parser directives 지정할 수 있음
# 주석은 BuildKit이 지우고 실행 함
# ex1 syntax) 지정한 버전의 syntax 버전을 들고옴 syntax=docker/dockerfile:1
# ex2 escape) 이스케이프 문자 지정 escape=` Windows에서는 \가 경로를 표시해 오류 발생할 수 있음 그럴때 사용
# ex3 check) 문법검사 지정
#       check=skip=<checks|all> # check=error=<boolean>
#       check=skip=JSONArgsRecommended,StageNameCasing
#       check=error=true

FROM python:3.9-alpine

#ENV 
# ${variable_name} $variable_name 둘 다 사용 가능
# ${variable_name:-default_value} 변수값이 없을 때 기본값 설정
# ${variable_name:+alternate_value} 변수값이 있을 때 대체값 설정
# 

# ENTRYPOINT
# Shell form
# INSTRUCTION command param1 param2
# \로 명령어 줄바꿈

# EXEC form
# INSTRUCTION ["executable","param1","param2"] 
# JSON array 형식으로 작성

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser -D appuser
USER appuser

#CMD ["python", "app.py"]
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]

