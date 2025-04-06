from flask import Flask, render_template, request, session, jsonify
from secret_word import SecretWord
from three_doors import ThreeDoors
from two_plus_two import TwoPlusTwo
import pickle

app = Flask(__name__)
app.secret_key = 'super_secret_key'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',
                           secret_chat=session.get('secret_chat', []),
                           doors_chat=session.get('doors_chat', []),
                           two_chat=session.get('two_chat', []))


@app.route('/secret', methods=['POST'])
def secret_word():
    if 'secret_game' not in session:
        game = SecretWord()
        session['secret_game'] = pickle.dumps(game)
        session['secret_chat'] = []
    else:
        game = pickle.loads(session['secret_game'])

    guess = request.form['guess']
    response = game.userInputted(guess)

    history = session.get('secret_chat', [])
    history.append(('user-message', f"🧠 You: {guess}"))
    history.append(('bot-response', f"🤖 GPT: {response}"))
    session['secret_chat'] = history
    session['secret_game'] = pickle.dumps(game)

    return response


@app.route('/three_doors', methods=['POST'])
def three_doors():
    if 'doors_game' not in session:
        game = ThreeDoors()
        session['doors_game'] = pickle.dumps(game)
        session['doors_chat'] = []
    else:
        game = pickle.loads(session['doors_game'])

    guess = request.form['guess']
    response = game.userInputted(guess)

    history = session.get('doors_chat', [])
    history.append(('user-message', f"🧠 You: {guess}"))
    history.append(('bot-response', f"🤖 GPT: {response}"))
    session['doors_chat'] = history
    session['doors_game'] = pickle.dumps(game)

    return response


@app.route('/two_plus_two', methods=['POST'])
def two_plus_two():
    if 'two_game' not in session:
        game = TwoPlusTwo()
        session['two_game'] = pickle.dumps(game)
        session['two_chat'] = []
    else:
        game = pickle.loads(session['two_game'])

    guess = request.form['guess']
    response = game.userInputted(guess)

    history = session.get('two_chat', [])
    history.append(('user-message', f"🧠 You: {guess}"))
    history.append(('bot-response', f"🤖 GPT: {response}"))
    session['two_chat'] = history
    session['two_game'] = pickle.dumps(game)

    return response


@app.route('/reset/<game>', methods=['POST'])
def reset(game):
    if game == 'secret':
        session.pop('secret_game', None)
        session.pop('secret_chat', None)
    elif game == 'three_doors':
        session.pop('doors_game', None)
        session.pop('doors_chat', None)
    elif game == 'two_plus_two':
        session.pop('two_game', None)
        session.pop('two_chat', None)
    return jsonify({'message': f'{game} game reset.'})


if __name__ == '__main__':
    app.run(debug=True)
