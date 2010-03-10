from Gui.ItemViews.TreeView import TreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class LengthUnitItemView(TreeView):

    def __init__(self, parent, model):
        TreeView.__init__(self, parent, model)
