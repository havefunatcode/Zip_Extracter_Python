import sys, os
from PyQt5.QtWidgets import *

class MainForm(QWidget):
    def __init__(self, name = 'ZipFile Extractor'):
        super(MainForm,self).__init__()
        self.setWindowTitle(name)       # Set Window Title
        self.cwd = os.getcwd() # Get the current program file location
        self.resize(300,200)   # Set the window size

        # Set Choose Directory Button
        self.btn_chooseDir = QPushButton(self)
        self.btn_chooseDir.setObjectName("btn_chooseDir")
        self.btn_chooseDir.setText("Choose Folder")

        # Set Layout
        layout = QVBoxLayout()
        layout.addWidget(self.btn_chooseDir)
        self.setLayout(layout)

        # Set Event Listener
        self.btn_chooseDir.clicked.connect(self.slot_btn_chooseDir)

        # Choose Directory(Dialog)
    def slot_btn_chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "Choose Folder", self.cwd)  #

        if dir_choose == "":
            print("\nCancel selection")
            return

        import extractZip as ze
        ze.extractZipFile(dir_choose)

        #print("\nThe folder you selected is:")
        #print(dir_choose)

        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    mainForm = MainForm('Test QFileDialog')
    mainForm.show()
    sys.exit(app.exec_())