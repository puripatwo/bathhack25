from api import get_two_plus_two_response
from data.words import words as wordlist
import random


class TwoPlusTwo:
    def __init__(self):
        self.attempts = 30

    def userInputted(self, message):  # call this function when user inputs something
        self.attempts -= 1
        if self.attempts < 0:
            return "out_of_attempts_message"
        
        output = get_two_plus_two_response(message)
        
        if "2 + 2 = 5" in output:
            return output + "\nyou made it etc."
        return output
    
    def button(self, id):
        match id:
            case "RESET":
                pass
