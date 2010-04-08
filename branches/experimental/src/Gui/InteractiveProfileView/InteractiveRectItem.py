from RectItem import *

class InteractiveRectItem(RectItem):
    def __init__(self, parent, scene, rect=None, pos=None):
        RectItem.__init__(self, parent, scene, rect, pos)
    def clearChildren(self):
        for c in self.childItems():
            print "deleting: ",c.__class__.__name__
            self.scene().removeItem(c)
            del c
