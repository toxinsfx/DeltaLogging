from pystyle import Colors, Colorate
import os
import platform

class Logger:
    @staticmethod
    def info(text):
        print(Colors.cyan + text)

    @staticmethod
    def error(text):
        print(Colors.red + text)

    @staticmethod
    def warning(text):
        print(Colors.yellow + text)

    @staticmethod
    def print(text, color):
        color2 = getattr(Colors, color)
        print(str(color2) + str(text))

class Utils:
    @staticmethod
    def cls():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    @staticmethod
    def title(titletext):
        if platform.system() == "Windows":
            os.system("title " + titletext)
        else:
            print(f'\33]0;{titletext}\a', end='', flush=True)
    @staticmethod
    def cmd(cmd):
        os.system(cmd)
