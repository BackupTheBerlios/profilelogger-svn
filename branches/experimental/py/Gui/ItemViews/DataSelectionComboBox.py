from Gui.Widgets.ComboBox import *

from Model.Dataset import Dataset

class DataSelectionComboBox(ComboBox):
    currentDatasetChanged = pyqtSignal(Dataset)
    def __init__(self, parent, model):
        ComboBox.__init__(self, parent)
        self.setModel(model)
        self.currentIndexChanged.connect(self.onCurrentIndexChanged)
    def onCurrentIndexChanged(self, idx):
        ds = self.model().getDataFromIntIndex(idx)
        self.currentDatasetChanged.emit(ds)
