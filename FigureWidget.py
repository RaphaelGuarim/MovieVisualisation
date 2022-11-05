import sys, numpy as np, time, math
from typing_extensions import Self
from typing import Union

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QGridLayout, QPushButton, QLineEdit,QMessageBox
from PyQt6.QtGui import QIntValidator

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# ------------------------------------------------------------------
# ---- class FigureWidget
# ------------------------------------------------------------------
class FigureWidget(FigureCanvas):
    """ Matplotlib Figure Widget  """
    # static attribute
    colors = np.array(["red","green","blue","yellow","pink","orange","purple","beige","brown","gray","cyan","magenta", "black"])

    def __init__(self : Self, width : int =10, height : int=5, dpi : int=100) -> None:
        # create Figure
        #self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = Figure()
        self.fig.set_facecolor('#193549')
        self.axes = self.fig.add_subplot(111)
        self.axes.set_facecolor('#0C1A25')
        self.axes.tick_params(axis='x', colors='white')
        self.axes.tick_params(axis='y', colors='white')
        FigureCanvas.__init__(self, self.fig)    # explicite call of super constructor
        FigureCanvas.updateGeometry(self)
        self.setMinimumSize(520, 800)
        self.setMaximumSize(520, 800)
        
    def scatter(self : Self,x : list[float],y : list[float], current : Union[int,None] = None, clear : bool =True , color : Union[int,None] = None) -> None:
        colorCurrent = 1
        colorSelection = 0 if not isinstance(color, int) else color 
        
        if clear : self.axes.clear()

        if len(x)> 1 :
            self.axes.scatter(x,y,10, c=FigureWidget.colors[colorSelection])

        if isinstance(current, int):
            self.axes.scatter(x[current],y[current],100, c=FigureWidget.colors[colorCurrent])

        #self.axes.annotate(str(i),(xs[i]+10,ys[i]))
        self.axes.axis('on')

        try:
            self.fig.canvas.draw()
        except Exception:
            time.sleep(0.5)
            self.fig.canvas.draw()


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    app : QApplication = QApplication(sys.argv)
    test : FigureWidget = FigureWidget()
    test.scatter([0,10],[10,0],0,True,1)
    test.scatter([0,5],[0,5],None,False,0)
    test.show()
    sys.exit(app.exec())