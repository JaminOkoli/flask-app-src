# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Pluralsight!'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)


from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask in Docker!"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/slow")
def slow():
    time.sleep(5)
    return {"status": "slow response complete"}

@app.route("/error")
def error():
    return {"error": "something went wrong"}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)