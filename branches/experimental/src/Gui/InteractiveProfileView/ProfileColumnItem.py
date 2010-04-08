from InteractiveRectItem import *

from BedItem import *

from Gui.Dialogs.BedEditorDialog import *

class ProfileColumnItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, legendFont, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.legendFont = legendFont
        self.profile = profile
        self.drawBeds()
    def getSession(self):
        return QApplication.instance().db.session
    def drawBeds(self):
        self.maxY = 0
        self.clearChildren()
        for bed in self.profile.beds:
            itm = BedItem(self, self.scene(),
                          QRectF(0, 0, self.rect().width(), bed.heightInPixel()),
                          QPointF(0, self.maxY),
                          self.legendFont, 
                          bed)
            self.maxY += itm.rect().height()
            self.setRect(QRectF(0, 0, self.rect().width(), self.maxY))
    def editBed(self, bed):
        oldNumber = bed.number
        oldHeight = bed.heightInMillimetres
        dlg = BedEditorDialog(QApplication.activeWindow(), bed)
        if QDialog.Accepted == dlg.exec_():
            if oldNumber != bed.number or oldHeight != bed.heightInMillimetres:
                self.getSession().expire(self.profile)
            self.drawBeds()
        else:
            if not bed.hasId():
                self.getSession().expunge(bed)
    def createBedOnTop(self):
        self.editBed(self.profile.createBedOnTop())
    def createBedAtBottom(self):
        self.editBed(self.profile.createBedAtBottom())
    def splitBed(self, bed):
        pass
    def deleteBed(self, bed):
        pass
    def deleteBedsAbove(self, bed):
        pass
    def deleteBedsBelow(self, bed):
        pass
    def mergeWithAbove(self, bed):
        pass
    def mergeWithBelow(self, bed):
        pass
    def createBedAbove(self, bed):
        pass
    def createBedBelow(self, bed):
        pass
    def renumberFromBase(self):
        pass
    def renumberFromTop(self):
        pass
    def splitProfileAbove(self, bed):
        pass
    def splitProfileBelow(self, bed):
        pass
    def insertProfileAbove(self, bed):
        pass
    def insertProfileBelow(self, bed):
        pass
