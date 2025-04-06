from api import get_secret_word_response
from data.words import words as wordlist
import random


class SecretWord:
    def __init__(self):
        self.word = random.choice(wordlist)
        self.attempts = 30

    def userInputted(self, message):  # call this function when user inputs something
        self.attempts -= 1
        if self.attempts < 0:
            return "out_of_attempts_message"
        
        output = get_secret_word_response(message, self.word)
        
        if self.word in output.split():
            return output + "\nyou made it etc."
        return output
    
    def button(self, id):
        match id:
            case "RESET":
                pass
