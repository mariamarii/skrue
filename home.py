import tkinter
from PIL import Image, ImageTk
import random

# Create a list of numbers from 1 to 10 repeated 4 times
numbers = list(range(1, 11)) * 4

# Shuffle the list to randomize the order
random.shuffle(numbers)

# Define a function to pick 4 numbers for a player
def pick_numbers():
    return [numbers.pop() for _ in range(4)]

# Assign numbers to players
p1 = pick_numbers()
p2 = pick_numbers()

# Function to flip the image when clicked
def flip_image(event, player, index):
    # Get the label that was clicked
    clicked_label = event.widget
    # If the player is 1 and the game is not started yet, flip the image
    if player == "p1" and not game_started:
        clicked_label.config(image=player_images_p1[index])
    # If the player is 1 and the game has started, do nothing
    elif player == "p1" and game_started:
        pass
    # If the player is 2, flip the image
    elif player == "p2":
        clicked_label.config(image=player_images_p2[index])

# Function to start the game
def start_game():
    global game_started
    game_started = True
    # Disable event binding for player 1 labels
    for label in labels_p1:
        label.unbind("<Button-1>")
    # Disable event binding for player 2 labels
    for label in labels_p2:
        label.unbind("<Button-1>")
    # Flip back the cards of player 1
    flip_back_player1()
    # Hide the start button
    start_button.place_forget()
    # Start player 1's turn
    player1_turn()

# Function to handle player 1's turn
def player1_turn():
    global center_card_image
    # Show the center card to player 1 (face side)
    center_card_image.config(image=center_image_p1)
    center_card_image.place(x=700, y=300)
    # Enable event binding for player 1 labels
    for i, label in enumerate(labels_p1):
        label.bind("<Button-1>", lambda event, index=i: replace_or_discard(event, index, "p1"))

# Function to handle player 2's turn
def player2_turn():
    global center_card_image
    # Show the center card to player 2 (flip side)
    center_card_image.config(image=back_image_p2)
    center_card_image.place(x=700, y=300)
    # Enable event binding for player 2 labels
    for i, label in enumerate(labels_p2):
        label.bind("<Button-1>", lambda event, index=i: replace_or_discard(event, index, "p2"))

# Function to handle card replacement or discard
def replace_or_discard(event, index, player):
    if player == "p1":
        # Replace the center card with player 1's selected card
        center_card_image.config(image=player_images_p1[index])
        # Update player 1's card with the center card
        player_images_p1[index] = center_card_image
        # Flip the replaced card back
        labels_p1[index].config(image=player_images_p1[index])
        # Move to player 2's turn
        player2_turn()
    elif player == "p2":
        pass  # Implement player 2's turn logic here

# create window
win = tkinter.Tk()
win.title("First Window")
win.geometry("1500x1024")
win.resizable(width=True, height=False)
win.configure(bg='#000fff000')  # change color

# Load image for back of cards
back_image = ImageTk.PhotoImage(Image.open(r"img\cardback.gif").resize((120,120)))

# Load image for center card for player 1 (face side)
center_image_p1 = back_image

# Load image for center card for player 2 (flip side)
back_image_p2 = back_image

# Create labels for player 1
labels_p1 = []
for i in range(4):
    label = tkinter.Label(win, image=back_image)
    label.place(x=50 + i * 150, y=600) # Adjusted y-coordinate for player 1
    labels_p1.append(label)
# Disable event binding for other cards of player 1

def flip_back_player1():
    for label in flipped_labels_p1:
        label.config(image=back_image)


# Create labels for player 2
labels_p2 = []
for i in range(4):
    label = tkinter.Label(win, image=back_image)
    label.place(x=600 + i * 150, y=100)
    labels_p2.append(label)

# Create a start button
start_button = tkinter.Button(win, text="Start", command=start_game)
start_button.place(x=700, y=500)

# Flag to track if the game has started
game_started = False

# Create a label for the center card
center_card_image = tkinter.Label(win, image=back_image)

win.mainloop()
