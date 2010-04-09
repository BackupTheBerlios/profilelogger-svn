from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ToolBar(QToolBar):
    def __init__(self, title, parent):
        QToolBar.__init__(self, title, parent)
