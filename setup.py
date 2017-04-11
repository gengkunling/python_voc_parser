from setuptools import setup

setup(name='python_voc_parser',
      version='0.1',
      description='Python pascal voc dataset parset',
      # see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5'
      ],
      url='https://github.com/gabrielrezzonico/python_voc_parser',
      author='Gabriel Rezzonico',
      author_email='gabrielrezzonico@gmail.com',
      license='MIT',
      packages=['python_voc_parser'],
      # $ pip install -e .[dev,test]
      extras_require={
          'dev': ['sphinx'],
          'test': ['pytest', 'pytest-cov'],
      },
      install_requires=[],
      zip_safe=False)

