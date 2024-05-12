from PIL import Image, ImageTk
import tkinter as tk
#from gui import GUI

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
        self.actual_player_card=[]

    def pick_numbers(self):
        self.cards = [self.numbers.pop() for _ in range(4)]
        update_computer_cards(self.cards)
        return self.cards

    def pick_numbers_player(self):
        self.cards = [self.numbers.pop() for _ in range(4)]
        update_player_cards(self.cards)
        return self.cards
    def deckCardCliked(self, deckLabel, deck):
        self.deckLabel = deckLabel
        self.deck = deck
        self.deck_card_clicked = True

        if self.pile_card_clicked == True:
            self.exchangeCardPlayer()
        self.pile_card_clicked = False

    def pileCardClicked(self, root, deckLabel):
        self.deckLabelGUI = deckLabel
        if self.pile_card_clicked == False:
            self.displayPileCard(root)
        self.pile_card_clicked = True


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
        self.cards=get_player_cards()
        if self.deck_card_clicked == True and get_round_counter() % 2 == 0 and self.cards[button_player_index]!=183:
            print('player')
            player_card_value = self.cards[button_player_index]
            temp = self.deck
            self.deck = player_card_value
            player_card_value = temp
            self.cards[button_player_index] = player_card_value
            print(self.cards)
            update_player_cards(self.cards)
            self.playerSeen[button_player_index] = (button_player_index, player_card_value)
            self.card_label = ImageTk.PhotoImage(Image.open(f"img/{self.deck}.gif"))
            self.deckLabel.config(image=self.card_label)
            self.deck_card_clicked = False
            increase_round_counter()
        elif self.pile_card_clicked == True and get_round_counter() % 2 == 0 and self.cards[button_player_index]!=183:  # card exchange
            print('player2')
            # pile_popped = self.numbers.pop(0)
            self.numbers.append(self.deck)

            self.deckLabel = self.deckLabelGUI
            # self.computerSeen[max_value[0]] = (max_value[0], pile_popped)  # Update as tuple
            self.playerImage = ImageTk.PhotoImage(Image.open(f"img/{self.cards[button_player_index]}.gif"))
            self.deckLabel.config(image=self.playerImage)
            self.deck = self.cards[button_player_index]
            self.cards[button_player_index] = self.pile_pop_player
            self.playerSeen[button_player_index]=(button_player_index,15)
            print(self.cards)
            update_player_cards(self.cards)
            #self.playerSeen[button_player_index] = (button_player_index, self.deck)
            self.displayPileBack()
            self.pile_card_clicked=False
            increase_round_counter()
        elif self.deck == 7 or self.deck == 8 :
            self.Bos_f_wr2tk(button_player_index, root)
            root.after(2000, lambda: increase_round_counter())
        elif self.deck == 11:
            card =get_player_cards()
            self.k3b_dayer(button_player_index,card,root,500)
        elif self.deck == 12 or self.deck == 14:
            self.ind=button_player_index
        elif self.deck == 13:
            self.basra(button_player_index,root)
            increase_round_counter()


    def Bos_f_wr2tk(self, index, root):
        if self.cards[index] != 183 and self.cards[index]!=-77:
            start_x = (1500 - (len(self.cards) * 150)) // 2
            card_image = ImageTk.PhotoImage(Image.open(f"img/{self.cards[index]}.gif"))
            my_label = tk.Label(root, image=card_image)
            my_label.image = card_image
            my_label.place(x=start_x + index * 150, y=500)
            root.after(2000, lambda: self.delay_forget_label(my_label))


    def delay_forget_label(self, label):
        label.place_forget()

    def exchangeCardPlayer(self):  # card exchange
        self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{self.pile_pop_player}.gif"))
        self.deckLabel.config(image=self.computerImage)
        self.numbers.append(self.deck)
        self.deck = self.pile_pop_player
        self.displayPileBack()
        self.deck_card_clicked=False
        if self.deck != 7 and self.deck != 8 and self.deck != 9 and self.deck != 10 and self.deck != 11 and self.deck != 12 and self.deck != 13 and self.deck != 14:
            increase_round_counter()

    def on_computer_cards_click(self, button_computr_index, nums,root):
        if self.deck ==9 or self.deck ==10 :
            self.Bos_f_wr2t_8erk(button_computr_index, nums, root)
            increase_round_counter()
        elif self.deck == 11:
            self.k3b_dayer(button_computr_index,nums,root,150)
            increase_round_counter()
        elif self.deck == 12:
            self.khod_w_hat(self.ind,button_computr_index)
            increase_round_counter()
        elif self.deck == 14 :
            self.see_swap(self.ind,button_computr_index, root)
            increase_round_counter()

    def Bos_f_wr2t_8erk(self, index,nums, root):
        #print("nums")
        #print(nums)
        start_x = (1500 - (len(self.cards) * 150)) // 2
        if index != -77:
            card_image = ImageTk.PhotoImage(Image.open(f"img/{nums[index]}.gif"))
            my_label = tk.Label(root, image=card_image)
            my_label.image = card_image
            my_label.place(x=start_x + index * 150, y=150)
            root.after(2000, lambda: self.delay_forget_label(my_label))

    def k3b_dayer(self, index,nums, root,y):
        print("k3b player")
        #print(nums)
        if nums[index] != -77 and nums[index] != 183:
            start_x = (1500 - (len(self.cards) * 150)) // 2
            card_image = ImageTk.PhotoImage(Image.open(f"img/{nums[index]}.gif"))
            my_label = tk.Label(root, image=card_image)
            my_label.image = card_image
            my_label.place(x=start_x + index * 150, y=y)
            root.after(2000, lambda: self.delay_forget_label(my_label))

    def khod_w_hat(self,player_index,computer_index):
        print("khod player")
        computer_card=get_computer_cards()
        player_card=get_player_cards()
        if computer_card[computer_index] != -77 and player_card[player_index] != 183:
            temp=self.playerSeen[player_index]
            self.playerSeen[player_index] = (player_index, self.computerSeen[computer_index][1])
            self.computerSeen[computer_index] = (computer_index, temp[1])

            self.cards[player_index] = computer_card[computer_index]
            #computer_card[computer_index] = player_card[player_index]
            computer_card[computer_index] = self.computerSeen[computer_index][1]

            # Swap the cards between player and computer at the specified indexes
            update_computer_cards(computer_card)
            print(self.cards)
            update_player_cards(self.cards)
            # Update playerSeen and computerSeen with the swapped card values
            print(self.computerSeen[computer_index])
            print(get_computer_cards())
            print(get_player_cards())

    def basra(self,index,root):
        print("basra player")
        start_x = (1500 - (len(self.cards) * 150)) // 2
        card_image = ImageTk.PhotoImage(Image.open("img/out.gif"))
        my_label = tk.Label(root, image=card_image)
        my_label.image = card_image
        my_label.place(x=start_x + index * 150, y=650)
        #root.after(2000, lambda: self.delay_forget_label(my_label))
        self.deck = self.cards[index]
        self.card_label = ImageTk.PhotoImage(Image.open(f"img/{self.deck}.gif"))
        self.deckLabel.config(image=self.card_label)
        self.playerSeen[index] = (index,183)
        self.cards[index] = 183
        print((self.cards))
        update_player_cards(self.cards)

    def see_swap(self,player_index,computer_index,root):
        computer_card = get_computer_cards()
        player_card = get_player_cards()
        self.Bos_f_wr2t_8erk(computer_index,computer_card, root)
        self.khod_w_hat(player_index,computer_index)

    def get_card(self):
        return self.cards
    def test(self):
        return self.deck

