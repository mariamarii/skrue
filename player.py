from PIL import Image,ImageTk


class Player:
    def __init__(self, numbers):
        self.cards = []
        self.numbers = numbers
        self.deck_card_clicked=False
        self.deckLabel=None
        self.deck=0
        self.card_label=None

    def pick_numbers(self):
        self.cards = [self.numbers.pop() for _ in range(4)]
        return self.cards
    def deckCardCliked(self,deckLabel,deck):
        self.deckLabel=deckLabel
        self.deck=deck
        self.deck_card_clicked = True


    def on_player_cards_click(self, button_player_index):

        # global Player_card_clicked
        # Player_card_clicked = 1
        # switch images of two buttons
        if self.deck_card_clicked == True:
            # get the value of card of player cards that player click on it
            player_card_value = self.cards[button_player_index]

            # switch ground card value and player card value
            temp = self.deck
            self.deck= player_card_value
            player_card_value= temp

            # update the card that changed in player cards
            self.cards[button_player_index]= player_card_value
            self.card_label=ImageTk.PhotoImage(Image.open(f"img/{self.deck}.gif").resize((110, 150)))
            # change image of ground card and button clicked
            self.deckLabel.config(image=self.card_label)


            self.deck_card_clicked = False
           # Player_card_clicked = 0


    def test(self):
        return self.deck





class Computer(Player):
    def __init__(self, numbers):
        super().__init__(numbers)
        self.computerSeen=[]
        self.playerSeen=[]

    def exchangeCard(self,deckLabel,deckCard):
        self.deck=deckCard
        self.deckLabel=deckLabel
        max_value = max(self.computerSeen, key=lambda t: t[1])


        if (self.deck < 5 and self.deck < int(max_value[1])) or (self.deck < max_value[1]):

            self.computerImage=ImageTk.PhotoImage(Image.open(f"img/{self.cards[max_value[0]]}.gif").resize((110, 150)))
            deckLabel.config(image=self.computerImage)
            temp =self.deck
            self.deck=self.cards[max_value[0]]
            #index = None
            # for i, t in enumerate(self.computerSeen):
            #     if t[1] == max_value:
            #         index = t[0]
            #         self.computerSeen[i] = (t[0], temp)
            self.computerSeen[max_value[0]]=temp
            self.cards[max_value[0]]=temp



        else:
            pilepopped=self.numbers.pop(0)
            if (pilepopped < 5 and pilepopped < max_value[1]) or (pilepopped < max_value[1]):

                #insert front
                self.numbers.appened(self.deck)
                # index = 0
                # for i, t in enumerate(self.computerSeen):
                #     if t[1] == max_value:
                #         index = t[0]
                self.computerSeen[max_value[0]] = (max_value[0], pilepopped)
                self.computerImage=ImageTk.PhotoImage(Image.open(f"img/{self.cards[max_value[0]]}.gif").resize((110, 150)))
                self.deckLabel.config(image=self.computerImage)
                self.deck=self.cards[max_value[0]]
                self.cards[max_value[0]]=pilepopped

            else:
                self.computerImage=ImageTk.PhotoImage(Image.open(f"img/{pilepopped}.gif").resize((110, 150)))
                self.deckLabel.config(image=self.computerImage)
                self.numbers.appened(self.deck)
                self.deck=pilepopped

        return self.deck










