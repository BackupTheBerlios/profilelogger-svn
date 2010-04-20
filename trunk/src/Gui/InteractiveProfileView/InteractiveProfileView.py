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
from FossilLegend import *
from CustomSymbolLegend import *
from SedimentStructureLegend import *

from ProfileHeaderItem import *
from InteractiveProfileScene import *
from BedItem import *

class InteractiveProfileView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setScene(InteractiveProfileScene(self))
        self.scene().enableViews.connect(self.onEnableMe)
        self.scene().disableViews.connect(self.onDisableMe)
    def onDisableMe(self):
        self.setEnabled(False)
    def onEnableMe(self):
        self.setEnabled(True)
    def contextMenuEvent(self, e):
        pos = self.mapToGlobal(e.pos())
        self.scene().setItemsAtContextMenuPoint(self.items(e.pos()))

        m = QMenu(self)

        editA = QAction(self.tr("Edit Profile..."), self)
        editA.triggered.connect(self.scene().editProfile)

        reloadA = QAction(self.tr("Reload"), self)
        reloadA.triggered.connect(self.scene().reload)
        m.addAction(editA)
        for i in self.scene().itemsAtContextMenu:
            print i.__class__.__name__
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
            if i.__class__ == FossilLegend:
                self.addActionsToMenu(self.createFossilLegendItemActions(), m)
            if i.__class__ == CustomSymbolLegend:
                self.addActionsToMenu(self.createCustomSymbolLegendItemActions(), m)
            if i.__class__ == SedimentStructureLegend:
                self.addActionsToMenu(self.createSedimentStructureLegendItemActions(), m)
            if i.__class__ == ProfileHeaderItem:
                self.addActionsToMenu(self.createProfileHeaderActions(), m)
            if i.__class__ == BedItem:
                self.addActionsToMenu(self.createBedActions(), m)
        m.addAction(reloadA)
        m.exec_(pos)
    def addActionsToMenu(self, actionList, menu):
        for a in actionList:
            if a is not None:
                menu.addAction(a)
            else:
                menu.insertSeparator(a)
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
    def createFossilLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Fossils"), self)
        manageA.triggered.connect(self.scene().manageFossils)
        l.append(manageA)
        return l
    def createCustomSymbolLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Custom Symbols"), self)
        manageA.triggered.connect(self.scene().manageCustomSymbols)
        l.append(manageA)
        return l
    def createSedimentStructureLegendItemActions(self):
        l = []
        manageA = QAction(self.tr("Manage Sediment Structures"), self)
        manageA.triggered.connect(self.scene().manageSedimentStructures)
        l.append(manageA)
        return l
    def createProfileHeaderActions(self):
        l = []
        createBedAtBottomA = QAction(self.tr("Create Bed At Bottom..."), self)
        createBedAtBottomA.triggered.connect(self.scene().createBedAtBottomAtContextMenuClickPoint)
        l.append(createBedAtBottomA)
        return l
    def createBedActions(self):
        l = []

        editBedA = QAction(self.tr("Edit Bed..."), self)
        moveBedUpA = QAction(self.tr("Move up"), self)
        moveBedDownA = QAction(self.tr("Move down"), self)
        deleteBedA = QAction(self.tr("Delete Bed..."), self)
        deleteBedsAboveA = QAction(self.tr("Delete Beds Above..."), self)
        deleteBedsBelowA = QAction(self.tr("Delete Beds Below..."), self)
        mergeWithAboveBedA = QAction(self.tr("Merge With Bed Above..."), self)
        mergeWithBelowBedA = QAction(self.tr("Merge With Bed Below..."), self)
        createBedAtTopA = QAction(self.tr("Create Bed At Top..."), self)
        createBedAtBottomA = QAction(self.tr("Create Bed At Bottom..."), self)
        createBedAboveA = QAction(self.tr("Create Bed Above..."), self)
        createBedBelowA = QAction(self.tr("Create Bed Below..."), self)
        renumberBedsFromBaseA = QAction(self.tr("Renumber Beds From Base..."), self)
        renumberBedsFromTopA = QAction(self.tr("Renumber Beds From Top..."), self)
        splitProfileAboveBedA = QAction(self.tr("Split Profile Above Bed..."), self)
        splitProfileBelowBedA = QAction(self.tr("Split Profile Below Bed..."), self)
        insertProfileAboveBedA = QAction(self.tr("Insert Profile Above Bed..."), self)
        insertProfileBelowBedA = QAction(self.tr("Insert Profile Below Bed..."), self)
        editBedA.triggered.connect(self.scene().editBedAtContextMenuClickPoint)
        deleteBedA.triggered.connect(self.scene().deleteBedAtContextMenuClickPoint)
        mergeWithAboveBedA.triggered.connect(self.scene().mergeWithAboveBedAtContextMenuClickPoint)
        mergeWithBelowBedA.triggered.connect(self.scene().mergeWithBelowBedAtContextMenuClickPoint)
        createBedAtTopA.triggered.connect(self.scene().createBedAtTopAtContextMenuClickPoint)
        createBedAtBottomA.triggered.connect(self.scene().createBedAtBottomAtContextMenuClickPoint)
        createBedAboveA.triggered.connect(self.scene().createBedAboveAtContextMenuClickPoint)
        createBedBelowA.triggered.connect(self.scene().createBedBelowAtContextMenuClickPoint)
        renumberBedsFromBaseA.triggered.connect(self.scene().renumberBedsAtContextMenuClickPointFromBase)
        renumberBedsFromTopA.triggered.connect(self.scene().renumberBedsAtContextMenuClickPointFromTop)
        splitProfileAboveBedA.triggered.connect(self.scene().splitProfileAboveBedAtContextMenuClickPoint)
        splitProfileBelowBedA.triggered.connect(self.scene().splitProfileBelowBedAtContextMenuClickPoint)
        insertProfileAboveBedA.triggered.connect(self.scene().insertProfileAboveBedAtContextMenuClickPoint)
        insertProfileBelowBedA.triggered.connect(self.scene().insertProfileBelowBedAtContextMenuClickPoint)
        deleteBedsAboveA.triggered.connect(self.scene().deleteBedsAboveAtContextMenuClickPoint)
        deleteBedsBelowA.triggered.connect(self.scene().deleteBedsBelowAtContextMenuClickPoint)
        moveBedUpA.triggered.connect(self.scene().moveBedAtContextMenuClickPointUp)
        moveBedDownA.triggered.connect(self.scene().moveBedAtContextMenuClickPointDown)

        l.append(editBedA)
        l.append(None)
        l.append(createBedAtTopA)
        l.append(createBedAtBottomA)
        l.append(createBedAboveA)
        l.append(createBedBelowA)
        l.append(None)
        l.append(moveBedUpA)
        l.append(moveBedDownA)
        l.append(None)
        l.append(deleteBedA)
        l.append(deleteBedsAboveA)
        l.append(deleteBedsBelowA)
        l.append(None)
        l.append(mergeWithAboveBedA)
        l.append(mergeWithBelowBedA)
        l.append(None)
        l.append(renumberBedsFromBaseA)
        l.append(renumberBedsFromTopA)
        l.append(None)
        l.append(splitProfileAboveBedA)
        l.append(splitProfileBelowBedA)
        l.append(None)
        l.append(insertProfileAboveBedA)
        l.append(insertProfileBelowBedA)
        
        return l
