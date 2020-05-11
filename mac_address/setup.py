from setuptools import setup, find_packages

setup(name='mac_address',
      packages=find_packages("."),
      version='0.1',
      author='Dor Green',
      author_email='dorgreen1@gmail.com',
      description='Parsing and conversion of MAC addresses',
      url='http://github.com/KimiNewt/mac_address',
      license='MIT',
      py_modules=['mac_address'],
      classifiers=[
          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
      ])
