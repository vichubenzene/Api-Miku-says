import random
from flask import Flask, jsonify, request,json,render_template
from threading import Thread

app = Flask('')

@app.route('/<string:name>')
def home(name: str):
    with open(f'{name}.json', 'r') as f:
        q = json.load(f)
    return jsonify(random.choice(q)), 200

@app.route('/')
def home2():
    return render_template('index.html')
    # return jsonify(HI='welcome to Mikusays api use endpoints', Quiz = 'https://miku-says.benzene002.repl.co/quiz', Topic = 'https://miku-says.benzene002.repl.co\topic'),200


def run():
  app.run(host='0.0.0.0',port=8080)

def say():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    say()

