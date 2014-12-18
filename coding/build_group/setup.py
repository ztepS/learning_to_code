from distutils.core import setup
import py2exe
setup(
        windows=['group_thoughts.py'],
        options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "includes": ["PyQt4", "PyQt4.QtGui", "PyQt4.QtCore",  "pyodbc", "decimal", "sip", "datetime"]
                }
        }
)