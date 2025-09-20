import os
import img2pdf
import tkinter as tk
from tkinter import filedialog, messagebox

SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".gif")

def convert_images_to_pdf(img_paths):
    try:
        output_dir = os.path.dirname(img_paths[0])
        output_file = os.path.join(output_dir, "output.pdf")
        
        with open(output_file, "wb") as f:
            f.write(img2pdf.convert(img_paths))
        
        messagebox.showinfo("Success", f"PDF saved at:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_files():
    filepaths = filedialog.askopenfilenames(
        title="Select Image Files",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.tiff *.bmp *.gif")]
    )
    if filepaths:
        convert_images_to_pdf(filepaths)

root = tk.Tk()
root.title("img2pdf")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="select your image 🖼️")
label.pack(pady=10)

btn_files = tk.Button(frame, text="Select Images", command=select_files, width=20)
btn_files.pack(pady=5)

root.mainloop()
