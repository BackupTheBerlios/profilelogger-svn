from Gui.Dialogs.EditorDialog import *

from Logic.Model.FieldBookEntry import *

class FieldBookEntryEditorDialog(EditorDialog):
    def __init__(self, parent, entity):
        EditorDialog.__init__(self, parent, entity)
