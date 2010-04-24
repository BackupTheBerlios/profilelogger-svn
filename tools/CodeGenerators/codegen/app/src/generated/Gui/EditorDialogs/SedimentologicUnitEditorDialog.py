from Gui.Dialogs.EditorDialog import *

from Logic.Model.SedimentologicUnit import *

class SedimentologicUnitEditorDialog(EditorDialog):
    def __init__(self, parent, entity):
        EditorDialog.__init__(self, parent, entity)
