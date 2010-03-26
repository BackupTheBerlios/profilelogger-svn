from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
