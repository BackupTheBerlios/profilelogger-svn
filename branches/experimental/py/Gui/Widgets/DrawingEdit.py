from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Canvas.CanvasScene import *
from Gui.Canvas.CanvasView import *

from Gui.ItemViews.PenItemView import *
from Gui.ItemViews.BrushItemView import *
from Gui.Canvas.StraightLineItem import *
from Gui.Canvas.RectangleItem import *
from Gui.Canvas.EllipseItem import *
from Gui.Canvas.PolygonItem import *
from Gui.Canvas.PainterPathItem import *
from Gui.Widgets.ZoomSlider import *

class DrawingEdit(QSplitter):
    def __init__(self, parent):
        QSplitter.__init__(self, parent)
        self.drawing = None
        self.setOrientation(Qt.Horizontal)
        self.canvasS = CanvasScene(self)
        self.canvasV = CanvasView(self)
        self.canvasV.setScene(self.canvasS)
        self.configureTools()
        self.addWidget(self.toolsW)
        self.addWidget(self.canvasV)
    def configureTools(self):
        self.toolsW = QWidget(self)
        self.toolsW.setLayout(QHBoxLayout(self.toolsW))
        self.zoomW = ZoomSlider(self.toolsW)
        self.setupToolsWidget()

        self.settingsW = QWidget(self.toolsW)
        self.settingsW.setLayout(QVBoxLayout(self.settingsW))
        self.pensW = PenItemView(self.settingsW, QApplication.instance().penModel)
        self.brushesW = BrushItemView(self.settingsW, QApplication.instance().brushModel)
        self.modeW = QLabel(self.tr("No Tool Selected"), self.settingsW)
        self.modeW.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.settingsW.layout().addWidget(self.pensW)
        self.settingsW.layout().addWidget(self.brushesW)
        self.settingsW.layout().addWidget(self.modeW)

        self.pensW.currentDatasetChanged.connect(self.canvasS.onPenChange)
        self.brushesW.currentDatasetChanged.connect(self.canvasS.onBrushChange)
        self.zoomW.valueChanged.connect(self.canvasV.onIntZoomChange)

        self.toolsW.layout().addWidget(self.toolBoxW)
        self.toolsW.layout().addWidget(self.settingsW)
        self.toolsW.layout().addWidget(self.zoomW)
    def setupToolsWidget(self):
        self.toolBoxW = QWidget(self.toolsW)
        self.toolBoxW.setLayout(QVBoxLayout(self.toolBoxW))
        self.straightLineW = QToolButton(self.toolBoxW)
        self.straightLineW.setToolTip(self.tr("Straight Line"))
        self.straightLineW.setIcon(self.createStraightLineIcon())

        self.polygonLineW = QToolButton(self.toolBoxW)
        self.polygonLineW.setToolTip(self.tr("Polygon"))
        self.polygonLineW.setIcon(self.createPolygonLineIcon())

        self.rectangleW = QToolButton(self.toolBoxW)
        self.rectangleW.setToolTip(self.tr("Rectangle"))
        self.rectangleW.setIcon(self.createRectangleIcon())

        self.ellipseW = QToolButton(self.toolBoxW)
        self.ellipseW.setToolTip(self.tr("Ellipse"))
        self.ellipseW.setIcon(self.createEllipseIcon())

        self.pathW = QToolButton(self.toolBoxW)
        self.pathW.setToolTip(self.tr("Path"))
        self.pathW.setIcon(self.createPathIcon())

        self.deleteW = QToolButton(self.toolBoxW)
        self.deleteW.setToolTip(self.tr("Delete"))
        self.deleteW.setIcon(self.createTextIcon(self.tr("D")))

        self.editW = QToolButton(self.toolBoxW)
        self.editW.setToolTip(self.tr("Edit"))
        self.editW.setIcon(self.createTextIcon(self.tr("E")))

        self.moveW = QToolButton(self.toolBoxW)
        self.moveW.setToolTip(self.tr("Move"))
        self.moveW.setIcon(self.createTextIcon(self.tr("M")))
        self.moveW.setEnabled(False)

        self.toolBoxW.layout().addWidget(self.straightLineW)
        self.toolBoxW.layout().addWidget(self.polygonLineW)
        self.toolBoxW.layout().addWidget(self.rectangleW)
        self.toolBoxW.layout().addWidget(self.ellipseW)
        self.toolBoxW.layout().addWidget(self.pathW)
        self.toolBoxW.layout().addWidget(self.editW)
        self.toolBoxW.layout().addWidget(self.moveW)
        self.toolBoxW.layout().addWidget(self.deleteW)

        self.straightLineW.clicked.connect(self.onStraightLineRequest)
        self.rectangleW.clicked.connect(self.onRectangleRequest)
        self.polygonLineW.clicked.connect(self.onPolygonLineRequest)
        self.ellipseW.clicked.connect(self.onEllipseRequest)
        self.pathW.clicked.connect(self.onPathRequest)
        self.deleteW.clicked.connect(self.onDeleteRequest)
        self.editW.clicked.connect(self.onEditRequest)
        self.moveW.clicked.connect(self.onMoveRequest)
        self.straightLineW.clicked.connect(self.canvasS.drawStraightLine)
        self.rectangleW.clicked.connect(self.canvasS.drawRectangle)
        self.ellipseW.clicked.connect(self.canvasS.drawEllipse)
        self.polygonLineW.clicked.connect(self.canvasS.drawPolygon)
        self.pathW.clicked.connect(self.canvasS.drawPainterPath)
        self.editW.clicked.connect(self.canvasS.onEdit)
        self.deleteW.clicked.connect(self.canvasS.onDelete)
        self.moveW.clicked.connect(self.canvasS.onMove)
    def setValue(self, drawing):
        self.drawing = drawing
        self.canvasS.drawing = self.drawing
        for l in self.drawing.straightLines:
            self.canvasS.addItem(StraightLineItem(l))
        for r in self.drawing.rectangles:
            self.canvasS.addItem(RectangleItem(r))
        for e in self.drawing.ellipses:
            self.canvasS.addItem(EllipseItem(e))
        for p in self.drawing.polygons:
            self.canvasS.addItem(PolygonItem(p))
        for p in self.drawing.painterPaths:
            self.canvasS.addItem(PainterPathItem(p))
          
    def createEmptyIcon(self, w=20, h=20):
        pm = QPixmap(w, h)
        pm.fill(Qt.white)
        return pm
    def createIconPen(self):
        p = QPen(Qt.black)
        p.setWidth(1)
        p.setStyle(Qt.SolidLine)
        return p
    def createStraightLineIcon(self):
        pm = self.createEmptyIcon()
        ptr = QPainter()
        ptr.setPen(self.createIconPen())
        ptr.begin(pm)
        ptr.drawLine(0, 0, 20, 20)
        ptr.end()
        return QIcon(pm)
    def createPolygonLineIcon(self):
        pm = self.createEmptyIcon()
        ptr = QPainter()
        poly = QPolygonF()
        poly.append(QPointF(0, 0))
        poly.append(QPointF(15, 10))
        poly.append(QPointF(20, 20))
        poly.append(QPointF(0, 10))
        poly.append(QPointF(5, 5))
        ptr.setPen(self.createIconPen())
        ptr.begin(pm)
        ptr.drawPolygon(poly)
        ptr.end()
        return QIcon(pm)
    def createRectangleIcon(self):
        pm = self.createEmptyIcon()
        ptr = QPainter()
        ptr.setPen(self.createIconPen())
        ptr.begin(pm)
        ptr.drawRect(5, 0, 15, 20)
        ptr.end()
        return QIcon(pm)
    def createPolygonIcon(self):
        pm = self.createEmptyIcon()
        ptr = QPainter()
        ptr.setPen(self.createIconPen())
        ptr.begin(pm)
        ptr.drawEllipse(5, 0, 15, 20)
        ptr.end()
        return QIcon(pm)
    def createEllipseIcon(self):
        pm = self.createEmptyIcon()
        ptr = QPainter()
        ptr.setPen(self.createIconPen())
        ptr.begin(pm)
        ptr.drawEllipse(5, 0, 15, 20)
        ptr.end()
        return QIcon(pm)
    def createPathIcon(self):
        pm = self.createEmptyIcon()
        ptr = QPainter()
        poly = QPainterPath()
        poly.lineTo(QPointF(0, 0))
        poly.lineTo(QPointF(20, 15))
        poly.lineTo(QPointF(20, 0))
        poly.lineTo(QPointF(0, 10))
        poly.lineTo(QPointF(5, 5))
        ptr.setPen(self.createIconPen())
        ptr.begin(pm)
        ptr.drawPath(poly)
        ptr.end()
        return QIcon(pm)
    def createTextIcon(self, txt):
        pm = self.createEmptyIcon()
        ptr = QPainter()
        ptr.setPen(self.createIconPen())
        ptr.begin(pm)
        ptr.drawText(0, 10, txt)
        ptr.end()
        return QIcon(pm)
    def onStraightLineRequest(self):
        self.modeW.setText(self.tr("Straight Line"))
    def onPolygonLineRequest(self):
        self.modeW.setText(self.tr("Polygon Line"))
    def onRectangleRequest(self):
        self.modeW.setText(self.tr("Rectangle"))
    def onEllipseRequest(self):
        self.modeW.setText(self.tr("Ellipse"))
    def onPathRequest(self):
        self.modeW.setText(self.tr("Path"))
    def onDeleteRequest(self):
        self.modeW.setText(self.tr("Delete"))
    def onMoveRequest(self):
        self.modeW.setText(self.tr("Move"))
    def onEditRequest(self):
        self.modeW.setText(self.tr("Edit"))
