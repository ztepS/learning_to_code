from distutils.core import setup
import py2exe
setup(
        windows=['report.py'],
        options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "includes": ["decimal"]
                }
        }
)