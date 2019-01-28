from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        return 'Up and running...'
    else:
        return request.form['challenge']

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)