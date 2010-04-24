class ConnectionData:
    def __init__(self, host=None, port=None, dbName=None, 
                 user=None, password=None,
                 createSchema=False, insertTemplateData=False):
        self.host = unicode(host)
        self.port = unicode(port)
        self.dbName = unicode(dbName)
        self.user = unicode(user)
        self.password = unicode(password)
        self.createSchema = createSchema
        self.insertTemplateData = insertTemplateData
        
    def makeConnectionString(self):
        return u'postgresql://%s:%s@%s:%s/%s' % (
            self.user,
            self.password,
            self.host,
            self.port,
            self.dbName)
    def makeInfoString(self):
        return u'%s@%s:%s/%s' % (self.user, 
                                 self.host, 
                                 self.port, 
                                 self.dbName, 
                                 self.schema)
