from cx_Freeze import setup, Executable 
 
base = None     
 
executables = [Executable("main.py", base=base)] 
 
packages = ["idna"] 
options = { 
    'build_exe': {     
        'packages':packages, 
    },     
} 
 
setup( 
    name = "DownloadImages", 
    options = options, 
    version = "1.0", 
    description = 'Download n number of images for google', 
    executables = executables 
) 