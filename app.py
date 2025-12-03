from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='my-db', port=6379)


@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'Hello Docker! 방문자 수: {count} 명 🚀'

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)