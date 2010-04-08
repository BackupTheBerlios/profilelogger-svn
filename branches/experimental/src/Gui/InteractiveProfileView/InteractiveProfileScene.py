from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ProfileItem import *

from Gui.ManagementDialogs.LithologyManagementDialog import *
from Gui.ManagementDialogs.BeddingTypeManagementDialog import *
from Gui.ManagementDialogs.ColorManagementDialog import *
from Gui.ManagementDialogs.OutcropTypeManagementDialog import *
from Gui.ManagementDialogs.FaciesManagementDialog import *
from Gui.ManagementDialogs.LithologicalUnitManagementDialog import *
from Gui.ManagementDialogs.TectonicUnitManagementDialog import *
from Gui.ManagementDialogs.StratigraphicUnitManagementDialog import *
from Gui.ManagementDialogs.FossilManagementDialog import *
from Gui.ManagementDialogs.SedimentStructureManagementDialog import *
from Gui.ManagementDialogs.CustomSymbolManagementDialog import *

from Gui.Dialogs.ProfileEditorDialog import *

class InteractiveProfileScene(QGraphicsScene):
    enableViews = pyqtSignal()
    disableViews = pyqtSignal()
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.profile = None
        self.itemsAtContextMenu = []
    def getSession(self):
        return QApplication.instance().db.session
    def setItemsAtContextMenuPoint(self, l):
        self.itemsAtContextMenu = l
    def onProfileChange(self, p):
        self.profile = p
        self.reload()
    def hasProfile(self):
        return self.profile is not None
    def reload(self):
        self.expireAndReload()
    def expireAndReload(self):
        self.clear()
        if self.hasProfile():
            self.enableViews.emit()
        else:
            self.disableViews.emit()
            return
        self.getSession().expire(self.profile)
        self.drawProfile()
    def drawProfile(self):
        self.profileItm = ProfileItem(None, self, 
                                      QRectF(0, 0, 0, 0), 
                                      QPointF(0, 0),
                                      self.profile)
    def manageLithologies(self):
        dlg = LithologyManagementDialog(QApplication.activeWindow(),
                                        self.profile.project)
        dlg.exec_()
        self.reload()
    def manageBeddingTypes(self):
        dlg = BeddingTypeManagementDialog(QApplication.activeWindow(),
                                          self.profile.project)
        dlg.exec_()
        self.reload()
    def manageColors(self):
        dlg = ColorManagementDialog(QApplication.activeWindow(),
                                    self.profile.project)
        dlg.exec_()
        self.reload()
    def manageOutcropTypes(self):
        dlg = OutcropTypeManagementDialog(QApplication.activeWindow(),
                                          self.profile.project)
        dlg.exec_()
        self.reload()
    def manageFacies(self):
        dlg = FaciesManagementDialog(QApplication.activeWindow(),
                                     self.profile.project)
        dlg.exec_()
        self.reload()
    def manageLithologicalUnits(self):
        dlg = LithologicalUnitManagementDialog(QApplication.activeWindow(),
                                               self.profile.project)
        dlg.exec_()
        self.reload()
    def manageTectonicUnits(self):
        dlg = TectonicUnitManagementDialog(QApplication.activeWindow(),
                                           self.profile.project)
        dlg.exec_()
        self.reload()
    def manageStratigraphicUnits(self):
        dlg = StratigraphicUnitManagementDialog(QApplication.activeWindow(),
                                                self.profile.project)
        dlg.exec_()
        self.reload()
    def manageFossils(self):
        dlg = FossilManagementDialog(QApplication.activeWindow(),
                                     self.profile.project)
        dlg.exec_()
        self.reload()
    def manageCustomSymbols(self):
        dlg = CustomSymbolManagementDialog(QApplication.activeWindow(),
                                           self.profile.project)
        dlg.exec_()
        self.reload()
    def manageSedimentStructures(self):
        dlg = SedimentStructureManagementDialog(QApplication.activeWindow(),
                                                self.profile.project)
        dlg.exec_()
        self.reload()
    def editProfile(self):
        dlg = ProfileEditorDialog(QApplication.activeWindow(),
                                  self.profile)
        dlg.exec_()
        self.reload()
    def getBedAtContextMenuClickPoint(self):
        for i in self.itemsAtContextMenu:
            if i.__class__ == BedItem:
                return i.bed
        return None
    def editBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.editBed(bed)
    def splitBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.splitBed(bed)
    def deleteBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.deleteBed(bed)
    def deleteBedsAboveAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.deleteBedsAbove(bed)
    def deleteBedsBelowAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.deleteBedsBelow(bed)
    def mergeWithAboveBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.mergeWithAbove(bed)
    def mergeWithBelowBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.mergeWithBelow(bed)
    def createBedAtTopAtContextMenuClickPoint(self):
        self.profileItm.createBedAtTop()
    def createBedAtBottomAtContextMenuClickPoint(self):
        self.profileItm.createBedAtBottom()
    def createBedAboveAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.createBedAbove(bed)
    def createBedBelowAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.createBedBelow(bed)
    def renumberBedsAtContextMenuClickPointFromBase(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.renumberFromBase()
    def renumberBedsAtContextMenuClickPointFromTop(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.renumberFromTop()
    def splitProfileAboveBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.splitProfileAbove(bed)
    def splitProfileBelowBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.splitProfileBelow(bed)
    def insertProfileAboveBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.insertProfileAbove(bed)
    def insertProfileBelowBedAtContextMenuClickPoint(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.insertProfileBelow(bed)
    def moveBedAtContextMenuClickPointDown(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.moveDown(bed)
    def moveBedAtContextMenuClickPointUp(self):
        bed = self.getBedAtContextMenuClickPoint()
        if bed is None:
            return
        self.profileItm.moveUp(bed)
