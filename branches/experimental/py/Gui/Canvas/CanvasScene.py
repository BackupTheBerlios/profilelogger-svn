from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class CanvasScene(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        
