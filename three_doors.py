from api import get_three_doors_response, reset_three_doors_chat
import random

related_words = [
    ["sun", "moon", "stars"],
    ["apple", "banana", "orange"],
    ["cat", "dog", "rabbit"],
    ["pen", "pencil", "eraser"],
    ["car", "truck", "motorcycle"],
    ["red", "blue", "green"],
    ["doctor", "nurse", "hospital"],
    ["ocean", "wave", "beach"],
    ["mountain", "valley", "hill"],
    ["book", "page", "chapter"],
    ["keyboard", "mouse", "monitor"],
    ["guitar", "drums", "piano"],
    ["chair", "table", "sofa"],
    ["bread", "butter", "jam"],
    ["rain", "snow", "hail"],
    ["shoe", "sock", "lace"],
    ["river", "stream", "creek"],
    ["lion", "tiger", "leopard"],
    ["gold", "silver", "bronze"],
    ["cup", "plate", "bowl"],
    ["apple", "banana", "carrot"]
]


class ThreeDoors:
    def __init__(self):
        self.words = random.choice(related_words)
        self.attempts = 30
        reset_three_doors_chat()

    def userInputted(self, message):  # call this function when user inputs something
        self.attempts -= 1
        if self.attempts < 0:
            return "Game over! You ran out of attempts."
        
        output = get_three_doors_response(message, self.words)
        
        if any([word in output.split() for word in self.words]):
            return output + " You win! The secret word was guessed correctly."
        return output + f" You have {self.attempts} attempts left."
