from api import get_user_input
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
        output = get_user_input(message)
        if self.word in output.split():
            return output + "\nyou made it etc."
        return output
    def button(self,id):
        match id:
            case "RESET":
                pass
