from setuptools import setup

APP = ['ProfileLogger.py']
OPTIONS = {'argv_emulation': True, 
           'includes': ['sip', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui', 'PyQt4.QtNetwork', 'PyQt4.QtXml', 
                        'psycopg2', 'psycopg2.*',
                        'sqlalchemy',
                        'sqlalchemy.*', 'sqlalchemy.databases.*', 'sqlalchemy.databases.*', 
                        'sqlalchemy.dialects.*', 'sqlalchemy.dialects.postgres.*', 'sqlalchemy.engine.*', 
                        'sqlalchemy.ext.*', 'sqlalchemy.orm.*', 'sqlalchemy.sql.*', ],
           'excludes': ['PyQt4.QtDesigner',  'PyQt4.QtOpenGL', 'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.phonon']}
 
setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],)
