#######
# Core: Logs
#######

import logging
from logging.handlers import RotatingFileHandler

class Enable:
    """ Boolean value indicating that logs are enabled """
    
    boolean = False


class Access:
    """ Access current log """
    
    log = None


class Logs:
    """ Logging class
    
    This will log most of what is happening in the console 
    and save it as terasploit.log in current working directory.
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
        
        setattr(Enable,'boolean',True)
        setattr(Access,'log',logger)
        
        
class Logger:
    """ Logger Class """
    
    def __init__(self,type,message):
        if Enable.boolean == True:
            if type.lower() == 'info':
                Access.log.info(message)
            if type.lower() == 'error':
                Access.log.error(message)
        if Enable.boolean == False:
            return
