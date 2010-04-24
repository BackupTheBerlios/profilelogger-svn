from Gui.Dialogs.EditorDialog import *

from Logic.Model.Project import *

class ProjectEditorDialog(EditorDialog):
    def __init__(self, parent, entity):
        EditorDialog.__init__(self, parent, entity)
