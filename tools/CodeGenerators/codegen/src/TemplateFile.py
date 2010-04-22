class TemplateFile:
    def __init__(self, file):
        self.file = file
    def loadFile(self):
        f = open(self.file, 'r')
        self.data = f.read()
        f.close()
    def replaceKeyword(self, keyword, string):
        self.data = self.data.replace(keyword, string)
