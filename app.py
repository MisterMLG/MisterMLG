from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('shop.html')

@app.route('/about/')
@app.route('/about/<username>')
def about(username='me'):
    return f'All about {escape(username)}'


if __name__=='__main__':
    app.run()

