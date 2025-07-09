from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "DevOps Docker Container 9.07"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

