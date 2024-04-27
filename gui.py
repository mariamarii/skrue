import tkinter as tk
from PIL import Image, ImageTk

class GUI:
    def __init__(self, root,card_game,player1,player2):
        self.root = root
        self.card_game=card_game
        self.player1 = player1
        self.player2 = player2
        self.root.title("Card Game")
        self.root.geometry("1500x1024")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#000fff000')  # change color

        # Load and resize background image
        background_image = Image.open("back2.jpeg")
        background_image = background_image.resize((1500, 1024))
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background image
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.back_image = ImageTk.PhotoImage(Image.open("img/cardback.gif").resize((110, 150)))

        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.place(x=700, y=500)

        self.game_started = False

        self.deck_labels = []
        for i in range(8):
            label = tk.Label(self.root, image=self.back_image)
            label.place(x=1200, y=300 + i * 5)  # Adjust the y-coordinate to stack the cards
            self.deck_labels.append(label)

        self.labels_p1 = []  # Initialize empty list to store player 1 labels
        self.labels_p2 = []  # Initialize empty list to store player 2 labels

        self.drawn_cards = []

    def start_game(self):
        self.game_started = True
        self.start_button.place_forget()
        self.flip_back_player1(self.labels_p1)
        self.draw_card()

    def create_labels(self, numbers, y, show_back=False):
        start_x = (1500 - (len(numbers) * 150)) // 2
        labels = []
        for i, num in enumerate(numbers):
            if i >= 2 and show_back:
                card_image = ImageTk.PhotoImage(Image.open(f"img/{num}.gif").resize((110, 150)))
            else:
                card_image = self.back_image

            label = tk.Label(self.root, image=card_image)
            label.image = card_image
            label.place(x=start_x + i * 150, y=y)
            labels.append(label)

        # Store the labels in the appropriate attribute
        if y == 650:
            self.labels_p1 = labels
        elif y == 50:
            self.labels_p2 = labels

        return labels

    def flip_back_player1(self, labels):
        for label in labels[2:]:
            label.config(image=self.back_image)

    def draw_card(self):
        if self.card_game.numbers:
            random_value = self.card_game.numbers.pop()
            card_image = ImageTk.PhotoImage(Image.open(f"img/{random_value}.gif").resize((110, 150)))
            card_label = tk.Label(self.root, image=card_image)
            card_label.image = card_image
            card_label.place(x=675, y=375)
            self.drawn_cards.append(card_label)
