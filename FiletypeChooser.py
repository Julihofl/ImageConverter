import tkinter as tk
from tkinter import filedialog
from filetypes import FileTypes
from genericconverter import GenericConverter

root = tk.Tk()
root.title('Image Converter')

root.update()
root.minsize(root.winfo_width() + 75, root.winfo_height())
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

current_from = tk.StringVar(value=FileTypes.HEIC.value)
options_from = [option.value for option in FileTypes]
options_from.sort()
tk.Label(root, text='Select a file type to convert').pack()
tk.OptionMenu(root, current_from, *options_from).pack()

current_to = tk.StringVar(value=FileTypes.PNG.value)
options_to = [option.value for option in FileTypes if option.value not in ["JPG", "HEIC", "SVG"]]
options_to.sort()
tk.Label(root, text='Select a file type to convert to').pack()
tk.OptionMenu(root, current_to, *options_to).pack()

tk.Button(root, text='Convert', command=lambda: GenericConverter.generic_converter(GenericConverter, current_from.get(), current_to.get(), root)).pack()

root.mainloop()
