from PyQt4.QtGui import *
from PyQt4.QtCore import *

from LithologyLegend import *
from BeddingTypeLegend import *
from ColorLegend import *
from OutcropTypeLegend import *
from FaciesLegend import *
from LithologicalUnitLegend import *
from TectonicUnitLegend import *
from StratigraphicUnitLegend import *


class InteractiveProfileView(QGraphicsView):
    def __init__(self, parent, modelClass):
        QGraphicsView.__init__(self, parent)
        self.setScene(modelClass(self))
        self.scene().enableViews.connect(self.onEnableMe)
        self.scene().disableViews.connect(self.onDisableMe)
    def onDisableMe(self):
        self.setEnabled(False)
    def onEnableMe(self):
        self.setEnabled(True)
    def contextMenuEvent(self, e):
        pos = self.mapToGlobal(e.pos())
        items = self.items(e.pos())

        m = QMenu(self)

        reloadA = QAction(self.tr("Reload"), self)
        reloadA.triggered.connect(self.scene().reload)
        m.addAction(reloadA)

        for i in items:
            if i.__class__ == LithologyLegend:
                self.addActionsToMenu(self.createLithologyLegendItemActions(), m)
            if i.__class__ == BeddingTypeLegend:
                self.addActionsToMenu(self.createBeddingTypeLegendItemActions(), m)
            if i.__class__ == ColorLegend:
                self.addActionsToMenu(self.createColorLegendItemActions(), m)
            if i.__class__ == OutcropTypeLegend:
                self.addActionsToMenu(self.createOutcropTypeLegendItemActions(), m)
            if i.__class__ == FaciesLegend:
                self.addActionsToMenu(self.createFaciesLegendItemActions(), m)
            if i.__class__ == LithologicalUnitLegend:
                self.addActionsToMenu(self.createLithologicalUnitLegendItemActions(), m)
            if i.__class__ == TectonicUnitLegend:
                self.addActionsToMenu(self.createTectonicUnitLegendItemActions(), m)            
            if i.__class__ == StratigraphicUnitLegend:
                self.addActionsToMenu(self.createStratigraphicUnitLegendItemActions(), m)
        m.exec_(pos)
    def addActionsToMenu(self, actionList, menu):
        for a in actionList:
            menu.addAction(a)
    def createLithologyLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Lithologies"), self)
        manageA.triggered.connect(self.scene().manageLithologies)
        l.append(manageA)
        return l
    def createBeddingTypeLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Bedding Types"), self)
        manageA.triggered.connect(self.scene().manageBeddingTypes)
        l.append(manageA)
        return l
    def createColorLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Colors"), self)
        manageA.triggered.connect(self.scene().manageColors)
        l.append(manageA)
        return l
    def createOutcropTypeLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Outcrop Types"), self)
        manageA.triggered.connect(self.scene().manageOutcropTypes)
        l.append(manageA)
        return l
    def createFaciesLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Facies"), self)
        manageA.triggered.connect(self.scene().manageFacies)
        l.append(manageA)
        return l
    def createLithologicalUnitLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Lithological Units"), self)
        manageA.triggered.connect(self.scene().manageLithologicalUnits)
        l.append(manageA)
        return l
    def createTectonicUnitLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Tectonic Units"), self)
        manageA.triggered.connect(self.scene().manageTectonicUnits)
        l.append(manageA)
        return l
    def createStratigraphicUnitLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Stratigraphic Units"), self)
        manageA.triggered.connect(self.scene().manageStratigraphicUnits)
        l.append(manageA)
        return l
