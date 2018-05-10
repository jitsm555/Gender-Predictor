from setuptools import setup, find_packages

setup(name='Gender-Predictor',  # This is the name of your PyPI-package.
      version='0.4',  # Update the version number for new releases
      description='Classify the name based on given name',
      author='Jitesh-Mohite',
      author_email='jiteshmohite619@gmail.com',
      maintainer='Mustafa Atik',
      maintainer_email='muatik@gmail.com',
      packages=['gender_predictor'],
      package_data={'gender_predictor': ['data/*']},
      url='https://github.com/jiteshmohite/Gender-Predictor',
      install_requires=['nltk'], )