from flask import Flask, render_template, request, session
from game import SecretWord
import pickle

app = Flask(__name__)
app.secret_key = 'super_secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/secret', methods=['GET', 'POST'])
def secret_word():
    if request.method == 'GET':
        session.pop('game', None)
        session.pop('chat_history', None)

    if 'game' not in session:
        game = SecretWord()
        session['game'] = pickle.dumps(game)
        session['chat_history'] = []
    else:
        game = pickle.loads(session['game'])

    if request.method == 'POST':
        try:
            guess = request.form['guess']
            response = game.userInputted(guess)

            history = session.get('chat_history', [])
            history.append(f"🧠 You: {guess}")
            history.append(f"🤖 GPT: {response}")
            session['chat_history'] = history

            if "Congratulations" in response:
                session.pop('game', None)
            else:
                session['game'] = pickle.dumps(game)
        except Exception as e:
            message = str(e)
    
    return render_template('secret_word.html', chat=session.get('chat_history', []))


if __name__ == '__main__':
    app.run(debug=True)
