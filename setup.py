import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.209aPlaintiffMotionToModify',
      version='0.2.0',
      description=("A docassemble extension for MA plaintiff's motion to modify a 209A using the docassemblyline process."),
      long_description="# docassemble.209aPlaintiffMotionToModify\r\n\r\nA docassemble extension for MA plaintiff's motion to modify a restraining order using the docassemblyline process.\r\n",
      long_description_content_type='text/markdown',
      author='Mark Ferraretto, @plocket, Luke Karis, Caroline Robinson, and Kate Barry',
      author_email='52798256+plocket@users.noreply.github.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=['docassemble.ALMassachusetts>=0.1.2', 'docassemble.AssemblyLine>=2.23.0', 'docassemble.MACourts>=0.59.1', 'docassemble.MassAccess>=0.3.0'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/209aPlaintiffMotionToModify/', package='docassemble.209aPlaintiffMotionToModify'),
     )

