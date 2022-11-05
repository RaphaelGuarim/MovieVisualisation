#self.t1.setGraphicsEffect(QGraphicsBlurEffect()) Easter egg 
from PyQt6.QtCore import * 
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import * 
import sys
import hhgm


class Tri1Vue (QWidget):
    
    Tri = pyqtSignal(list)
    
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("App")
        self.setWindowIcon(QIcon("clashroyale.png"))
        self.setStyleSheet('background-color : #0C1A25 ')
        self.setFont(QFont('Jokerman',20))
        self.setGeometry(0,0,300,800)
        
        self.initialLayout = QHBoxLayout(); 
        self.initialLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.initialLayout)
        
        
        self.tri1Layout= QVBoxLayout();
        self.tri1Layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.initialLayout.addLayout(self.tri1Layout)
        
        self.triLayout = QVBoxLayout(); 
        
        self.firstLayout = QVBoxLayout(); 

        # Reste a redimensionner la box
        
        self.buttonAll = QPushButton("Select All")
        self.buttonAll.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.buttonNone = QPushButton("Deselect All")
        self.buttonNone.setStyleSheet('background-color :#5B6668 ; color : white')
        
        
        self.t1 = QCheckBox("Walt Disney Studio Motion Picture");
        self.t1.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t2 = QCheckBox("Twentieth Century Fox");
        self.t2.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t3 = QCheckBox("Sony Picture Entertainment");
        self.t3.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t4 = QCheckBox("Paramount Pictures");
        self.t4.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t5 = QCheckBox("Universal Pictures");
        self.t5.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t6 = QCheckBox("Warner Bros");
        self.t6.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t7 = QCheckBox("DreamWorks Distribution");
        self.t7.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t8 = QCheckBox("Lionsgate");
        self.t8.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t9 = QCheckBox("DreamWorks");
        self.t9.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t10 = QCheckBox("New Line Cinema");
        self.t10.setStyleSheet('background-color : #5B6668 ; color : white')       
        
        self.t11 = QCheckBox("Newmarket Films");
        self.t11.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t12 = QCheckBox("Summit Entertainment");
        self.t12.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t13 = QCheckBox("Colombia Pictures");
        self.t13.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t14 = QCheckBox("IFC Films");
        self.t14.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t15 = QCheckBox("Instar Pictures");
        self.t15.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t16 = QCheckBox("Orion Pictures");
        self.t16.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t17 = QCheckBox("Metro Goldwyn Mayer");
        self.t17.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t18 = QCheckBox("Miramax");
        self.t18.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t19 = QCheckBox("The Weinstein Company");
        self.t19.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t20 = QCheckBox("Fox Searchlight Pictures");
        self.t20.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t21 = QCheckBox("Revolution Studios");
        self.t21.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t22 = QCheckBox("Artisan Entertainment");
        self.t22.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t23 = QCheckBox("Sony Pictures Classics");
        self.t23.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t24 = QCheckBox("United Artists");
        self.t24.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t25 = QCheckBox("Screen Gems");
        self.t25.setStyleSheet('background-color : #5B6668 ; color : white')

        self.t26 = QCheckBox("USA Films");
        self.t26.setStyleSheet('background-color : #5B6668 ; color : white')

        self.t27 = QCheckBox("20th Century Studios");
        self.t27.setStyleSheet('background-color : #5B6668 ; color : white')

        self.t28 = QCheckBox("STX Entertainment");
        self.t28.setStyleSheet('background-color : #5B6668 ; color : white')

        self.t29 = QCheckBox("Dimension Films");
        self.t29.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t30 = QCheckBox("United Artists Releasing");
        self.t30.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t31 = QCheckBox("FilmDistrict");
        self.t31.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t32 = QCheckBox("Focus Features");
        self.t32.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t33 = QCheckBox("Relativity Media");
        self.t33.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.t34 = QCheckBox("Roadside Attractions");
        self.t34.setStyleSheet('background-color : #5B6668 ; color : white')
        
        self.filter = QPushButton("Filter")
        self.filter.setStyleSheet('background-color : #0C1A25 ; color : white')
        
        self.triLayout.addWidget(self.buttonAll)
        self.triLayout.addWidget(self.buttonNone)
        
        self.firstLayout.addWidget(self.t1)
        self.firstLayout.addWidget(self.t2)
        self.firstLayout.addWidget(self.t3)
        self.firstLayout.addWidget(self.t4)
        self.firstLayout.addWidget(self.t5)
        self.firstLayout.addWidget(self.t6)
        self.firstLayout.addWidget(self.t7)
        self.firstLayout.addWidget(self.t8)
        self.firstLayout.addWidget(self.t9)
        self.firstLayout.addWidget(self.t10)
        self.firstLayout.addWidget(self.t11)
        self.firstLayout.addWidget(self.t12)
        self.firstLayout.addWidget(self.t13)
        self.firstLayout.addWidget(self.t14)
        self.firstLayout.addWidget(self.t15)
        self.firstLayout.addWidget(self.t16)
        self.firstLayout.addWidget(self.t17)
        self.firstLayout.addWidget(self.t18)
        self.firstLayout.addWidget(self.t19)
        self.firstLayout.addWidget(self.t20)
        self.firstLayout.addWidget(self.t21)
        self.firstLayout.addWidget(self.t22)
        self.firstLayout.addWidget(self.t23)
        self.firstLayout.addWidget(self.t24)
        self.firstLayout.addWidget(self.t25)
        self.firstLayout.addWidget(self.t26)
        self.firstLayout.addWidget(self.t27)
        self.firstLayout.addWidget(self.t28)
        self.firstLayout.addWidget(self.t29)
        self.firstLayout.addWidget(self.t30)
        self.firstLayout.addWidget(self.t31)
        self.firstLayout.addWidget(self.t32)
        self.firstLayout.addWidget(self.t33)
        self.firstLayout.addWidget(self.t34)
        
        
        self.box = QGroupBox()
        self.box.setLayout(self.triLayout)
        self.box.setMaximumHeight(70)
        self.box.setMaximumWidth(250)
        self.box.move(0,0)
        self.box.setStyleSheet('background-color : #0C1A25 ; color : white')
        
        self.box2 = QGroupBox()
        self.box2.setLayout(self.firstLayout)
        self.box2.setMaximumWidth(300)
        self.box2.setStyleSheet('background-color : #0C1A25 ; color : white')
        
        self.tri1Layout.addWidget(self.box)
        self.tri1Layout.addWidget(self.box2)
        self.tri1Layout.addWidget(self.filter)
        
        
        
        self.buttonAll.clicked.connect(self.change_coche)
        self.buttonNone.clicked.connect(self.change_decoche)
        
        self.show()
        
    def check(self):
        tab=[]
        list=[]
        if self.t1.isChecked():
             list.append(0)
        if self.t2.isChecked():
             list.append(1)
        if self.t3.isChecked():
             list.append(2)
        if self.t4.isChecked():
             list.append(3)
        if self.t5.isChecked():
             list.append(4)
        if self.t6.isChecked():
             list.append(5)
        if self.t7.isChecked():
             list.append(6)
        if self.t8.isChecked():
             list.append(7)
        if self.t9.isChecked():
             list.append(8)
        if self.t10.isChecked():
             list.append(9)
        if self.t11.isChecked():
             list.append(10)
        if self.t12.isChecked():
             list.append(11)
        if self.t13.isChecked():
             list.append(12)
        if self.t14.isChecked():
             list.append(13)
        if self.t15.isChecked():
             list.append(14)
        if self.t16.isChecked():
             list.append(15)
        if self.t17.isChecked():
             list.append(16)
        if self.t18.isChecked():
             list.append(17)
        if self.t19.isChecked():
             list.append(18)
        if self.t20.isChecked():
             list.append(19)
        if self.t21.isChecked():
             list.append(20)
        if self.t22.isChecked():
             list.append(21)
        if self.t23.isChecked():
             list.append(22)
        if self.t24.isChecked():
             list.append(23)
        if self.t25.isChecked():
             list.append(24)
        if self.t26.isChecked():
             list.append(25)
        if self.t27.isChecked():
             list.append(26)
        if self.t28.isChecked():
             list.append(27)
        if self.t29.isChecked():
             list.append(28)
        if self.t30.isChecked():
             list.append(29)
        if self.t31.isChecked():
             list.append(30)
        if self.t32.isChecked():
             list.append(31)
        if self.t33.isChecked():
             list.append(32)
        if self.t34.isChecked():
             list.append(33)
        db = hhgm.HHGM()
        db.loadCSV("./data/Highest_Holywood_Grossing_Movies.csv")

        
        for element in db.db:
            if element['distributor'] in list:
                tab.append(element)
        return tab

        
    def change_decoche(self):
        self.t1.setChecked(False)
        self.t2.setChecked(False)
        self.t3.setChecked(False)
        self.t4.setChecked(False)
        self.t5.setChecked(False)
        self.t6.setChecked(False)
        self.t7.setChecked(False)
        self.t8.setChecked(False)
        self.t9.setChecked(False)
        self.t10.setChecked(False)
        self.t11.setChecked(False)
        self.t12.setChecked(False)
        self.t13.setChecked(False)
        self.t14.setChecked(False)
        self.t15.setChecked(False)
        self.t16.setChecked(False)
        self.t17.setChecked(False)
        self.t18.setChecked(False)
        self.t19.setChecked(False)
        self.t20.setChecked(False)
        self.t21.setChecked(False)
        self.t22.setChecked(False)
        self.t23.setChecked(False)
        self.t24.setChecked(False)
        self.t25.setChecked(False)
        self.t26.setChecked(False)
        self.t27.setChecked(False)
        self.t28.setChecked(False)
        self.t29.setChecked(False)
        self.t30.setChecked(False)
        self.t31.setChecked(False)
        self.t32.setChecked(False)
        self.t33.setChecked(False)
        self.t34.setChecked(False)
        
    def change_coche(self):
        self.t1.setChecked(True)
        self.t2.setChecked(True)
        self.t3.setChecked(True)
        self.t4.setChecked(True)
        self.t5.setChecked(True)
        self.t6.setChecked(True)
        self.t7.setChecked(True)
        self.t8.setChecked(True)
        self.t9.setChecked(True)
        self.t10.setChecked(True)
        self.t11.setChecked(True)
        self.t12.setChecked(True)
        self.t13.setChecked(True)
        self.t14.setChecked(True)
        self.t15.setChecked(True)
        self.t16.setChecked(True)
        self.t17.setChecked(True)
        self.t18.setChecked(True)
        self.t19.setChecked(True)
        self.t20.setChecked(True)
        self.t21.setChecked(True)
        self.t22.setChecked(True)
        self.t23.setChecked(True)
        self.t24.setChecked(True)
        self.t25.setChecked(True)
        self.t26.setChecked(True)
        self.t27.setChecked(True)
        self.t28.setChecked(True)
        self.t29.setChecked(True)
        self.t30.setChecked(True)
        self.t31.setChecked(True)
        self.t32.setChecked(True)
        self.t33.setChecked(True)
        self.t34.setChecked(True)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Tri1Vue()
    sys.exit(app.exec())
    