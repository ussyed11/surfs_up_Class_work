from flask import Flask
app = Flask(__name__)
@app.route('/')
def It_is_sunny():
    return 'It is sunny'
