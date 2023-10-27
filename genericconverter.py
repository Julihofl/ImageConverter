import os
# Ermitteln des aktuellen Arbeitsverzeichnisses
current_directory = os.getcwd()
# Den relativen Pfad vom aktuellen Verzeichnis aus erstellen
relative_path = os.path.join(current_directory, 'lib')
print(relative_path)
# Zum PATH-Umgebungsvariable hinzufügen
os.environ['PATH'] += ';' + relative_path

from PIL import Image
from pillow_heif import register_heif_opener
import tkinter as tk
from tkinter import filedialog
from cairosvg import svg2png
from pdf2image import convert_from_path

register_heif_opener()

class GenericConverter:
    def generic_converter(self, source, target, root):
        self.root = root
        self.root.withdraw()

        self.source = source
        self.s_extension = '.' + self.source.lower()
        self.s_filetypes = [(self.source, '*' + self.s_extension)]
        self.s_title = 'Select ' + self.source + ' files'

        self.target = target
        self.t_extension = '.' + self.target.lower()

        images_path = filedialog.askopenfilenames(defaultextension=self.s_extension, filetypes=self.s_filetypes, title=self.s_title)

        for image_path in images_path:
            match self.source:
                case 'WEBP':
                    image = Image.open(image_path).convert('RGB')
                case 'SVG':
                    image = svg2png(url=image_path, write_to=image_path.replace(self.s_extension, self.t_extension))
                    exit()
                case 'PDF':
                    image = convert_from_path(image_path)
                    for page in image:
                        image_path = image_path.removesuffix(self.s_extension)
                        image_path += '_' + str(image.index(page) + 1) + self.t_extension
                        page.save(image_path, self.target)
                    exit()
                case _:
                    image = Image.open(image_path)
            image_path = image_path.replace(self.s_extension, self.t_extension)
            image.save(image_path, format=self.target)

        exit()
