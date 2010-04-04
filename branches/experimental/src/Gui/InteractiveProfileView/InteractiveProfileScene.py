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

class InteractiveProfileScene(QGraphicsScene):
    enableViews = pyqtSignal()
    disableViews = pyqtSignal()
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.profile = None
        self.profileWidth = 1000
    def onProfileChange(self, p):
        self.profile = p
        self.reload()
    def hasProfile(self):
        return self.profile is not None
    def reload(self):
        self.clear()
        if self.hasProfile():
            self.enableViews.emit()
        else:
            self.disableViews.emit()
            return
        self.profileItm = ProfileItem(None, self, 
                                      QRectF(0, 0, self.profileWidth, 100), 
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