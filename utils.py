import os 
import pyperclip


class Utils:
    __path = os.path.dirname(os.path.abspath(__file__)) 


    def saveBooferText(self, fileName):
        with open(self.__path + "src" +fileName, "w") as file:
            file.write(pyperclip.paste() + "\n" + "\n" + "----------------------------------------------------------------------------------------------------------" + "\n" + "\n")


