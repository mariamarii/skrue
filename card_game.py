import tkinter as tk
from player import Player
from gui import GUI
import random

class CardGame:
    def __init__(self):
        self.numbers = (list(range(1, 11)) * 4 + list(range(11, 15)) * 2)
        random.shuffle(self.numbers)

        self.root = tk.Tk()

        self.player1 = Player(self.numbers)
        self.player2 = Player(self.numbers)

        self.gui = GUI(self.root, self, self.player1, self.player2)

        self.labels_p1 = self.gui.create_labels(self.player1.pick_numbers(), 650, show_back=True)
        self.labels_p2 = self.gui.create_labels(self.player2.pick_numbers(), 50)


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = CardGame()
    game.run()
