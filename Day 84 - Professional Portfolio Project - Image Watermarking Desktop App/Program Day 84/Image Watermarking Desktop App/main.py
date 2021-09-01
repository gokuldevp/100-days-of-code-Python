import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw


class WatermarkApp(tk.Frame):
    """WatermarkApp - App to Add Watermarking to Images."""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Image Watermarking Desktop App")
        self.master.minsize(1000, 400)

        self.image_path1 = "default.jpg"
        self.img_width = 1
        self.img_height = 1
        # label
        self.text_label = tk.Label(text="Enter the text for Watermarking:", font=("Times New Roman", 15))
        self.original_label = tk.Label(text="Original Image:", font=("Akzidenz-Grotesk", 12))
        self.watermark_label = tk.Label(text="Watermarking image:", font=("Akzidenz-Grotesk", 12))
        # entry
        self.watermark_entry = tk.Entry()
        # canvas
        self.canvas = tk.Canvas(self.master, width=500, height=300, bg="white")
        self.canvas2 = tk.Canvas(self.master, width=500, height=300, bg="white")
        # images
        self.image1 = Image.open(self.image_path1).resize((500, 300))
        self.image2 = self.image1
        self.image_tk1 = ImageTk.PhotoImage(self.image1)
        self.image_tk2 = ImageTk.PhotoImage(self.image2)
        self.image_id1 = self.canvas.create_image(250, 150, image=self.image_tk1)
        self.image_id2 = self.canvas2.create_image(250, 150, image=self.image_tk2)
        # buttons
        self.image_button = tk.Button(text="Select Image Click Here", command=self.get_image)
        self.watermark_button = tk.Button(text="Watermark Text", command=self.watermark)
        self.save_button = tk.Button(text="Save Image", command=self.save_image)
        # widget config
        self.widget_config()

    def widget_config(self):
        """Configuration the Widget"""
        # button config
        self.image_button.config(padx=38)
        self.watermark_button.config(padx=38)
        self.save_button.config(padx=38)
        # grid
        self.text_label.grid(column=2, row=0)
        self.original_label.grid(column=0, row=2, columnspan=2)
        self.watermark_label.grid(column=2, row=2, columnspan=2)
        self.watermark_entry.grid(column=3, row=0)
        self.canvas.grid(column=0, row=3, columnspan=2)
        self.canvas2.grid(column=2, row=3, columnspan=2)
        self.image_button.grid(column=0, row=0, columnspan=2)
        self.watermark_button.grid(column=2, row=4)
        self.save_button.grid(column=3, row=4)

    def get_image(self):
        """Get Image Path and and show the the image"""
        try:
            # getting image from file
            self.image_path1 = filedialog.askopenfilename(initialdir="/", title="Choose Image File", filetypes=(('IMAGE', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif', '*.png', '*.bmp', '*.jdib')), ('GIF', '*.gif')))
            self.image1 = Image.open(self.image_path1)
        except AttributeError:
            pass

        # resizing image and showing selected image
        self.image1 = self.image1.resize((500, 300))
        self.image_tk1 = ImageTk.PhotoImage(self.image1)
        self.canvas.itemconfig(self.image_id1, image=self.image_tk1)

    def watermark(self):
        """Function to Add Watermark to the Image"""
        # resizing image and showing the Watermarked Image
        self.image2 = self.image1.resize((500, 300))
        watermark_text = self.watermark_entry.get()
        draw = ImageDraw.Draw(self.image2)
        draw.text((5, 5), f"{watermark_text}", (150, 150, 150),)
        self.image_tk2 = ImageTk.PhotoImage(self.image2)
        self.canvas2.itemconfig(self.image_id2, image=self.image_tk2)

    def save_image(self):
        """Function to Save Image as .png format"""
        # Save the Final Watermarked in selected path in .png format
        final_image = self.image2
        final = self.image2.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",)
        final_image.save(f"{final}.png")


root = tk.Tk()
app = WatermarkApp(root)
app.mainloop()
