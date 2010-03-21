from CanvasItemEditorDialog import *

class LineItemEditorDialog(CanvasItemEditorDialog):
    def __init__(self, parent, itm):
        CanvasItemEditorDialog.__init__(self, parent, itm)
        self.addContentWidget(self.tr("Line Item"))
        self.addPenWidthEditor()
        self.addPenColorEditor()
        self.addPenCapStyleEditor()
        self.addPenJoinStyleEditor()
        self.addPenStyleEditor()
#self.addBrushColorEditor()
#self.addBrushStyleEditor()
        self.addButtons()
