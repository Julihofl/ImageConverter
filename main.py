import webbrowser
import sv_ttk as sv
import tkinter as tk

from tkinter import ttk
from filetypes import Filetypes
from converter import Converter

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Image Converter')
        self.root.iconbitmap('images\\icon.ico')

        sv.set_theme("dark")
        self.center_window(self.root, width_offset=100, height_offset=-35)

        self.create_widgets()
        root.mainloop()

    def center_window(self, window, width_offset=0, height_offset=0):
        window.update()
        window.minsize(window.winfo_width() + width_offset, window.winfo_height() + height_offset)
        x_cordinate = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
        y_cordinate = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
        window.geometry(f"+{x_cordinate}+{y_cordinate - 20}")
        window.resizable(False, False)

    def create_widgets(self):
        # About button
        button_help = ttk.Button(self.root, text='About', command=self.open_about_window)
        button_help.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky='nw')

        # Filetype to convert to
        self.current_to = tk.StringVar(value=Filetypes.PNG.value)
        options_to = sorted(option.value for option in Filetypes if option.value not in {"JPG", "HEIC", "SVG", "TIF"})
        label_to = ttk.Label(self.root, text='File type to convert to:')
        label_to.grid(row=2, column=0, pady=15, padx=10)
        optionmenu_to = ttk.OptionMenu(self.root, self.current_to, self.current_to.get(), *options_to)
        optionmenu_to.grid(row=2, column=1, padx=20)

        # Convert button
        self.converter = Converter(self.root, self.current_to.get())
        button_convert = ttk.Button(self.root, text='Choose files', command=self.convert_files)
        button_convert.grid(row=3, column=0, columnspan=2, pady=10)

    def convert_files(self):
        """
        Startet den Konvertierungsprozess basierend auf der Auswahl.
        """
        self.converter.target = self.current_to.get()
        self.converter.convert()


    def open_about_window(self):
        about_window = tk.Toplevel(self.root)
        self.center_window(about_window, width_offset=100, height_offset=-35)
        about_window.title('About')
        about_window.iconbitmap('images\\icon.ico')

        label = tk.Label(about_window, text='\n\nVersion 1.1\n\n2023')
        label.pack()

        link = tk.Label(about_window, text='\nhttps://github.com/Julihofl/ImageConverter', fg="blue", cursor="hand2")
        link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/Julihofl/ImageConverter"))
        link.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageConverterApp(root)
