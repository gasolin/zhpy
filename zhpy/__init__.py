try:
    import psyco
    psyco.full()
except ImportError:
        pass

from release import version
__version__ = version

from zhpy import *