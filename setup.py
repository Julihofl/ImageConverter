from cx_Freeze import setup, Executable

base = "Win32GUI"    

include_files = [("images", "images")]

executables = [Executable("FiletypeChooser.py", base=base)]

packages = ["idna", "tkinter", "sv_ttk", "webbrowser", "filetypes", "genericconverter", "pillow_heif", "PIL", "pdf2image", "wand", "io"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Image Converter",
    options = options,
    version = "1.0",
    description = 'Image Converter by Julian',
    executables = executables
)
