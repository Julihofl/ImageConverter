from cx_Freeze import setup, Executable

base = "Win32GUI"    

include_files = [("images", "images")]

executables = [Executable("imageconverter.py", base=base)]

packages = ["idna", 
            "tkinter", 
            "sv_ttk", 
            "webbrowser", 
            "filetypes", 
            "genericconverter", 
            "pillow_heif", 
            "PIL", 
            "pdf2image", 
            "wand", 
            "io"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Image Converter",
    options = options,
    version = "1.1",
    description = 'Image Converter',
    executables = executables
)
