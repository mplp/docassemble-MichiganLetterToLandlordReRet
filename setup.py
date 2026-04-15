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

setup(name='docassemble.MichiganLetterToLandlordReRet',
      version='1.0.999',
      description=('DIY tool for writing a Letter to Landlord (Security Deposit)'),
      long_description='# docassemble.MichiganLetterToLandlordReRet\r\n\r\nDIY tool for writing a Letter to Landlord (Security Deposit)\r\n\r\n## Author\r\n\r\n## Changelog\r\n* 12/12/25  1.0.1 Update embedded survey; update styling on instructions page\r\n* 9/30/24   Update cover letter; download screen; user survey\r\n* Jan 2024  Incorporate MLH testing feedback. bharrison\r\n* Oct 2023  Various enhancements per initial testing feedback. bharrison\r\n* Aug 2023  Refactor and complete. Brett Harrison\r\n* 2023      Initial dev by Suffolk member Bianca Stella Bruschi\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Brett Harrison',
      author_email='harrison.brett.m@gmail.com',
      license='MIT',
      url='https://michiganlegalhelp.org/resources/housing',
      packages=find_namespace_packages(),
      install_requires=['docassemble.AssemblyLine @ git+https://github.com/SuffolkLITLab/docassemble-AssemblyLine.git@main'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MichiganLetterToLandlordReRet/', package='docassemble.MichiganLetterToLandlordReRet'),
     )
