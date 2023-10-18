import tkinter.filedialog
from tkinter import *
from tkinter import Tk, messagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont


def savefile():
    """Saves the watermarked image in a location chosen by you, with a name of your choice..."""
    filetypes = (('Image File', '*.png *.jpg *.jpeg *.pdf'), ('All files', '*.*'))
    filename = tkinter.filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=".png")
    img.save(f"{filename}")
    messagebox.showinfo("saved", "The photo has been saved")


class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Watermarker")
        self.geometry("1920x1080")
        self.label_text()
        self.button()
        self.mainloop()

    def label_text(self):
        label = Label(self, text='Add a watermark', font=("ShadowHand", 24, "bold"))
        label.place(x=500, y=40)

    def button(self):
        button = Button(self, text="Upload Image", font=("Magneto", 18), relief="groove", command=self.upload_img)
        button.place(x=520, y=100)

    def download_button(self):
        button = Button(self, text="Download new Image", relief="groove", font=18, command=savefile)
        button.place(x=530, y=580)

    def upload_img(self):
        global label_img
        global img
        filename = tkinter.filedialog.askopenfilename()
        img = Image.open(filename)
        li = ImageDraw.Draw(img)
        my_font = ImageFont.truetype('ShadowHand.ttf', 65)
        li.text((0, 0), text="Oluwagbeminiyi", fill=(255, 0, 0), font=my_font, )
        # img.show()
        image_resized = img.resize((300, 400))
        label_img = ImageTk.PhotoImage(image_resized)
        label = Label(self, image=label_img, )
        label.place(x=480, y=150)
        self.download_button()


if __name__ == "__main__":
    app = App()
