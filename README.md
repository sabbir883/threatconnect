# threatconnect

This script usees modules/packages from  Threat connect SDK so it is necessary to setup those packages. Below is what we need to to setup the SDK. Once the SDK is setup correctly  scripts in the repository will work withoug errors. 

For windows environment
=====================================

1. Install Python 2.7.10 from https://www.python.org/downloads/ . 
2. Add python to the system path variable
3. Upgrade setuptools for python to version 18.2. Go to below url to download .
https://bootstrap.pypa.io/ez_setup.py . Once you have downloaded the .py file run using below .

python ez_setup.py

4.Download Threatconnect SDK from github. Please use below link and download the zip file.
https://github.com/ThreatConnect-Inc/threatconnect-python . Unzip the file . From the commandline
browse to the unzipped folder and run the setup.py using below. 

python setup.py install --force 