class Computer(Player):
    def __init__(self, numbers, playerSeen, computerSeen, root):
        super().__init__(numbers, playerSeen, computerSeen)
        self.screwCom = False
        self.root = root

    def exchangeCard(self, deckLabel, deckCard, labels_p2, backcard,root):

        
        self.deck = deckCard
        self.deckLabel = deckLabel
        self.cards = get_computer_cards()
        if self.screwCom == True:
            return self.deck, labels_p2, self.screwCom
        if score(self.computerSeen) < 4 and get_round_counter() > 6:
            print(score(self.computerSeen))
            self.screwCom = True
            #increase_round_counter()
            return self.deck, labels_p2, self.screwCom

        # Check if computerSeen contains tuples
        if not all(isinstance(item, tuple) for item in self.computerSeen):
            print("Error: computerSeen does not contain tuples")
            return self.deck, labels_p2, self.screwCom

        # Find maximum value from computerSeen
        max_value = max(self.computerSeen, key=lambda t: t[1])
        filtered_tuples = [(x, y) for (x, y) in self.playerSeen if y < 183]
        max_value_player = max(filtered_tuples, key=lambda t: t[1])
        min_value_player = min(self.playerSeen, key=lambda t: t[1])
        if get_round_counter() % 2 != 0:
            print('computer')
            print(self.computerSeen)
            print(self.playerSeen)
            self.cards = get_computer_cards()

            if (self.deck < 5 and self.deck < int(max_value[1])) or (self.deck < max_value[1]):
                self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{self.cards[max_value[0]]}.gif"))
                self.index = max_value[0]
                labels_p2[self.index].config(image = backcard, background = "#E5A82E")
                deckLabel.config(image=self.computerImage)
                temp = self.deck
                self.deck = self.cards[max_value[0]]
                self.computerSeen[max_value[0]] = (max_value[0], temp)  # Update as tuple
                self.cards[max_value[0]] = temp
                update_computer_cards(self.cards)
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
                    update_computer_cards(self.cards)
                else:
                    self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{pile_popped}.gif"))
                    self.deckLabel.config(image=self.computerImage)
                    self.numbers.append(self.deck)
                    self.deck = pile_popped

                    if self.deck == 7 or self.deck==8:
                        self.computerSeen[max_value[0]]= (max_value[0],self.cards[max_value[0]])
                    elif self.deck ==9 or self.deck==10:
                        card=get_player_cards()
                        self.playerSeen[max_value_player[0]] = (max_value_player[0],card[max_value_player[0]])
                    elif self.deck ==11:
                        print("k3b computer")
                        card = get_player_cards()
                        self.playerSeen[max_value_player[0]] = (max_value_player[0], card[max_value_player[0]])
                        self.computerSeen[max_value[0]] = (max_value[0], self.cards[max_value[0]])
                    elif self.deck == 12 or self.deck == 14:
                        card = get_player_cards()
                        computer_c = get_computer_cards()
                        if self.deck ==14:
                            self.computerSeen[max_value[0]] = (max_value[0], card[min_value_player[0]])
                        else:
                            self.computerSeen[max_value[0]] = (max_value[0], min_value_player[1])

                        self.playerSeen[min_value_player[0]]=(min_value_player[0],max_value[1])

                        self.cards[max_value[0]]=card[min_value_player[0]]

                        card[min_value_player[0]]=computer_c[max_value[0]]

                        update_computer_cards(self.cards)
                        update_player_cards(card)
                    elif self.deck == 13:
                        print("basra comp")
                        start_x = (1500 - (len(self.cards) * 150)) // 2
                        card_image = ImageTk.PhotoImage(Image.open("img/out.gif"))
                        my_label = tk.Label(root, image=card_image)
                        my_label.image = card_image
                        my_label.place(x=start_x + max_value[0] * 150, y=50)
                        self.computerImage = ImageTk.PhotoImage(Image.open(f"img/{self.computerSeen[max_value[0]][1]}.gif"))
                        self.deckLabel.config(image=self.computerImage)
                        self.numbers.append(self.deck)
                        self.deck = self.computerSeen[max_value[0]]
                        # root.after(2000, lambda: self.delay_forget_label(my_label))
                        self.computerSeen[max_value[0]] = (max_value[0], -77)
                        self.cards[max_value[0]] = -77
                        update_computer_cards(self.cards)

            increase_round_counter()
            self.root.after(2000, lambda: self.reset_background(labels_p2, self.index, backcard))
        return self.deck, labels_p2, self.screwCom

    def reset_background(self, labels, index, backcard):
        labels[index].config(background="white")  # Reset background color to default


# Function to increase the round counter
def increase_round_counter():
    global round_counter
    round_counter += 1

# Function to get the current value of the round counter
def get_round_counter():
    return round_counter
def update_player_cards(cards):
    global player_cards
    player_cards = cards
def get_player_cards():
    #global player_cards
    return player_cards
def update_computer_cards(cards):
    global computer_cards
    computer_cards = cards
def get_computer_cards():
    #global player_cards
    return computer_cards
def score(cards):
    sum = 0
    for i in range(0, 4):
        if cards[i][1] != 183 and cards[i][1] != -77:
            if cards[i][1] > 10 and cards[i][1] < 15:
                sum = sum + 10
            else:
                sum = sum + cards[i][1]
    return sum


# Initialize the counter outside the function
round_counter = 0
player_cards=[]
computer_cards=[]


