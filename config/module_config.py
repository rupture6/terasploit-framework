#!/usr/bin/env python3
import os
import json

# Path of modules-metadata starting from root '/'
modules_metadata = f"{os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))}/db/module-metadata.json"

def get_module_metadata():
    """ Opens and Parse the json file """
    
    root_privileges = True if os.geteuid() == 0 else False
    if not root_privileges:
        with open(modules_metadata,'r') as json_db:
            database = json.load(json_db)
    if root_privileges:
        with open(modules_metadata, 'r+') as json_db:
            database = json.load(json_db)
    return database


class modules_metadata_database:
    """ Modules Metadata Database: Distributor Class - Returns the whole metadata database """
    
    def get() -> dict:
        modules_metadata_database = get_module_metadata()
        
        return modules_metadata_database


class directories:
    """ Directories: Distributor Class - Returns all module dirs from modules metadata database """

    def get() -> list:
        modules_metadata_database = get_module_metadata()
        dirs = modules_metadata_database['module-directories']
        
        return dirs


class modules:
    """ Modules: Distributor Class - Returns all modules contents from modules metadata database """
    
    def get() -> tuple[dict,dict,dict,dict]:
        modules_metadata_database = get_module_metadata()
        Auxiliary  =  modules_metadata_database['modules']['auxiliary']
        Encoders   =  modules_metadata_database['modules']['encoder']
        Exploits   =  modules_metadata_database['modules']['exploit']
        Payloads   =  modules_metadata_database['modules']['payload']
        
        return Auxiliary, Encoders, Exploits, Payloads