from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, os

from caesar_cipher import encrypt, deciphering


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        
        super(MainWindow, self).__init__(*args, **kwargs)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "ui_caesar_cipher.ui"), self)
        
        self.spinBox_chiffre.valueChanged.connect(self.encrypt)
        self.lineEdit_chiffre.textChanged.connect(self.encrypt)
        self.spinBox_dechiffre.valueChanged.connect(self.deciphering)
        self.lineEdit_dechiffre.textChanged.connect(self.deciphering)

    def encrypt(self):
        
        msg = self.lineEdit_chiffre.text()
        number = self.spinBox_chiffre.value()
        encrypted_msg = encrypt(msg, number)
        self.label_chiffre.setText(encrypted_msg)
        
    def deciphering(self):
        
        msg = self.lineEdit_dechiffre.text()
        number = self.spinBox_dechiffre.value()
        decrypted_msg = deciphering(msg, number)
        self.label_dechiffre.setText(decrypted_msg)

if __name__ == "__main__":
        
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
