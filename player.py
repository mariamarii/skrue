from PIL import Image,ImageTk


class Player:
    def __init__(self, numbers):
        self.cards = []
        self.numbers = numbers

    def pick_numbers(self):
        self.cards = [self.numbers.pop() for _ in range(4)]
        return self.cards

class Computer(Player):
    def __init__(self, numbers):
        super().__init__(numbers)
        self.computerSeen=[]
        self.playerSeen=[]

    def exchangeCard(self,deckCard,deckLabel):
        max_value = max(t[1] for t in self.computerSeen)

        if (deckCard < 5 and deckCard < int(max_value)) or (deckCard < max_value):
            self.computerImage=ImageTk.PhotoImage(Image.open(f"img/{max_value}.gif").resize((110, 150)))
            deckLabel.config(image=self.computerImage)
            index = None
            for i, t in enumerate(self.computerSeen):
                if t[1] == max_value:
                    index = t[0]
                    self.computerSeen[i] = (t[0], deckCard)
            self.cards[index]=deckCard

        else:
            pilepopped=self.numbers.pop()
            if (pilepopped < 5 and pilepopped < max_value) or (pilepopped < max_value):

                #insert front
                self.numbers.insert(0,deckCard)
                index = 0
                for i, t in enumerate(self.computerSeen):
                    if t[1] == max_value:
                        index = t[0]
                        self.computerSeen[i] = (t[0], pilepopped)
                self.computerImage=ImageTk.PhotoImage(Image.open(f"img/{self.cards[index]}.gif").resize((110, 150)))
                deckLabel.config(image=self.computerImage)
                self.cards[index]=pilepopped

            else:
                self.computerImage=ImageTk.PhotoImage(Image.open(f"img/{pilepopped}.gif").resize((110, 150)))
                deckLabel.config(image=self.computerImage)
                self.numbers.append(deckCard)












