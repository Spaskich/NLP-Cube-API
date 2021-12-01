import os
from waitress import serve
from flask import Flask
from flask import Response
from flask import request
from cube.api import Cube

app = Flask(__name__)


def initialize_cube():
    print('Initializing NLP-Cube...')
    cubeObj = Cube(verbose=True)

    print('NLP-Cube initialized.')
    return cubeObj


def load_language_model(language):

    print('Loading language model for [%s]...' % language)

    cube.load(language, device='cpu')
    print('Language model loaded.')


@app.route('/nlp', methods=['POST'])
def process_text():
    text = request.form['text']
    document = cube(text)

    return Response(str(document), mimetype='text/plain', status=200)


if __name__ == '__main__':

    lang = os.getenv('MODEL_LANGUAGE')
    cube = initialize_cube()
    load_language_model(lang)

    serve(app, host="0.0.0.0", port=8000)
