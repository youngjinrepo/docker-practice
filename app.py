import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

redis = Redis(host=redis_host, port=redis_port)

is_healthy = True   

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello Docker!  방문자 수: {count} 명 🚀'

@app.route('/health')
def health_check():
    if is_healthy:
        return "I'm OK", 200  # 정상 (200 OK)
    else:
        return "I'm Sick...", 500 # 아픔 (500 Error -> 쿠버네티스가 감지함)
    
# 2. 서버를 고장 내는 버튼 (우리가 호출할 주소)
@app.route('/die')
def kill_server():
    global is_healthy
    is_healthy = False  # 상태를 '아픔'으로 변경
    return "Argh! I am dying...", 200

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)