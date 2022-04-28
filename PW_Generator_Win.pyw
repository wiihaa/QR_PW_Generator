import secrets
import string
import qrcode
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd


numbers=[]
passwords=[]


class Ui_Dialog(object):


    def generate(self, length, name, i):

        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        numbers.append(i)
        passwords.append(password)

        img = qrcode.make(password)
        type(img)
        img.save(name)

    def click(self):
        destination=QFileDialog.getExistingDirectory(None,"Zielordner wählen")
        print (destination)       
        quantity = self.lineEdit_2.text()
        quantity = int(quantity)
        i = 1
        while i <= quantity:

            length = self.lineEdit.text()
            length = int(length)
            name = i
            name = str(destination) + "/" + str(name) + ".png"          
            self.generate(length,name,i)

            i = i+1

        data = {'Nummer': numbers,
	        'Passwort': passwords}
	
        #create dataframe
        df_marks = pd.DataFrame(data)
        print(df_marks)
        tablename = str(destination) + '/' + 'overview.txt'
        df_marks.to_csv(tablename, header=None, index=None, sep=' ', mode='a')

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(225, 183)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 111, 20))
        self.label_2.setObjectName("label_2")

        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 51, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 80, 51, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 130, 90, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButton, self.lineEdit)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PW_Gen"))
        self.pushButton.setText(_translate("Dialog", "Erstellen"))
        self.label.setText(_translate("Dialog", "Passwort Länge"))
        self.label_2.setText(_translate("Dialog", "Anzahl Passwörter"))


if __name__ =="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QMainWindow()
    ui=Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())