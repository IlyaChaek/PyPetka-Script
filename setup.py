from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='PyPetka Script',
  version='1.1.0',
  author='Chorelin',
  author_email='miheevila6@gmail.com',
  description='Модуль для упрощения работы с Python, созданный командой PyPetka Team.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='home_link',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='example python',
  project_urls={
    'Documentation': 'link'
  },
  python_requires='>=3.7'
)