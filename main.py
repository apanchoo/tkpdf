import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PyPDF2 import PdfMerger
import os
import sys

def convert_img_to_pdf(file_path, pdf_path):
    image = Image.open(file_path)
    image.save(pdf_path, "PDF", resolution=100.0)
    return pdf_path

def merge_pdfs(files, output_path):
    merger = PdfMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    return output_path

def gui_convert_img_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if pdf_path:
            result = convert_img_to_pdf(file_path, pdf_path)
            print(f"Image converted to PDF: {result}")

def gui_merge_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if files:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_path:
            result = merge_pdfs(files, output_path)
            print(f"PDFs merged into: {result}")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("PDF Utility")
    root.geometry("400x200")

    # Définir l'icône de la fenêtre
    icon_path = resource_path('icon.ico')
    root.iconbitmap(icon_path)

    # Créer les boutons
    button_convert = tk.Button(root, text="Convert img to PDF", command=gui_convert_img_to_pdf, width=20, height=5)
    button_merge = tk.Button(root, text="Merge PDF", command=gui_merge_pdfs, width=20, height=5)

    # Placer les boutons
    button_convert.pack(side="left", expand=True, padx=10, pady=10)
    button_merge.pack(side="right", expand=True, padx=10, pady=10)

    # Lancer la boucle principale de l'application
    root.mainloop()
