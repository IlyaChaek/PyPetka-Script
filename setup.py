from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r', encoding='utf-8') as f:
    return f.read()

setup(
  name='PyPetka-Script',
  version='2.4.2',
  author='Chorelin',
  author_email='miheevila6@gmail.com',
  description='Модуль для упрощения работы с Python, созданный командой PyPetka Team.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/IlyaChaek/PyPetka-Script',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.13',
    'License :: Freeware',
    'Operating System :: Microsoft :: Windows :: Windows 10',
  ],
  keywords='Python language module PyPetka NewLanguage programming language development',
  project_urls={
    'Documentation': 'https://github.com/IlyaChaek/PyPetka-Script',
  },
  python_requires='>=3.6'
)
