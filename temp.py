# import tkinter as tk
#
#
# class SwitchingApp(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#
#         for F in (StartPage, SecondPage):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             self.frames[page_name] = frame
#
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("StartPage")
#
#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#
# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         label = tk.Label(self, text="This is the start page")
#         label.pack(side="top", fill="x", pady=10)
#
#         button = tk.Button(self, text="Go to Second Page",
#                            command=lambda: controller.show_frame("SecondPage"))
#         button.pack()
#
#
# class SecondPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#
#         label = tk.Label(self, text="This is the second page")
#         label.pack(side="top", fill="x", pady=10)
#
#         button = tk.Button(self.root, text="Click Me", command=lambda: controller.show_frame("StartPage"), borderwidth=0, highlightthickness=0, relief="flat", bg="blue", fg="white")
#
#         button.pack()
#
#
# if __name__ == "__main__":
#     app = SwitchingApp()
#     app.mainloop()
# import tkinter as tk
# from PIL import Image, ImageTk, ImageDraw
#
# def round_corners(image_path, radius):
#     # Open the image using PIL
#     image = Image.open(image_path).convert("RGBA")
#
#     # Create a mask with rounded corners
#     mask = Image.new("L", image.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.rounded_rectangle((10, 3, image.width - 10, image.height - 3), radius, fill=255)
#
#     # Apply the mask to the image
#     image.putalpha(mask)
#
#     return image
#
# root = tk.Tk()
#
# # Replace 'image_path' with the path to your image
# image_path = "img/-5.gif"
# radius = 10  # Adjust the radius as needed
#
# rounded_image = round_corners(image_path, radius)
# tk_image = ImageTk.PhotoImage(rounded_image)
#
# label = tk.Label(root, image=tk_image)
# label.pack()
#
# root.mainloop()
import tkinter as tk

def draw_border(canvas, image_item, border_color="black", border_width=0):
    x0, y0, x1, y1 = canvas.bbox(image_item)
    # Draw the border closer to the image
    canvas.create_rectangle(x0, y0, x1, y1, outline=border_color, width=border_width)

root = tk.Tk()
root.title("Image with Border")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Load the image
image_path = "img/25.gif"
image = tk.PhotoImage(file=image_path)

# Display the image on the canvas
image_item = canvas.create_image(200, 150, image=image, anchor="center")

# Draw a border around the image with increased thickness
draw_border(canvas, image_item, border_width=5)

# root.mainloop()
