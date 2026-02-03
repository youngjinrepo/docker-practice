from flask import Flask
import socket
import redis
import os

app = Flask(__name__)

# 환경변수에서 Redis 주소를 가져오거나, 없으면 'redis'로 설정
redis_host = os.getenv('REDIS_HOST', 'redis')
# 연결 시도 (여기서는 연결만 맺고 실제 통신은 안 함)
r = redis.Redis(host=redis_host, port=6379, socket_timeout=2)
# login 

@app.route('/')
def hello():
    try:
        # Redis에 접속 시도!
        r.incr('hits')
        count = r.get('hits').decode('utf-8')
    except Exception as e:
        # ⭐ [핵심] Redis가 없으면 에러 내지 말고 그냥 메시지로 대체해!
        count = "Redis 없음 (연결 실패)"

    return f'[Version 3] Fixed! Host: {socket.gethostname()} / Count: {count}\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)