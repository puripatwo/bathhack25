from api import get_three_doors_response
from data.words import words as wordlist
import random


class ThreeDoors:
    def __init__(self):
        self.words = random.choices(wordlist, k=3)
        self.attempts = 30

    def userInputted(self, message):  # call this function when user inputs something
        self.attempts -= 1
        if self.attempts < 0:
            return "out_of_attempts_message"
        
        output = get_three_doors_response(message, self.words)
        
        if any([word in output.split() for word in self.words]):
            return output + "\nyou made it etc."
        return output
    
    def button(self, id):
        match id:
            case "RESET":
                pass
