from flask import Flask
from flask_cors import CORS
from db.characters import get_all_characters

app = Flask(__name__)
CORS(app)


@app.route('/characters')
def all_characters():
    return get_all_characters()