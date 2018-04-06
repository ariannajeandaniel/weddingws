import os
from flask import Flask
from flask import request, send_from_directory
app = Flask(__name__)


class InternalError(Exception):
    pass


website_directory = '.'
allowed_files = [name for name in os.listdir(website_directory) if name.endswith('.html')]
if (
    'index.html' not in allowed_files
    or 'accueil.html' not in allowed_files
    or 'indice.html' not in allowed_files):
    raise InternalError('Index files not found in website directory.')


@app.route("/")
def root():
    try:
      language = request.headers.get('Accept-Language')
    except KeyError:
      language = 'en'
    if language.startswith('it'):
      return send_from_directory(website_directory, 'indice.html')
    elif language.startswith('fr'):
      return send_from_directory(website_directory, 'accueil.html')
    return send_from_directory(website_directory, 'index.html')


@app.route('/<filename>')
def page(filename):
    if filename in allowed_files:
        return send_from_directory(website_directory, filename)
    else:
        return 'Not found.', 404
