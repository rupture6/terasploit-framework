""" Framework Information

All information of the framework including its license and version.
this can be accessed by importing 'info.py' and fetching the dictionary
it will return.

This is used on banners.
"""

def information() -> dict:
    return {
        'framework-version'  :  'v1.3.0-dev',
        'framework-license'  :  'BSD-3-Clause License',
        'framework-github'   :  'https://github.com/rupture6/terasploit-framework',
        'dev-email'          :  '<rupture6.dev[at]gmail.com>'
    }
