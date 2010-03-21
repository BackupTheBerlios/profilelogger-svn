from FillableItemEditorDialog import *

class EllipseItemEditorDialog(FillableItemEditorDialog):
    def __init__(self, parent, itm):
        CanvasItemEditorDialog.__init__(self, parent, itm)
        self.addContentWidget(self.tr("Ellipse Item"))
        self.addPenWidthEditor()
        self.addPenColorEditor()
        self.addPenCapStyleEditor()
        self.addPenJoinStyleEditor()
        self.addPenStyleEditor()
        self.addBrushColorEditor()
        self.addBrushStyleEditor()
        self.addButtons()
