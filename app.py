import os
from flask import Flask, request, render_template

app = Flask(__name__)


supported_languages = ['English', 'Hindi', 'French']
hello_world_msg = {'English':'Hello world', 'Hindi':'Namastey sansar', 'French':'Bonjour le monde'}


@app.route('/hello', methods=['GET'])
def hello_world():
    try:
        
        lang = request.args.get('language')
        msg = None
        status = None

        if lang in supported_languages:
            status = 200
            msg = hello_world_msg[lang]
        
        else :
            status = 400
            msg = 'language prefrence missing or invalid'

    except Exception as ex:

        print('internal server error -> ',str(ex))
        status = 500
        msg = 'internal server error'
    
    finally:
        return render_template('hello.html', msg=msg)


@app.route('/', methods=['GET'])
def index():
    
    msg = 'visit /hello with param lanaguage as ["English", "Hindi", "French"] for greeting message, eg /hello?language=English'
    
    english_link = '/hello?language=English'
    hindi_link = '/hello?language=Hindi'
    french_link = '/hello?language=French'

    return render_template('index.html', msg=msg, english_link=english_link, hindi_link=hindi_link, french_link=french_link)

if __name__ == '__main__':
    os.environ['FLASK_APP'] = 'hello'
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug=True)
