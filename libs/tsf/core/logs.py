#######
# Core: Logs
#######

import logging
from logging.handlers import RotatingFileHandler

class Logs(object):
    """ Logging class
    
    This will log most of what is happening in the console 
    and save it as console.log in current working directory.
    If you are interested in seeing the contents of logs,
    use 'cat terasploit.log'.
    """

    def logs(self) -> None:
        logformat = logging.Formatter('[%(asctime)s] %(name)s :: %(levelname)s - %(message)s')
        loghandler = RotatingFileHandler('terasploit.log', maxBytes=1000000)
        loghandler.setFormatter(logformat)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(loghandler)