from player import Player, Computer, increase_round_counter, get_round_counter
from gui import GUI
import random
import tkinter as tk

class CardGame:
    def __init__(self):
        self.numbers = (list(range(1, 11)) * 4 + list(range(11, 15)) * 2)
        self.numbers = self.numbers + [20, 20, 25, 25, -1, -1, -5, -5]
        random.shuffle(self.numbers)

        self.root = tk.Tk()

        self.player1 = Player(self.numbers)
        self.computer = Computer(self.numbers)

        self.gui = GUI(self.root, self, self.player1, self.computer)

        self.labels_p1 = self.gui.create_labels(self.player1.pick_numbers(), 650, show_back=True)

        self.labels_p2 = self.gui.create_labels(self.computer.pick_numbers(), 50)
        self.computer.computerSeen.append((0, self.computer.cards[0]))
        self.computer.computerSeen.append((1, self.computer.cards[1]))
        self.computer.computerSeen.append((2, 15))
        self.computer.computerSeen.append((3, 15))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = CardGame()
    game.run()
