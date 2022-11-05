from __future__ import annotations
from modulefinder import IMPORT_NAME
# --- import 
import csv
from typing_extensions import Self
from PyQt6.QtWidgets import QWidget, QFrame
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout,QApplication
from PyQt6.QtWidgets import QLabel, QLineEdit, QDateEdit, QTextEdit, QPushButton,QDial
from PyQt6.QtCore import Qt, QDate, pyqtSignal 
from PyQt6.QtGui import QFont,QPixmap,QIcon
import sys
import pandas as p 

from matplotlib.pyplot import table
import matplotlib.pyplot as plt
from MultiLineEdit import MultiLineEdit
from WImage import WImage
import FilmView
import hhgm
import FigureWidget
import tri3Vue

class Interface (QWidget):
    
    Tri = pyqtSignal(list)
    
    def __init__(self) :
        super().__init__()
        # Propriétés 
        self.setStyleSheet('background-color : #193549 ')
        self.setFont(QFont('Jokerman',20))
        self.setWindowTitle('Hollywood Movies')    
        self.setWindowIcon(QIcon("qt.png"))
        # Affichage de départ
        self.name ="./data/Highest_Holywood_Grossing_Movies.csv"
        self.db = hhgm.HHGM()
        self.db.loadCSV(self.name)
        self.view = FilmView.FilmView({})
        self.tri = tri3Vue.Tri3Vue()
        self.id=0
        self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
        self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
        
        # Connexion des boutons de navigation
        self.view.next.connect(self.next)
        self.view.previous.connect(self.previous)
        
        # Connection des boutons de tri
        self.tri.filter.clicked.connect(self.tri1)
        self.tri.vue.filter.clicked.connect(self.tri1)
        self.tri.vue.vue.filter.clicked.connect(self.tri1)
        
        # -- Graphique -- #
        
        df=self.db.db
        self.annee=[]
        self.vente=[]
        
        # Traitement des données
        for element in df:
            # Recuperation de l'annee avec uniquement l'année de sortie dans le titre 
            step=element['title'].split('(')
            self.annee.append(int(step[1][:-1]))
            # Recuperation des ventes
            step=int(element['worldSales'])
            self.vente.append(step)
        # Tracer
        self.graph  = FigureWidget.FigureWidget()
        self.graph.scatter(self.annee,self.vente,0,False,0)

        
        
        # Layout
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.tri.vue.vue)
        self.mainLayout.addWidget(self.view)
        self.mainLayout.addWidget(self.graph)
        self.setLayout(self.mainLayout)
        
        self.showMaximized()
        
# ---------------------------------------------------------------------------------------------- #
        
    # Tri des films
    def tri1(self):
        
        # Affichage si aucun film ne correspond
        empty={'title': 'NO DATA', 'info': 'NO DATA', 'distributor': 0, 'releaseDate': '2000-01-01', 'domesticSales': 0, 'internationalSales': 0, 'worldSales': 0, 'genre': [0], 'runtime': 0, 'license': 0}
        
        # Premier Tri
        newbase=(self.tri.vue.vue.check())
        if (newbase!=[] ):
            self.db.db=[]
            for element in newbase:
                self.db.db.append(element)
            self.id=0
            self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
            self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
            
            # Partie Graphique Update
            df=self.db.db
            self.annee=[]
            self.vente=[]
            for element in df:
                step=element['title'].split('(')
                self.annee.append(int(step[1][:-1]))
                step=int(element['worldSales'])
                self.vente.append(step)
            self.graph.scatter(self.annee,self.vente,0,True,0)
            
        # Si rien n'est sélectionné on affiche qu'aucun ne correspond    
        else:
            self.db.db=[empty]
            self.id=0
            self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
            self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
            
        # Deuxieme Tri 
        newbase=(self.tri.vue.check(self.db.db))
        if (newbase!=[]):
            self.db.db=[]
            for element in newbase:
                self.db.db.append(element)
            self.id=0
            self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
            self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
            
            # Partie Graphique Update
            df=self.db.db
            self.annee=[]
            self.vente=[]
            for element in df:
                step=element['title'].split('(')
                self.annee.append(int(step[1][:-1]))
                step=int(element['worldSales'])
                self.vente.append(step)
            self.graph.scatter(self.annee,self.vente,0,True,0)
            
        # Si rien n'est sélectionné on affiche qu'aucun ne correspond 
        else:
            self.db.db=[empty]
            self.id=0
            self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
            self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
            
        # Troisieme Tri 
        newbase=(self.tri.check(self.db.db))
        if (newbase!=[]):
            self.db.db=[]
            for element in newbase:
                self.db.db.append(element)
            self.id=0
            self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
            self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
            
             # Partie Graphique Update
            df=self.db.db
            self.annee=[]
            self.vente=[]
            for element in df:
                step=element['title'].split('(')
                self.annee.append(int(step[1][:-1]))
                step=int(element['worldSales'])
                self.vente.append(step)
            self.graph.scatter(self.annee,self.vente,0,True,0)
            
        # Si rien n'est sélectionné on affiche qu'aucun ne correspond 
        else:
            self.db.db=[empty]
            self.id=0
            self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
            self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
            
# ---------------------------------------------------------------------------------------------- #
        
    # suivant
    def next(self) :
        self.id+=1
        if self.id >= len(self.db.db):
            self.id=0
        self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
        self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")
        self.graph.scatter(self.annee,self.vente,self.id,True,0)

    # precedent
    def previous(self) :
        self.id-=1
        if self.id <0:
            self.id=len(self.db.db)-1
        self.view.update(self.db.db[self.id],self.db.genres, self.db.distributors, self.db.licences)
        self.view.message("film : "+str(self.id+1)+" in "+str(len(self.db.db))+"")

        
        
if __name__ == "__main__":
    print(f'--------main--------')
    # création d'une QApplication
    app = QApplication(sys.argv)
    val=[]
    def printSignal(val : list) : print(val)
    f = Interface()
    
    # lancement de l'application
    sys.exit(app.exec())