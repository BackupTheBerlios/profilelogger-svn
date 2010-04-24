from Gui.Dialogs.EditorDialog import *

from Logic.Model.StratigraphicUnit import *

class StratigraphicUnitEditorDialog(EditorDialog):
    def __init__(self, parent, entity):
        EditorDialog.__init__(self, parent, entity)
