import setuptools

with open('README.md', 'r') as fh:
     long_description = fh.read()

setuptools.setup(
  name = 'getPDFmetadata',
  version = '1.0.0',
  author = 'Newton Galiza',
  author_email = 'newtonjgaliza@gmail.com',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/NewtonGaliza/getPDFmetadata',
  packages = setuptools.find_packages(),
  classifiers = ['Programming Language :: Python :: 3'],
  install_requires = ['optparse', 'PyPDF2']

)
