from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    
    This function will return a list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines as file
            lines=file.readlines()
            ##Process each line 
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network Security",
    version= "0.0.1",
    author= "Taran Aditya",
    author_email="taran.airrr@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)