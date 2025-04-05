from flask import Flask, render_template, redirect, url_for
from game import magical1,magical2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/secret')
def secret_word():
    return_data = magical1() #magical function that does everything
    return render_template('secret_word.html', hello = return_data)

if __name__ == '__main__':
    app.run(debug=True)
