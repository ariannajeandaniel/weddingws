from flask import Flask
from flask import request, send_from_directory
app = Flask(__name__)


@app.route("/")
def root():
    try:
      language = request.headers.get('Accept-Language')
    except KeyError:
      language = 'en'
    if language.startswith('it'):
      return send_from_directory('.', 'indice.html')
    elif language.startswith('fr'):
      return send_from_directory('.', 'accueil.html')
    return send_from_directory('.', 'index.html')
