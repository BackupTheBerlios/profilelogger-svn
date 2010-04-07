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
from Gui.Dialogs.BedEditorDialog import *

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
        oldH = bed.heightInMillimetres()
        oldPos = bed.number
        dlg = BedEditorDialog(QApplication.activeWindow(), bed)
        if QDialog.Accepted == dlg.exec_():
            self.getSession().expire(bed)
            if bed.heightInMillimetres() == oldH and bed.number == oldPos:
                self.drawProfile()
            else:
                self.reload()
    def splitBedAtContextMenuClickPoint(self):
        pass
    def deleteBedAtContextMenuClickPoint(self):
        pass
    def mergeWithAboveBedAtContextMenuClickPoint(self):
        pass
    def mergeWithBelowBedAtContextMenuClickPoint(self):
        pass
    def createBedAtTopAtContextMenuClickPoint(self):
        pass
    def createBedAtBottomAtContextMenuClickPoint(self):
        pass
    def createBedAboveAtContextMenuClickPoint(self):
        pass
    def createBedBelowAtContextMenuClickPoint(self):
        pass
    def renumbeBedsAtContextMenuClickPointFromBase(self):
        pass
    def renumbeBedsAtContextMenuClickPointFromTop(self):
        pass
    def splitProfileAboveBedAtContextMenuClickPoint(self):
        pass
    def splitProfileBelowBedAtContextMenuClickPoint(self):
        pass
    def insertProfileAboveBedAtContextMenuClickPoint(self):
        pass
    def insertProfileBelowBedAtContextMenuClickPoint(self):
        pass
