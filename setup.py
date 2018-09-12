from setuptools import setup, find_packages


setup(
    name="SlicePDF",
    version="1.0",
    packages=find_packages(),
    scripts=['slicepdf.py', 'interface.py', 'design.py'],
    install_requires=['fpdf>=1.7.2', 'PyQt5==5.10.1', 'Wand==0.4.4'],
    author="Wagner Cardoso",
    entry_points={'gui_scripts': ['SlicePDF = interface']},
    incluce_package_data=True
    )
