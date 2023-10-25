import tkinter as tk
import sv_ttk as sv
from tkinter import ttk
from filetypes import FileTypes
from genericconverter import GenericConverter

def main():
    root = tk.Tk()
    root.title('Image Converter')
    root.iconbitmap('images\\icon.ico')

    sv.set_theme("dark")

    root.update()
    root.minsize(root.winfo_width() + 100, root.winfo_height() - 35)
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))
    root.resizable(False, False)

    current_from = tk.StringVar()
    default_from = FileTypes.HEIC.value
    options_from = [option.value for option in FileTypes]
    options_from.sort()

    label_from = ttk.Label(root, text='File type to convert from:')
    label_from.grid(row=0, column=0, pady=15, padx=10)
    optionmenu_from = ttk.OptionMenu(root, current_from, default_from, *options_from)
    optionmenu_from.grid(row=0, column=1, padx=20)

    current_to = tk.StringVar()
    default_to = FileTypes.PNG.value
    options_to = [option.value for option in FileTypes if option.value not in ["JPG", "HEIC", "SVG", "TIF"]]
    options_to.sort()

    label_to = ttk.Label(root, text='File type to convert to:')
    label_to.grid(row=1, column=0, pady=15, padx=10)
    optionmenu_to = ttk.OptionMenu(root, current_to, default_to, *options_to)
    optionmenu_to.grid(row=1, column=1, padx=20)

    button_convert = ttk.Button(root, text='Convert', command=lambda: GenericConverter.generic_converter(GenericConverter, current_from.get(), current_to.get(), root))
    button_convert.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()