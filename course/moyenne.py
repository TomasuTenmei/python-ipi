from PyQt5 import QtWidgets, QtCore, QtGui, uic
import os, sys

listeNotes = []

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "moyenne.ui"), self)
        
        mapperValue = QtCore.QSignalMapper(self)
        
        for i in range(0, 15):
            
            button = getattr(self, "pB{}".format(i))
            mapperValue.setMapping(button, i)
            button.clicked.connect(mapperValue.map)
            
        mapperValue.mapped.connect(self.composition)
        
        self.pBNext.clicked.connect(self.addition)
        
    def composition(self, value):
        
        self.labelExcept.setText("")

        text = self.labelResult.text()
        
        if value < 10:
            
            text += str(value)
            
        elif value == 10:
            
            text += "H"
            
        elif value == 11:
                
            text += "."
            
        elif value == 12:
            
            text = text[:-1]
            
        elif value == 13:
            
            text = ""
            
        elif value == 14:
            
            text = "-"
        
        self.labelResult.setText(text)
        
    def addition(self):
        
        try:
            
            newVal = self.labelResult.text()
            self.labelResult.setText("")
            
            global listeNotes, total
            listeNotes.append(newVal)
            total = 0

            for i in listeNotes:

                if float(i) > 0:
                    
                    total += float(i)
                    
                else:
                    
                    raise ValueError
                
        except ValueError:
            
            if newVal == "":
                
                app.exit()
            
            elif newVal[0] == "-":
                
                listeNotes = listeNotes[:-1]
                self.moyenne()
            
            else:
                
                self.labelExcept.setText("Vous n'avez pas rentré un nombre valide")
                listeNotes = listeNotes[:-1]

        print(listeNotes)
            
    def moyenne(self):
        
        try:
            
            result = total / len(listeNotes)
            self.labelResult.setText(str(result))
            
        except:
            
            self.labelExcept.setText("Il n'y a pas de note à calculer")
    
if __name__ == "__main__":
        
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())