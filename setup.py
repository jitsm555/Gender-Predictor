from setuptools import setup, find_packages

setup(name='Gender-Predictor',  # This is the name of your PyPI-package.
      version='0.3',  # Update the version number for new releases
      description='Classify the name based on given name',
      author='Jitesh-Mohite',
      author_email='jiteshmohite619@gmail.com',
      url='https://github.com/jiteshmohite/Gender-Predictor',
      packages=find_packages(),
      install_requires=['nltk'], )
