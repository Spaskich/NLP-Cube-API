import os
from flask import Flask
from flask import Response
from flask import request
from cube.api import Cube

app = Flask(__name__)
lang = os.getenv('MODEL_LANGUAGE')

print('Initializing NLP-Cube...')

cube = Cube(verbose=True)

print('NLP-Cube initialized.')
print('Loading language model for [%s]...' % lang)

cube.load(lang, device='cpu')

print('Language model loaded.')


@app.route('/nlp', methods=['POST'])
def process_text():
    text = request.form['text']
    document = cube(text)

    return Response(str(document), mimetype='text/plain', status=200)


if __name__ == '__main__':
    app.run()
