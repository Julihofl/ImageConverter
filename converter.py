import io
import os
import wand.color
import wand.image

from tkinter import filedialog
from pdf2image import convert_from_path
from wand.api import library
from PIL import Image
from pillow_heif import register_heif_opener
from filetypes import Filetypes

register_heif_opener()

class Converter:
    def __init__(self, root, target):
        self.root = root
        self.target = target.upper()
        self.extension = f'.{self.target.lower()}'
        self.valid_extensions = [filetype.value.lower() for filetype in Filetypes]

    def convert(self):
        images_path = filedialog.askopenfilenames(defaultextension=self.extension, filetypes=[("All files", "*.*")], title='Select images to convert')

        for image_path in images_path:
            extension = os.path.splitext(image_path)[1][1:].lower()
            if extension not in self.valid_extensions:
                print(f"Unsupported file type: {extension}")
                continue

            try:
                self._convert_file(image_path, extension)
            except Exception as e:
                print(f"Fehler bei der Verarbeitung von {image_path}: {e}")
        
        self.root.destroy()

    def _convert_file(self, image_path, extension):
        if self.target == 'WEBP':
            self._convert_webp(image_path, extension)
        elif self.target == 'SVG':
            self._convert_svg(image_path, extension)
        elif self.target == 'PDF':
            self._convert_pdf(image_path, extension)
        else:
            self._convert_image(image_path, extension)

    def _convert_webp(self, image_path, extension):
        image = Image.open(image_path).convert('RGB')
        self._save_image(image, image_path, extension)

    def _convert_svg(self, image_path, extension):
        with io.open(image_path, "rb") as svg_file:
            with wand.image.Image() as image:
                with wand.color.Color('transparent') as background_color:
                    library.MagickSetBackgroundColor(image.wand, background_color.resource)
                image.read(blob=svg_file.read(), format="svg")
                png_image = image.make_blob("png32")
        
        image_path = image_path.replace(extension, self.extension)
        with open(image_path, "wb") as out:
            out.write(png_image)

    def _convert_pdf(self, image_path, extension):
        pages = convert_from_path(image_path)
        for idx, page in enumerate(pages):
            temp_path = f"{image_path.removesuffix(extension)}_{idx + 1}{self.extension}"
            page.save(temp_path, self.target)

    def _convert_image(self, image_path, extension):
        image = Image.open(image_path)
        self._save_image(image, image_path, extension)

    def _save_image(self, image, image_path, extension):
        image_path = image_path.replace(extension, self.extension)
        image.save(image_path, format=self.target)
