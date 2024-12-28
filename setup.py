from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements 
    '''
    HYPHEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        '''we don't want \n from reqirements.py to be in list'''
        [req.replace("\n"," ") for req in requirements]

        '''we don't want -e . from reqirements.py to be in list'''
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='ML_Project',
    author='Jayati Kariya',
    version='0.0.1',
    author_email='kariyajayati@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
    
    


)