from api import get_two_plus_two_response,reset_two_plus_two_chat
from data.words import words as wordlist
import random


class TwoPlusTwo:
    def __init__(self):
        self.attempts = 30
        reset_two_plus_two_chat()

    def userInputted(self, message):  # call this function when user inputs something
        self.attempts -= 1
        if self.attempts < 0:
            return "Game over! You ran out of attempts."
        
        output = get_two_plus_two_response(message)
        
        if "2 + 2 = 5 is true." in output:
            return output + " You win! The false statement has been verified as true."
        return output + f" You have {self.attempts} attempts left."
