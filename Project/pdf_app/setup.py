application_title="labelingApp" ######Name
main_python_file="PDF_tkinter.py"######Name of the program to compile
icon="icon.ico"#####Icon of the application
include_files=["icon.ico"]####other images
your_name="Saloni Sharma"
program_description="An Legal document labeling and summarizing app"#Describe your program

#main
import sys
from cx_Freeze import setup, Executable
base=None
if sys.platform=="win32":
    base="Win32GUI"

setup(
    name=application_title,
    version="1.0",
    description=program_description,
    author=your_name,
    options={"build_exe":{"icon":icon, "include_files": include_files}},
    executables=[Executable(main_python_file,base=base, icon="icon.ico")])
