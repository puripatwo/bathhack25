from api import get_secret_word_response,reset_secret_word_chat
from data.words import words as wordlist
import random


class SecretWord:
    def __init__(self):
        self.word = random.choice(wordlist)
        self.attempts = 30
        reset_secret_word_chat()


    def userInputted(self, message):  # call this function when user inputs something
        self.attempts -= 1
        if self.attempts < 0:
            return "Game over! You ran out of attempts."
        
        output = get_secret_word_response(message, self.word)
        
        if self.word in output.split():
            return "You win! The secret word was guessed correctly."
        return output + f"you have {self.attempts} attempts left"
    
    def button(self, id):
        match id:
            case "RESET":
                pass
