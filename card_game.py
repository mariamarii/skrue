import random
import tkinter as tk

from tkinter import PhotoImage

#from bokeh.models import canvas

from gui import GUI
from player import Player, Computer


class CardGamePage:
    def __init__(self):
        self.root = tk.Tk()
        self.current_frame = None
        self.root.geometry("1500x1024")
        self.root.resizable(False, False)  # Disable window resizing
        self.show_start_page()

    def show_start_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = StartPage(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_card_game(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = CardGame(self.root)
        self.current_frame.run()

    def show_how_to_play(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = HowToPlayPage(self.root, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def run(self):
        self.root.mainloop()


class CardGame:
    def __init__(self, root):
        self.numbers = (list(range(1, 11)) * 4 + list(range(11, 15)) * 2)
        self.numbers = self.numbers + [0 , 0, 20, 20, 25, 25, -1, -5]
        random.shuffle(self.numbers)
        self.computerSeen = []
        self.playerSeen = []

        self.player1 = Player(self.numbers, self.playerSeen, self.computerSeen)
        self.computer = Computer(self.numbers, self.playerSeen, self.computerSeen,root)

        self.gui = GUI(root, self, self.player1, self.computer)

        self.labels_p1 = self.gui.create_labels(self.player1.pick_numbers_player(), 650, show_back=True)
        self.labels_p2 = self.gui.create_labels_com(self.computer.pick_numbers(), 50)
        self.computer.computerSeen.append((0, self.computer.cards[0]))
        self.computer.computerSeen.append((1, self.computer.cards[1]))
        self.computer.computerSeen.append((2, 15))
        self.computer.computerSeen.append((3, 15))

        self.playerSeen.append((0, 15))
        self.playerSeen.append((1, 15))
        self.playerSeen.append((2, 15))
        self.playerSeen.append((3, 15))

    def get_labels_p2(self):
        return self.labels_p2

    def run(self):
        pass  # The GUI handles the mainloop


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Load background image
        self.bg_image = tk.PhotoImage(file="img/start2.gif")

        # Create Canvas widget to hold the background image
        self.canvas = tk.Canvas(self, width=1500, height=1024)
        self.canvas.pack(fill="both", expand=True)

        # Place the background image on the canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        button1 = tk.Button(self.canvas, text="Screw Now", command=lambda: controller.show_card_game(), bg="#E3BA5C", fg="white", font=("Comic Sans MS", 14))
        button1.place(x=470, y=600, width=240, height=60)
        button1.config(activebackground="#E5A82E")

        button2 = tk.Button(self.canvas, text="How to Play", command=lambda: controller.show_how_to_play(), bg="white", font=("Comic Sans MS", 14))
        button2.place(x=800, y=600, width=240, height=60)
        button2.config(activebackground="#E2E1E0")


class HowToPlayPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Load background image
        self.bg_image = tk.PhotoImage(file="img/how to play back.gif")

        # Create Canvas widget to hold the background image
        self.canvas = tk.Canvas(self, width=1500, height=1024)
        self.canvas.pack(fill="both", expand=True)

        # Place the background image on the canvas
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Write text on the background image
        self.canvas.create_text(750, 400, text="""
        Game system:

        It is to get the smallest number of numbers, and each player at the playing table starts with two face-up cards,
        then a field of cards is placed in the half from which the players draw in order from right to left.
        The method of the game consists of three draws or more until one of the players says (Screw).

        Each player chooses one of three options:

        1- It is withdrawn from the pile of cards, then it is decided whether to keep it or dispose of it on the deck.
        2- Or he draws from the deck the last card left by the player before him in a way that helps him win.

        Auxiliary cards to play:
        
        Card No. 7 or  8: You look at only one of your cards
        Card No. 9 or 10: You look at only one card from one of the players.
        
        The following cards: If you have them when the game ends, they will be +10.
        
        khod w hat card: You replace a card from one of the players with a card of your own without looking at the cards.
        k3b dair card: You look at one card from each player, including a card from your own.
        Basra card: With this card, you can get rid of one of your cards by your choice.
        See swap: You replace a card from one of the players with a card of your own and you can see the card you took.
        Warning: In order to be able to use these cards, they must be drawn from the pile.

        Game over:
        The player who clicks “Screw” does not play the turn, then everyone plays until the turn is reached, 
        then the cards are revealed, and the player with the lowest number is the winner.
        """, font=("Comic Sans MS", 14), fill="white", justify="center")

        # Back button
        button = tk.Button(self.canvas, text="Back", command=lambda: controller.show_start_page(), font=("Comic Sans MS", 10), bg="white")
        button.place(x=20, y=20)
        button.config(activebackground="#E2E1E0")

        # Update the canvas to ensure proper scrolling behavior
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))








if __name__ == "__main__":
    game = CardGamePage()
    game.run()


