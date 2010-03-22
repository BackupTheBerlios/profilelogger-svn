from FillableItemEditorDialog import *

class PathItemEditorDialog(FillableItemEditorDialog):
    def __init__(self, parent, itm):
        CanvasItemEditorDialog.__init__(self, parent, itm)
        self.addContentWidget(self.tr("Path Item"))
        self.addPenWidthEditor()
        self.addPenColorEditor()
        self.addPenCapStyleEditor()
        self.addPenJoinStyleEditor()
        self.addPenStyleEditor()
        self.addBrushColorEditor()
        self.addBrushStyleEditor()
        self.addButtons()
