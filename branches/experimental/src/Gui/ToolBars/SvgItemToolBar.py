from ToolBar import *

from Gui.Widgets.SvgItemSelectionComboBox import *

from Model.SVGItem import *

class SvgItemToolBar(ToolBar):
    currentSvgItemChanged = pyqtSignal(SVGItem)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.svgItemsW = SvgItemSelectionComboBox(self)
        self.svgItemsW.currentDatasetChanged.connect(self.onSvgItemChange)
        self.addWidget(QLabel(self.tr("SVG Items:"), self))
        self.addWidget(self.svgItemsW)
    def onSvgItemChange(self, p):
        self.currentSvgItemChanged.emit(p)
