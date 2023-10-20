from random import randint
import sys, os
from PyQt5 import QtWidgets, QtCore, QtGui, uic

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "more_or_less.ui"), self)
        
        self.pBfacile.clicked.connect(self.facile)
        self.pBmoyen.clicked.connect(self.moyen)
        self.pBdifficile.clicked.connect(self.difficile)
        self.pBOk.clicked.connect(self.validation)
        
        global coups
        coups = 0
        
        self.moyen()
        
    def facile(self):
        
        global min, max, nb_secret
        min = 0
        max = 10
        
        nb_secret = randint(min, max)
        
        self.pBfacile.setStyleSheet("background-color: green")
        self.pBmoyen.setStyleSheet("background-color: white")
        self.pBdifficile.setStyleSheet("background-color: white")
        
        self.sBValue.setMinimum(min)
        self.sBValue.setMaximum(max)
        
        self.textBrowser.setText("")
        
    def moyen(self):
        
        global min, max, nb_secret
        min = 0
        max = 100
        
        nb_secret = randint(min, max)
        
        self.pBfacile.setStyleSheet("background-color: white")
        self.pBmoyen.setStyleSheet("background-color: green")
        self.pBdifficile.setStyleSheet("background-color: white")
        
        self.sBValue.setMinimum(min)
        self.sBValue.setMaximum(max)
        
        self.textBrowser.setText("")
        
    def difficile(self):
        
        global min, max, nb_secret
        min = 0
        max = 1000
        nb_secret = randint(min, max)
        
        self.pBfacile.setStyleSheet("background-color: white")
        self.pBmoyen.setStyleSheet("background-color: white")
        self.pBdifficile.setStyleSheet("background-color: green")
        
        self.sBValue.setMinimum(min)
        self.sBValue.setMaximum(max)
        
        self.textBrowser.setText("")
        
    def validation(self):
        
        global guess
        guess = self.sBValue.value()
        
        self.main()
        
    def main(self):
        
        global nb_secret
        print(nb_secret)

        try:
            
            global coups
            coups += 1
            
            if guess == nb_secret:
                
                print(f"Félicitations ! Vous avez deviné le nombre {nb_secret} en {coups} coups")
                self.textBrowser.setText(f"Félicitations ! Vous avez deviné le nombre {nb_secret} en {coups} coups")
            
            elif guess < nb_secret:
                
                print("Le nombre est plus grand")
                text = self.textBrowser.toPlainText()
                self.textBrowser.setText(text + "\nLe nombre est plus grand que " + str(guess))
                
            else:
                
                print("Le nombre est plus petit")
                text = self.textBrowser.toPlainText()
                self.textBrowser.setText(text + "\nLe nombre est plus petit que " + str(guess))
                
        except ValueError:
            
            print("Veuillez entrer un nombre valide.")
            text = self.textBrowser.toPlainText()
            self.textBrowser.setText(text + "\nVeuillez entrer un nombre valide.")
                
if __name__ == "__main__":
        
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())