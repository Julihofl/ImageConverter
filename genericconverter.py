from PIL import Image
from pillow_heif import register_heif_opener
import tkinter as tk
from tkinter import filedialog
from cairosvg import svg2png

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
                    image = svg2png(url=image_path, write_to=image_path.replace(self.s_extension, '.png'))
                    exit()
                case _:
                    image = Image.open(image_path)
            image_path = image_path.replace(self.s_extension, self.t_extension)
            image.save(image_path, format=self.target)

        exit()
