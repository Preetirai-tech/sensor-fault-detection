from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
  """
  This function will return list of requirements
  """
  requirements_list:List[str] = []
  return requirements_list

setup(

  name = "sensor",
  version = "0.0.1",
  author = "Preetirai",
  author_email = "preetirai1812@yahoo.com",
  packages = find_packages(),
  install_requires = get_requirements(),
)
