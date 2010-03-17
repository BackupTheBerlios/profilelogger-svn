from GraphicsView import *

class ProfileView(GraphicsView):
    def __init__(self, parent):
        GraphicsView.__init__(self, parent)
        self.setEnabled(False)
        self.setScene(QApplication.instance().profileScene)
        QApplication.instance().profileScene.enableViews.connect(self.onEnableView)
        QApplication.instance().profileScene.disableViews.connect(self.onDisableView)
    def onEnableView(self):
        self.setEnabled(True)
    def onDisableView(self):
        self.setEnabled(False)
