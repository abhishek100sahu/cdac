from flask import Flask
from icecream import ic

app = Flask(__name__)


@app.route('/', methods=['GET'])

def index():
    return '''
    <html>
        <head>
            <title>
                title
            </title>
        </head>
    
        <body>
            <h2>
                Hello, world
            </h2>
        </body>
    '''

app.run(debug=True)