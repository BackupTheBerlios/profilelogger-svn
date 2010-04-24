from Gui.Dialogs.EditorDialog import *

from Logic.Model.Profile import *

class ProfileEditorDialog(EditorDialog):
    def __init__(self, parent, entity):
        EditorDialog.__init__(self, parent, entity)
