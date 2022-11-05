from PyQt6.QtCore import * 
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import * 
import sys
import Tri1Vue
import hhgm


class Tri2Vue (QWidget):
    
    clic1 = pyqtSignal()
    
    def __init__(self) :
        super().__init__()
        self.vue= Tri1Vue.Tri1Vue()
        
        self.tri2Layout = QVBoxLayout()
        
        self.triLayout = QVBoxLayout(); 
        self.secondLayout = QVBoxLayout(); 
        
        self.buttonAll = QPushButton("Select All")
        self.buttonAll.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.buttonNone = QPushButton("Deselect All")
        self.buttonNone.setStyleSheet('background-color :#5B6668 ; color : white')
        
        self.c1 = QCheckBox("Action");
        self.c1.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c2 = QCheckBox("Adventure");
        self.c2.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c3 = QCheckBox("Sci Fi");
        self.c3.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c4 = QCheckBox("Drama");
        self.c4.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c5 = QCheckBox("Fantasy");
        self.c5.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c6 = QCheckBox("Romance");
        self.c6.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c7 = QCheckBox("Animation");
        self.c7.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c8 = QCheckBox("Comedy");
        self.c8.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c9 = QCheckBox("Family");
        self.c9.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c10 = QCheckBox("Musical");
        self.c10.setStyleSheet('background-color : #5B6668 ; color : white')       
        
        self.c11 = QCheckBox("Crime");
        self.c11.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c12 = QCheckBox("Thriller");
        self.c12.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c13 = QCheckBox("War");
        self.c13.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c14 = QCheckBox("Mystery");
        self.c14.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c15 = QCheckBox("Biography");
        self.c15.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c16 = QCheckBox("Horror");
        self.c16.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c17 = QCheckBox("Sport");
        self.c17.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c18 = QCheckBox("Music");
        self.c18.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c19 = QCheckBox("History");
        self.c19.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c20 = QCheckBox("Western");
        self.c20.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.c21 = QCheckBox("Documentary");
        self.c21.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.filter = QPushButton("Filter")
        self.filter.setStyleSheet('background-color : #0C1A25 ; color : white ;')
        
        
        
        self.secondLayout.addWidget(self.c1)
        self.secondLayout.addWidget(self.c2)
        self.secondLayout.addWidget(self.c3)
        self.secondLayout.addWidget(self.c4)
        self.secondLayout.addWidget(self.c5)
        self.secondLayout.addWidget(self.c6)
        self.secondLayout.addWidget(self.c7)
        self.secondLayout.addWidget(self.c8)
        self.secondLayout.addWidget(self.c9)
        self.secondLayout.addWidget(self.c10)
        self.secondLayout.addWidget(self.c11)
        self.secondLayout.addWidget(self.c12)
        self.secondLayout.addWidget(self.c13)
        self.secondLayout.addWidget(self.c14)
        self.secondLayout.addWidget(self.c15)
        self.secondLayout.addWidget(self.c16)
        self.secondLayout.addWidget(self.c17)
        self.secondLayout.addWidget(self.c18)
        self.secondLayout.addWidget(self.c19)
        self.secondLayout.addWidget(self.c20)
        self.secondLayout.addWidget(self.c21)
    
        
        self.triLayout.addWidget(self.buttonAll)
        self.triLayout.addWidget(self.buttonNone)
        
        self.box = QGroupBox()
        self.box.setLayout(self.triLayout)
        self.box.setMaximumHeight(70)
        self.box.setMaximumWidth(300)
        self.box.setStyleSheet('background-color : #0C1A25 ; color : white')
        
        self.box2 = QGroupBox()
        self.box2.setLayout(self.secondLayout)
        self.box2.setMaximumWidth(300)
        self.box2.setStyleSheet('background-color : #0C1A25 ; color : white')
        
        self.tri2Layout.addWidget(self.box)
        self.tri2Layout.addWidget(self.box2)
        self.tri2Layout.addWidget(self.filter)
        
        self.buttonAll.clicked.connect(self.change_coche)
        self.buttonNone.clicked.connect(self.change_decoche)
        
        self.vue.initialLayout.addLayout(self.tri2Layout)
        
        
        
        self.vue.show()
        
    
    
    def check(self,base : list):
        tab=[]
        list=[]
        if self.c1.isChecked():
            list.append(0)
        if self.c2.isChecked():
            list.append(1)
        if self.c3.isChecked():
            list.append(2)
        if self.c4.isChecked():
            list.append(3)
        if self.c5.isChecked():
            list.append(4)
        if self.c6.isChecked():
            list.append(5)
        if self.c7.isChecked():
            list.append(6)
        if self.c8.isChecked():
            list.append(7)
        if self.c9.isChecked():
            list.append(8)
        if self.c10.isChecked():
            list.append(9)
        if self.c11.isChecked():
            list.append(10)
        if self.c12.isChecked():
            list.append(11)
        if self.c13.isChecked():
            list.append(12)
        if self.c14.isChecked():
            list.append(13)
        if self.c15.isChecked():
           list.append(14)
        if self.c16.isChecked():
            list.append(15)
        if self.c17.isChecked():
            list.append(16)
        if self.c18.isChecked():
            list.append(17)
        if self.c19.isChecked():
            list.append(18)
        if self.c20.isChecked():
            list.append(19)
        if self.c21.isChecked():
            list.append(20)
        for element in base:
            # Verification qu'on ne la pas deja ajouter car plusieurs genres par film 
            for i in range (len(element['genre'])):
                if element not in tab:
                    if element['genre'][i] in list:
                        tab.append(element)
        return tab
               
    def change_decoche(self):
        self.c1.setChecked(False)
        self.c2.setChecked(False)
        self.c3.setChecked(False)
        self.c4.setChecked(False)
        self.c5.setChecked(False)
        self.c6.setChecked(False)
        self.c7.setChecked(False)
        self.c8.setChecked(False)
        self.c9.setChecked(False)
        self.c10.setChecked(False)
        self.c11.setChecked(False)
        self.c12.setChecked(False)
        self.c13.setChecked(False)
        self.c14.setChecked(False)
        self.c15.setChecked(False)
        self.c16.setChecked(False)
        self.c17.setChecked(False)
        self.c18.setChecked(False)
        self.c19.setChecked(False)
        self.c20.setChecked(False)
        self.c21.setChecked(False)
    
        
    def change_coche(self):
        self.c1.setChecked(True)
        self.c2.setChecked(True)
        self.c3.setChecked(True)
        self.c4.setChecked(True)
        self.c5.setChecked(True)
        self.c6.setChecked(True)
        self.c7.setChecked(True)
        self.c8.setChecked(True)
        self.c9.setChecked(True)
        self.c10.setChecked(True)
        self.c11.setChecked(True)
        self.c12.setChecked(True)
        self.c13.setChecked(True)
        self.c14.setChecked(True)
        self.c15.setChecked(True)
        self.c16.setChecked(True)
        self.c17.setChecked(True)
        self.c18.setChecked(True)
        self.c19.setChecked(True)
        self.c20.setChecked(True)
        self.c21.setChecked(True)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Tri2Vue()
    sys.exit(app.exec())
    