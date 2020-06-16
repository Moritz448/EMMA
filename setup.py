from cx_Freeze import setup, Executable

setup(name = "EMMA" ,
      version = "1.6.0" ,
      description = "https://github.com/Moritz448/EMMA" ,
      executables = [Executable(script="main.py",icon="icon.ico")])