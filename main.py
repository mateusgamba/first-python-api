from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Python!'

@app.route('/sum/<a>/<b>')
def sum(a,b):
    x = int(a)+int(b)
    y = {"Result" : x}
    return jsonify(y)

@app.route('/show-name', methods=['POST'])
def add():
    value = request.json
    data = {"Result": value['name']}
    return jsonify(data)

if __name__ == "__main__":
    app.run()


