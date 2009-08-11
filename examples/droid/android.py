class Android(object):
    """
    The mock up of 
    http://code.google.com/p/android-scripting/source/browse/python/ase/android.py
    """
    def __init__(self):
        print "Create Android instance"
    
    def makeToast(self, text):
        print "message: " + text
    
    def getInput(self, text):
        print "get input: "
    
    def Speak(self, text):
        print "speak: " + text
        
    def scanBarcode(self):
        print "Start barcode scaning ..."
        return "1234567890123"
    
    def captureImage(self):
        print "get image"