import sys

fn = 'dist/ProfileLogger.app/Contents/Resources/__boot__.py'
print "opening file '",fn,"'..."
f = open(fn, 'r')
print "reading content..."
s = f.read()
f.close()

print "patching..."
s = s.replace('import os, sys, site', """import os, sys, site
    sys.path = [os.path.join(os.environ['RESOURCEPATH'], 'lib', 'python2.5', 'lib-dynload')] + sys.path""")
print "writing patched file..."
f = open(fn, 'w')
f.write(s)
print "closing file..."
f.close()
print "done patching: ", fn
