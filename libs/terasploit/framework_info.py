""" Framework Information

All information of the framework including its license and version.
this can be accessed by importing 'info.py' and fetching the dictionary
it will return.

This is used on banners.
"""

def information() -> dict:
    return {
        'framework-version'  :  'v1.2.5-dev',
        'framework-license'  :  'BSD-3-Clause License',
        'framework-github'   :  'https://github.com/handler/terasploit-framework',
        'dev-email'          :  'handler4.nsi@gmail.com'
    }