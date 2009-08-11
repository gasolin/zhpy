class Android(object):
    """
    The mock up of 
    http://code.google.com/p/android-scripting/source/browse/python/ase/android.py
    """
    def __init__(self):
        print "Create Android instance"
    
    def ScanBarcode(self):
        print "Start barcode scaning ..."
        return "1234567890123"