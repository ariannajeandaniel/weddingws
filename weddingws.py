import os
from flask import Flask
from flask import request, send_from_directory

DIR = '.'

app = Flask(__name__)

class InternalError(Exception):
    pass

send = lambda basename: send_from_directory(DIR, basename)

indexes = ('en', 'index.html'), ('fr', 'accueil.html'), ('it', 'indice.html')

@app.route("/")
def root():
    language = request.headers.get('Accept-Language', 'en')
    for lan, filename in indexes:
      if language.startswith(lan):
         return send(filename)
    return send('index.html')

@app.route('/<filename>')
def page(filename):
    try:
        return send(filename)
    except IOError as e:
        print e
        return 'Not found.', 404

allowed_dirs = ('css', 'about', 'jekyll')
    
@app.route('/<dir>/<filename>')
def subpage(dir, filename):
    if dir not in allowed_dirs:
        return 'Not found.', 404
    try:
        return send_from_directory(dir, filename)
    except IOError as e:
        print e
        return 'Not found.', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
