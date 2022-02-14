#!/usr/bin/python3

import plistlib
import subprocess

class IORegistryExplorerDumper():

    def __init__(self, output_file_name: str = 'output.plist'):
        self.output_file_name = output_file_name
    
    def getDevicePropertiesByName(self, name):
        ...
    def getDevicePropertiesByHID(self, hid):
        ...

if __name__ == "__main__":
    print("Warning! This script is intended to be run as a library, not a runnable script!")
    return 1

