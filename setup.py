#!/usr/bin/env python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
        packages=['diarc','diarc.diarc', 'diarc.qt_view', 'diarc.ascii_view', 'diarc.ros'],
        package_dir={'': 'src'}
        )

setup(**d)
