import os
import logging
from waitress import serve
from flask import Flask
from flask import Response
from flask import request
from cube.api import Cube

# __name__ = "__main__"
app = Flask(__name__)

logging.basicConfig(filename='./logs/application.log', level=logging.INFO)


def initialize_cube():
    logging.info('Initializing NLP-Cube...')
    cubeObj = Cube(verbose=True)

    logging.info('NLP-Cube initialized.')
    return cubeObj


def load_language_model(language):

    logging.info('Loading language model for [%s]...' % language)

    cube.load(language, device='cpu')
    logging.info('Language model loaded.')


@app.route('/nlp', methods=['POST'])
def process_text():
    text = request.form['text']
    document = cube(text)

    return Response(str(document), mimetype='text/plain', status=200)


if __name__ == '__main__':

    lang = os.getenv('MODEL_LANGUAGE', 'en')
    cube = initialize_cube()
    load_language_model(lang)

    host = os.getenv('FLASK_HOST', "0.0.0.0")
    port = os.getenv('FLASK_PORT', 8080)

    serve(app, host=host, port=port)

    logging.info("Running on {0}:{1}".format(host, port))
