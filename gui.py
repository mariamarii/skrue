import time
import tkinter as tk


from PIL import Image, ImageTk, ImageDraw
from player import increase_round_counter, get_round_counter

class GUI:
    def __init__(self, root, card_game, player1, player2):
        self.root = root
        self.card_game = card_game
        self.player = player1
        self.computer = player2
        self.deckLabel = None
        self.pile_labels = []
        self.root.title("Card Game")
        self.root.geometry("1500x1024")
        self.root.resizable(width=False, height=False)
        #self.root.configure(bg='#000fff000')  # change color

        # Load and resize background image
        background_image = Image.open("img/background.gif")
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background image
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.back_image = self.round_corners("img/cardback.gif", 10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.place(x=700, y=500)

        self.game_started = False

        self.labels_p1 = []  # Initialize empty list to store player 1 labels
        self.labels_p2 = []  # Initialize empty list to store player 2 labels

        self.drawn_cards = []

    def start_game(self):
        self.game_started = True
        self.draw_pile()
        self.start_button.place_forget()
        self.flip_back_player1(self.labels_p1)
        self.draw_card()
        #time.sleep(2)
        self.perform_exchange_card()  # Call once initially
        self.continuous_exchange_card()  # Schedule continuous calling

    def continuous_exchange_card(self):
        if get_round_counter() % 2 != 0:
            self.perform_exchange_card()
        self.root.after(1000, self.continuous_exchange_card)

    def create_labels(self, numbers, y, show_back=False):
        start_x = (1500 - (len(numbers) * 150)) // 2
        labels = []
        for i, num in enumerate(numbers):
            if i >= 2 and show_back:
                card_image = self.round_corners(f"img/{num}.gif", 10)
            else:
                card_image = self.round_corners("img/cardback.gif", 10)

            my_label = tk.Label(self.root, image=card_image)
            my_label.image = card_image
            my_label.place(x=start_x + i * 150, y=y)
            labels.append(my_label)
            if(show_back):
                my_label.bind("<Button-1>", lambda event, index=i: self.player.on_player_cards_click(index, self.root))
                self.player.deck = self.player.test()

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
            self.player.deck = self.card_game.numbers.pop(0)
            card_image = self.round_corners(f"img/{self.player.deck}.gif", 10)

            self.deckLabel = tk.Label(self.root, image=card_image)
            self.deckLabel.bind("<Button-1>", lambda event: self.player.deckCardCliked(self.deckLabel, self.player.deck))
            self.deckLabel.image = card_image
            self.deckLabel.place(x=675, y=375)
            self.drawn_cards.append(self.deckLabel)

    def draw_pile(self):
        x_start = 200  # Starting x position
        y_start = 300  # Starting y position
        angle_step = -2  # Angle step for fan effect

        for i in range(8):
            card_label = tk.Label(self.root, image=self.back_image, bd=0, highlightthickness=0)
            card_label.place(x=x_start + i * angle_step, y=y_start - i * angle_step)
            card_label.bind("<Button-1>", lambda event, label=card_label: self.player.pileCardClicked(self.root, self.deckLabel))
            self.pile_labels.append(card_label)

    def perform_exchange_card(self):
        if get_round_counter() % 2 != 0:
            while get_round_counter() % 2 != 0:
                self.player.deck, self.labels_p2 = self.computer.exchangeCard(self.deckLabel, self.player.deck, self.labels_p2, self.back_image)
                self.root.update()
                time.sleep(3)

    def round_corners(self,image_path, radius):
        # Open the image using PIL
        image = Image.open(image_path).convert("RGBA")

        # Create a mask with rounded corners
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((10, 3, image.width - 10, image.height - 3), radius, fill=255)

        rounded_image = Image.new("RGBA", image.size, (255, 255, 255, 0))

        # Paste the original image onto the new image using the rounded mask
        rounded_image.paste(image, (0, 0), mask)

        # Apply the mask to the image
        bbox = rounded_image.getbbox()
        rounded_image = rounded_image.crop(bbox)

        img = ImageTk.PhotoImage(rounded_image)

        return img