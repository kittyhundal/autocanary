import os, sys, platform
from glob import glob

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = open('version').read().strip()

system = platform.system()

if system == 'Linux':
    setup(
        name='autocanary',
        version=version,
        author='Micah Lee',
        author_email='micah.lee@firstlook.org',
        packages=['autocanary'],
        include_package_data=True,
        scripts=['install/autocanary'],
        data_files=[
            (os.path.join(sys.prefix, 'share/applications'), ['install/autocanary.desktop']),
            (os.path.join(sys.prefix, 'share/pixmaps'), ['install/autocanary.xpm']),
            (os.path.join(sys.prefix, 'share/autocanary'), ['share/icon.png'])
        ]
    )

elif system == 'Darwin':
    setup(
        name='AutoCanary',
        app=['autocanary-launcher.py'],
        data_files=[],
        options={
            'py2app': {
                'argv_emulation': True,
                'iconfile':'install/icon.icns',
                'includes': ['sip', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'],
                'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.phonon']
            }
        },
        setup_requires=['py2app'],
    )
