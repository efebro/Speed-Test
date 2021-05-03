from PyQt5 import QtCore, QtGui, QtWidgets
import speedtest

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 171)
        Form.setStyleSheet("background-color: rgb(85, 0, 255);\n"
"background-color: rgb(255, 255, 0);")
        self.textDownload = QtWidgets.QTextBrowser(Form)
        self.textDownload.setGeometry(QtCore.QRect(0, 80, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textDownload.setFont(font)
        self.textDownload.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.textDownload.setObjectName("textDownload")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 30, 221, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"border-radius:15px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.olc)
        self.textUpload = QtWidgets.QTextBrowser(Form)
        self.textUpload.setGeometry(QtCore.QRect(0, 130, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.textUpload.setFont(font)
        self.textUpload.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);")
        self.textUpload.setObjectName("textUpload")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def olc(self):
        test = speedtest.Speedtest()
        indirme = test.download()
        gönderme = test.upload()
        indirme = indirme/1000000
        gönderme = gönderme/1000000
        download = ("İndirme Hızınız(DOWNLOAD) = %d" %((indirme)))
        upload = ("Gönderme Hızınız(UPLOAD) = %d" %((gönderme)))
        self.textDownload.setText(download)
        self.textUpload.setText(upload)
        

     
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SPEED TEST"))
        self.pushButton.setText(_translate("Form", "SPEED TEST"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
