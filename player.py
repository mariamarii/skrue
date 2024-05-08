from PIL import Image, ImageTk
import tkinter as tk

class Player:
    def __init__(self, numbers, playerSeen, computerSeen):
        self.cards = []
        self.numbers = numbers
        self.deck_card_clicked = False
        self.deckLabel = None
        self.role = False
        self.deck = 0
        self.card_label = None
        self.computerSeen = computerSeen  # Use passed computerSeen listself.pile_card_clicked=False
        self.pile_pop_player = 0
        self.playerSeen = playerSeen
        self.pileLabel = None
        self.pile_card_clicked = False

    def pick_numbers(self):
        self.cards = [self.numbers.pop() for _ in range(4)]
        return self.cards

    def deckCardCliked(self, deckLabel, deck):
        self.deckLabel = deckLabel
        self.deck = deck
        self.deck_card_clicked = True

        if self.pile_card_clicked == True:
            self.exchangeCardPlayer()
        self.pile_card_clicked = False

    def pileCardClicked(self, root, deckLabel):
        self.pile_card_clicked = True
        self.deckLabelGUI = deckLabel
        self.displayPileCard(root)


    def displayPileCard(self, root):  # Display the drawn pile card briefly
        self.pile_pop_player = self.numbers.pop(0)
        self.pile_card_image = ImageTk.PhotoImage(Image.open(f"img/{self.pile_pop_player}.gif"))
        x_start = 330  # Starting x position
        y_start = 300  # Starting y position
        self.pileLabel = tk.Label(root, image=self.pile_card_image, bd=0, highlightthickness=0)
        self.pileLabel.place(x=x_start, y=y_start)


    def displayPileBack(self):
        self.pileLabel.place_forget()

    def on_player_cards_click(self, button_player_index, root):
        if self.deck_card_clicked == True and get_round_counter() % 2 == 0:
            print('player')
            player_card_value = self.cards[button_player_index]
            temp = self.deck
            self.deck = player_card_value
            player_card_value = temp
            self.cards[button_player_index] = player_card_value
            self.playerSeen[button_player_index] = (button_player_index, player_card_value)
            self.card_label = ImageTk.PhotoImage(Image.open(f"img/{self.deck}.gif"))
            self.deckLabel.config(image=self.card_label)
            self.deck_card_clicked = False
            increase_round_counter()
        elif self.pile_card_clicked == True and get_round_counter() % 2 == 0:  # card exchange
            print('player2')  # pile_popped = self.numbers.pop(0)
            self.numbers.append(self.deck)

            self.deckLabel = self.deckLabelGUI# self.computerSeen[max_value[0]] = (max_value[0], pile_popped)  # Update as tuple
            self.playerImage = ImageTk.PhotoImage(Image.open(f"img/{self.cards[button_player_index]}.gif"))
            self.deckLabel.config(image=self.playerImage)
            self.deck = self.cards[button_player_index]
            self.cards[button_player_index] = self.pile_pop_player
            self.playerSeen[button_player_index] = (button_player_index, self.deck)
            self.displayPileBack()
            increase_round_counter()

        else:
            self.flip_card(button_player_index, root)
            root.after(2000, lambda: increase_round_counter())

    def flip_card(self, index, root):
        start_x = (1500 - (len(self.cards) * 150)) // 2

        card_image = ImageTk.PhotoImage(Image.open(f"img/{self.cards[index]}.gif"))
        my_label = tk.Label(root, image=card_image)
        my_label.image = card_image
        my_label.place(x=start_x + index * 150, y=500)
        root.after(2000, lambda: self.delay_forget_label(my_label))

    def delay_forget_label(self, label):
        label.place_forget()

    def exchangeCardPlayer(self):  # card exchange
        print("card")  # pile_popped = self.numbers.pop(0)
        self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{self.pile_pop_player}.gif"))
        self.deckLabel.config(image=self.computerImage)
        self.numbers.append(self.deck)
        self.deck = self.pile_pop_player
        self.displayPileBack()
        increase_round_counter()

    def test(self):
        return self.deck

class Computer(Player):
    def __init__(self, numbers, playerSeen, computerSeen, root):
        super().__init__(numbers, playerSeen, computerSeen)
        self.root = root

    def exchangeCard(self, deckLabel, deckCard, labels_p2, backcard):
        self.deck = deckCard
        self.deckLabel = deckLabel

        # Check if computerSeen contains tuples
        if not all(isinstance(item, tuple) for item in self.computerSeen):
            print("Error: computerSeen does not contain tuples")
            return self.deck, labels_p2

        # Find maximum value from computerSeen
        max_value = max(self.computerSeen, key=lambda t: t[1])

        if get_round_counter() % 2 != 0:
            print('computer')
            if (self.deck < 5 and self.deck < int(max_value[1])) or (self.deck < max_value[1]):
                self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{self.cards[max_value[0]]}.gif"))
                self.index = max_value[0]
                labels_p2[self.index].config(image = backcard, background = "#E5A82E")
                deckLabel.config(image=self.computerImage)
                temp = self.deck
                self.deck = self.cards[max_value[0]]
                self.computerSeen[max_value[0]] = (max_value[0], temp)  # Update as tuple
                self.cards[max_value[0]] = temp
            else:
                pile_popped = self.numbers.pop(0)
                if (pile_popped < 5 and pile_popped < max_value[1]) or (pile_popped < max_value[1]):
                    self.numbers.append(self.deck)
                    self.index = max_value[0]
                    labels_p2[self.index].config(image=backcard, background="#E5A82E")
                    self.computerSeen[max_value[0]] = (max_value[0], pile_popped)  # Update as tuple
                    self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{self.cards[max_value[0]]}.gif"))
                    self.deckLabel.config(image=self.computerImage)
                    self.deck = self.cards[max_value[0]]
                    self.cards[max_value[0]] = pile_popped
                else:
                    self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{pile_popped}.gif"))
                    self.deckLabel.config(image=self.computerImage)
                    self.numbers.append(self.deck)
                    self.deck = pile_popped
            increase_round_counter()
            self.root.after(2000, lambda: self.reset_background(labels_p2, self.index, backcard))

        return self.deck, labels_p2

    def reset_background(self, labels, index, backcard):
        labels[index].config(background="white")  # Reset background color to default


# Function to increase the round counter
def increase_round_counter():
    global round_counter
    round_counter += 1

# Function to get the current value of the round counter
def get_round_counter():
    return round_counter

# Initialize the counter outside the function
round_counter = 0


