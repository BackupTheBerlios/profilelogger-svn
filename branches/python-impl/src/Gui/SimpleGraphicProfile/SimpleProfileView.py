from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

from SimpleProfileModel import *

class SimpleProfileView(QGraphicsView):
    def __init__(self, parent):
        QGraphicsView.__init__(self, parent)
        self.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform | QPainter.HighQualityAntialiasing | QPainter.NonCosmeticDefaultPen)
        self.model = SimpleProfileModel(self)
        self.setScene(self.model)
        self.setEnabled(False)
    def hasProfile(self):
        return self.model.profile is not None
    def onProfileChange(self, profile):
        self.model.setProfile(profile)
        self.setEnabled(self.hasProfile())
    def onExportToSvg(self, profile):
        self.onProfileChange(profile)

        fn = QFileDialog.getSaveFileName(self, 
                                         self.tr("Save File"),
                                         QDir.currentPath(),
                                         self.tr("SVG Files (*.svg *.SVG)"));
        if fn.isEmpty():
            return

        gen = QSvgGenerator();
        gen.setSize(QSize(self.scene().sceneRect().width(),
                          self.scene().sceneRect().height()))
        gen.setFileName(fn);
        painter = QPainter();
        painter.begin(gen)
        self.scene().render(painter);
        painter.end();
