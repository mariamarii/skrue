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
# create window
win = tkinter.Tk()
win.title("First Window")
win.geometry("1500x1024")
win.resizable(width=False, height=False)
win.configure(bg='#000fff000')  # change color

# Load image
image = Image.open(r"back2.jpeg")
# Adjust image size to be smaller
image = ImageTk.PhotoImage(image)

# Create label with image
label = tkinter.Label(win, image=image)
label.pack()

# Load player images for player 1
player_images_p1 = [ImageTk.PhotoImage(Image.open(f"img\\{num}.gif").resize((120,120))) for num in p1]

# Load player images for player 2
player_images_p2 = [ImageTk.PhotoImage(Image.open(f"img\\{num}.gif").resize((120,120))) for num in p2]

# Load image for back of cards
back_image = ImageTk.PhotoImage(Image.open(r"img\cardback.gif").resize((120,120)))

# Create labels for player 1
# Create labels for player 1
labels_p1 = []
flipped_labels_p1 = []  # Store references to flipped labels for player 1
for i in range(4):
    if i >= 2:
        label = tkinter.Label(win, image=player_images_p1[i])
        flipped_labels_p1.append(label)  # Store the references to flipped labels
    else:
        label = tkinter.Label(win, image=back_image)
       # label.bind("<Button-1>", lambda event, player="p1", index=i: flip_image(event, player, index))
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

win.mainloop()
