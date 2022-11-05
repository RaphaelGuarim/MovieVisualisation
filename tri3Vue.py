from PyQt6.QtCore import * 
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import * 
import sys
import Tri2Vue
import hhgm

class Tri3Vue (QWidget):
    
    clic1 = pyqtSignal()
    
    def __init__(self) :
        super().__init__()
        self.vue= Tri2Vue.Tri2Vue()
        
        self.tri3Layout = QVBoxLayout()
        
        self.triLayout = QVBoxLayout(); 
        self.thirdLayout = QVBoxLayout(); 
        
        self.buttonAll = QPushButton("Select All")
        self.buttonAll.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.buttonNone = QPushButton("Deselect All")
        self.buttonNone.setStyleSheet('background-color :#5B6668 ; color : white')
        
        self.d1 = QCheckBox("PG 13");
        self.d1.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.d2 = QCheckBox("NA");
        self.d2.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.d3 = QCheckBox("PG");
        self.d3.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.d4 = QCheckBox("G");
        self.d4.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.d5 = QCheckBox("R");
        self.d5.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.filter = QPushButton("Filter")
        self.filter.setStyleSheet('background-color : #0C1A25 ; color : white ;')
        
        self.thirdLayout.addWidget(self.d1)
        self.thirdLayout.addWidget(self.d2)
        self.thirdLayout.addWidget(self.d3)
        self.thirdLayout.addWidget(self.d4)
        self.thirdLayout.addWidget(self.d5)
        
        self.triLayout.addWidget(self.buttonAll)
        self.triLayout.addWidget(self.buttonNone)
        
        self.box = QGroupBox()
        self.box.setLayout(self.triLayout)
        self.box.setMaximumHeight(70)
        self.box.setMaximumWidth(90)
        self.box.setStyleSheet('background-color : #0C1A25 ; color : white')
        
        self.box2 = QGroupBox()
        self.box2.setLayout(self.thirdLayout)
        self.box2.setMaximumWidth(90)
        self.box2.setStyleSheet('background-color : #0C1A25 ; color : white')
        
        self.tri3Layout.addWidget(self.box)
        self.tri3Layout.addWidget(self.box2)
        self.tri3Layout.addWidget(self.filter)
        
        self.buttonAll.clicked.connect(self.change_coche)
        self.buttonNone.clicked.connect(self.change_decoche)
        
        self.vue.vue.initialLayout.addLayout(self.tri3Layout)
    
    # Renvoie une liste des indices checkés en fonction du premier tri
    def check(self,base):
        tab=[]
        list=[]
        if self.d1.isChecked():
            list.append(0)
        if self.d2.isChecked():
            list.append(1)
        if self.d3.isChecked():
            list.append(2)
        if self.d4.isChecked():
            list.append(3)
        if self.d5.isChecked():
            list.append(4)
        for element in base:
            if element['license'] in list:
                tab.append(element)
        return tab
                       
    def change_decoche(self):
        self.d1.setChecked(False)
        self.d2.setChecked(False)
        self.d3.setChecked(False)
        self.d4.setChecked(False)
        self.d5.setChecked(False)
        
    
        
    def change_coche(self):
        self.d1.setChecked(True)
        self.d2.setChecked(True)
        self.d3.setChecked(True)
        self.d4.setChecked(True)
        self.d5.setChecked(True)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Tri3Vue()
    sys.exit(app.exec())