class ConnectionData:
    def __init__(self, host=None, port=None, dbName=None, schema=None, 
                 user=None, password=None,
                 dropSchema=False, createSchema=False, insertTemplateData=False):
        self.host = unicode(host)
        self.port = unicode(port)
        self.dbName = unicode(dbName)
        self.schema = unicode(schema)
        self.user = unicode(user)
        self.password = unicode(password)
        self.dropSchema = dropSchema
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
        return u'%s@%s:%s/%s/%s' % (self.user, self.host, self.port, self.dbName, self.schema)
