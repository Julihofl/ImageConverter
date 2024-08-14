import io
import os
import wand.color
import wand.image
import tkinter as tk

from tkinter import filedialog
from pdf2image import convert_from_path
from wand.api import library
from PIL import Image
from pillow_heif import register_heif_opener
from filetypes import Filetypes
from typing import List

register_heif_opener()

class Converter:
    def __init__(self, root: tk.Tk, target: str) -> None:
        self.root: tk.Tk = root
        self.target: str = target.upper()
        self.old_extension: str  = f'.{self.target.lower()}'
        self.new_extension: str = ''
        self.valid_extensions: List[str] = [filetype.value.lower() for filetype in Filetypes]

    def convert(self) -> None:
        images_paths: List[str] = filedialog.askopenfilenames(filetypes=[("All files", "*.*")], title='Select images to convert')

        for image_path in images_paths:
            self.new_extension: str = os.path.splitext(image_path)[1][1:].lower()
            if self.new_extension not in self.valid_extensions:
                print(f"Unsupported file type: {self.new_extension}")
                continue

            try:
                self._convert_file(image_path)
            except Exception as e:
                print(f"Fehler bei der Verarbeitung von {image_path}: {e}")
        
        self.root.destroy()

    def _convert_file(self, image_path: str) -> None:
        if self.target == 'WEBP':
            self._convert_webp(image_path)
        elif self.target == 'SVG':
            self._convert_svg(image_path)
        elif self.target == 'PDF':
            self._convert_pdf(image_path)
        else:
            self._convert_image(image_path)

    def _convert_webp(self, image_path: str) -> None:
        image: Image = Image.open(image_path).convert('RGB')
        self._save_image(image, image_path)

    def _convert_svg(self, image_path: str) -> None:
        with io.open(image_path, "rb") as svg_file:
            with wand.image.Image() as image:
                with wand.color.Color('transparent') as background_color:
                    library.MagickSetBackgroundColor(image.wand, background_color.resource)
                image.read(blob=svg_file.read(), format="svg")
                png_image: bytes = image.make_blob("png32")
        
        image_path = image_path.replace(self.new_extension, self.old_extension)
        with open(image_path, "wb") as out:
            out.write(png_image)

    def _convert_pdf(self, image_path: str) -> None:
        pages = convert_from_path(image_path)
        for idx, page in enumerate(pages):
            temp_path = f"{image_path.removesuffix(self.new_extension)}_{idx + 1}{self.old_extension}"
            page.save(temp_path, self.target)

    def _convert_image(self, image_path: str) -> None:
        image: Image = Image.open(image_path)
        self._save_image(image, image_path)

    def _save_image(self, image: Image, image_path: str) -> None:
        image_path = image_path.replace(self.new_extension, self.old_extension)
        image.save(image_path, format=self.target)
