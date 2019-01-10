from distutils.core import setup
from glob import glob

setup(name='finite-element-course',
      version=2018.0,
      description="""Skeleton finite element implementation in support of maths M345A47 at
Imperial College London""",
      author="David Ham",
      author_email="david.ham@imperial.ac.uk",
      url="https://finite-element.github.io/",
      packages=["fe_utils"],
      scripts=glob('scripts/*'))
