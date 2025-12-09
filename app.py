import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello Docker! 방문자 수: {count} 명 🚀'

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)