#from api import get_user_input
from words import words as wordlist
import random

class SecretWord:
    def __init__(self):
        self.word = random.choice(wordlist)
        self.attempts = 30

    def userInputted(self,message): #call this function when user inputs something
        attempts -= 1
        if attempts < 0:
            return "out_of_attempts_message"
        output = f"you sent me {message}"
        return output
    def userWordGuess(self,word): #call this function when user guesses a word
        if self.word == word:
            return f"Congratulations! The word was {self.word}, you guessed it with {self.attempts} remaining"
        return f"incorrect"
    def button(self,id):
        match id:
            case "RESET":
                pass
