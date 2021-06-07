import flask
import redis

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/set')
def set():
    key = flask.request.args.get('key')
    value = flask.request.args.get('value')
    r = redis.Redis(host='redis', port=6370)
    r.set(name=key, value=value)
    return "OK"

@app.route('/get')
def get():
    key = flask.request.args.get('key')
    r = redis.Redis(host='redis', port=6370)
    value = r.get(key)
    return value

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)