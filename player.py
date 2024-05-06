from PIL import Image, ImageTk

class Player:
    def __init__(self, numbers):
        self.cards = []
        self.numbers = numbers
        self.deck_card_clicked = False
        self.deckLabel = None
        self.role = False
        self.deck = 0
        self.card_label = None

    def pick_numbers(self):
        self.cards = [self.numbers.pop() for _ in range(4)]
        return self.cards

    def deckCardCliked(self, deckLabel, deck):
        self.deckLabel = deckLabel
        self.deck = deck
        self.deck_card_clicked = True

    def on_player_cards_click(self, button_player_index):
        if self.deck_card_clicked == True and get_round_counter() % 2 == 0:
            print('player')
            player_card_value = self.cards[button_player_index]
            temp = self.deck
            self.deck = player_card_value
            player_card_value = temp
            self.cards[button_player_index] = player_card_value
            self.card_label = ImageTk.PhotoImage(Image.open(f"img/{self.deck}.gif"))
            self.deckLabel.config(image=self.card_label)
            self.deck_card_clicked = False
            increase_round_counter()

    def test(self):
        return self.deck

class Computer(Player):
    def __init__(self, numbers):
        super().__init__(numbers)
        self.computerSeen = []
        self.playerSeen = []

    def exchangeCard(self, deckLabel, deckCard):
        self.deck = deckCard
        self.deckLabel = deckLabel

        # Check if computerSeen contains tuples
        if not all(isinstance(item, tuple) for item in self.computerSeen):
            print("Error: computerSeen does not contain tuples")
            return self.deck

        # Find maximum value from computerSeen
        max_value = max(self.computerSeen, key=lambda t: t[1])

        if get_round_counter() % 2 != 0:
            print('computer')
            if (self.deck < 5 and self.deck < int(max_value[1])) or (self.deck < max_value[1]):
                self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{self.cards[max_value[0]]}.gif"))
                deckLabel.config(image=self.computerImage)
                temp = self.deck
                self.deck = self.cards[max_value[0]]
                self.computerSeen[max_value[0]] = (max_value[0], temp)  # Update as tuple
                self.cards[max_value[0]] = temp
            else:
                pile_popped = self.numbers.pop(0)
                if (pile_popped < 5 and pile_popped < max_value[1]) or (pile_popped < max_value[1]):
                    self.numbers.append(self.deck)
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
        return self.deck

# Function to increase the round counter
def increase_round_counter():
    global round_counter
    round_counter += 1

# Function to get the current value of the round counter
def get_round_counter():
    return round_counter

# Initialize the counter outside the function
round_counter = 0
