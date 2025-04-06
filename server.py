from flask import Flask, render_template, request, session
from secret_word import SecretWord
from three_doors import ThreeDoors
from two_plus_two import TwoPlusTwo
import pickle

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/secret', methods=['POST'])
def secret_word():
    if 'game' not in session:
        game = SecretWord()
        session['game'] = pickle.dumps(game)
        session['chat_history'] = []
    else:
        game = pickle.loads(session['game'])

    guess = request.form['guess']
    response = game.userInputted(guess)

    # Update the chat history
    history = session.get('chat_history', [])
    history.append(('user-message', f"🧠 You: {guess}"))
    history.append(('bot-response', f"🤖 GPT: {response}"))
    session['chat_history'] = history

    # Return the bot response as a plain text
    return response

if __name__ == '__main__':
    app.run(debug=True)
