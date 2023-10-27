from PIL import Image
from pillow_heif import register_heif_opener
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from wand.api import library
import wand.color
import wand.image
import io

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
                    with io.open(image_path, "rb") as svg_file:
                        with wand.image.Image() as image:
                            with wand.color.Color('transparent') as background_color:
                                library.MagickSetBackgroundColor(image.wand, background_color.resource) 
                            image.read(blob=svg_file.read(), format="svg")
                            png_image = image.make_blob("png32")
                    image_path = image_path.replace(self.s_extension, self.t_extension)
                    with open(image_path, "wb") as out:
                        out.write(png_image)
                    exit()
                case 'PDF':
                    image = convert_from_path(image_path)
                    for page in image:
                        temp_path = image_path.removesuffix(self.s_extension)
                        temp_path += '_' + str(image.index(page) + 1) + self.t_extension
                        page.save(temp_path, self.target)
                    exit()
                case _:
                    image = Image.open(image_path)
            image_path = image_path.replace(self.s_extension, self.t_extension)
            image.save(image_path, format=self.target)

        exit()
