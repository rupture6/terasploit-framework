""" Framework Information

All information of the framework including its license and version.
this can be accessed by importing 'info.py' and fetching the dictionary
it will return.

This is used on banners.
"""

def information() -> dict:
    return {
        
        'framework-version' : 'v1.3.1-dev',
        'framework-license' : 'BSD-3-Clause License',
        
        'framework-release' : 'September 18, 2024.', 
        
        # Github Creation Date: September 18, 2024
        # 
        # It was not released on github when it was still in version 1.0.0,
        # it was officially released in September 18, 2024 in github at
        # version 1.3.0
        
        'framework-github' : 'https://github.com/rupture6/terasploit-framework',
        
        'dev-email' : '<rupture6.dev[at]gmail.com>'
    }