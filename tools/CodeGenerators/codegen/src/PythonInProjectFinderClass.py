from PythonFinder import *

class PythonInProjectFinderClass(PythonFinderClass):
    def __init__(self, module, name, dataClassName, template):
        PythonFinderClass.__init__(self, module, name, dataClassName, template)
    def doFindAllInProject(self, dataClass, project):
        if project is None:
            return None
        return self.getSession().query(dataClass).filter(dataClass.project == project).all()
