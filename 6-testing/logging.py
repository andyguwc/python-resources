################################################
# Logging 
################################################

# https://www.loggly.com/ultimate-guide/python-logging-basics/
# https://docs.python.org/3/howto/logging-cookbook.html
# https://docs.python-guide.org/writing/logging/

'''
logging basics
'''
# To emit a log message, a caller first requests a named logger. 
# The name can be used by the application to configure different rules for different loggers. 
# This logger then can be used to emit simply-formatted messages at different log levels (DEBUG, INFO, ERROR, etc.), 
# which again can be used by the application to handle messages of higher priority different than those of a lower priority. 
# While it might sound complicated, it can be as simple as this:

import logging
logging.basicConfig(level=logging.INFO) 
log = logging.getLogger("my-logger")
log.info("Hello, world")

# Internally, the message is turned into a LogRecord object and routed to a Handler object registered for this logger. 
# The handler will then use a Formatter to turn the LogRecord into a string and emit that string.

# In addition to a name, Logger can be configured with a list of handlers that
# determines where the messages are written and a list of Filters to determine which
# kinds of messages are passed or rejected. A logger is the essential API for logging:
# we use a logger to create LogRecords. These records are then routed to Filters and
# Handlers, where the passed records are formatted and eventually wind up getting
# stored in a local file or transmitted over a network.

# The best practice is to have a distinct logger for each of our classes or modules. As
# Logger names are .-separated strings, the Logger names can parallel class or module
# names; our application's hierarchy of component definitions will have a parallel
# hierarchy of loggers.


import logging
class Player:
    def __init__(self, bet, strategy, stake):
        # ensure the Logger object for this class have a name that matches the qualified name of the class 
        self.logger = logging.getLogger(self.__class__.__qualname__)
        self.logger.debug("init bet {}, strategy {}, stake {}".format(bet, strategy, stake))


# create a shared class level logger 
# define a decorator that creates the logger outside the class definition itself 
def logged(class_):
    class_.logger = logging.getLogger(class_.__qualname__)
    return class_

@logged 
class Player:
    def __init__(self, bet, strategy, stake):
        self.logger.debug("init bet {}, strategy {}, stake {}".format(bet, strategy, stake))

'''
config the loggers 
'''
# https://www.machinelearningplus.com/python/python-logging-guide/

# In general, a configuration consists of adding a Formatter and a Handler to the root logger. 
# Because this is so common, the logging module provides a utility function called basicConfig that handles a majority of use cases.
# - the logger needs to be associated with a handler that produces output
# - the handler needs a logging level that will pass our logging messages 
import logging 
import sys 
# permits a few parameters to create a logging.handlers.StreamHandler to create the output 
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


# configure formatter and handler 
import logging 

# get or create a logger (if same name then the same logger)
logger = logging.getLogger(__name__)

# set log level 
logger.setLevel(logging.WARNING)

# define the handler and set formatter 
file_handler = logging.FileHander('logfile.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger 
logger.addHandler(file_handler)

# logs 
logger.debug('A debug message')
logger.error('An error message'

)

# example sending to syslog
import logging
import logging.handlers
import os
 
class SyslogBOMFormatter(logging.Formatter):
    def format(self, record):
        result = super().format(record)
        return "ufeff" + result
 
handler = logging.handlers.SysLogHandler('/dev/log')
formatter = SyslogBOMFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)
 
try:
    exit(main())
except Exception:
    logging.exception("Exception in main()")
    exit(1)


'''
naming the loggers
'''
#  - module name 
import logging 
logger = logging.getLogger(__name__)


# - object instances 
# create logger in the __init__() method. Logger will be unique to the instance 
import logging
def __init__(self, player_name):
    self.name = player_name
    self.logger = logging.getLogger("{}{}".format(
        self.__class__.__qualname__, player_name))

# - class names 
# using __class__.__qualname__ as the Logger name and assign Logger to the class as a whole


'''
levels of logging 
'''
# DEBUG: Detailed information, for diagnosing problems. Value=10.
# INFO: Confirm things are working as expected. Value=20.
# WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
# ERROR: More serious problem, the software is not able to perform some function. Value=40
# CRITICAL: A serious error, the program itself may be unable to continue running. Value=50


'''
what to log
'''
# Diagnostic logging
# - Diagnostic logging records events related to the application’s operation. If a user calls in to report an error, for example, the logs can be searched for context.

# Audit logging
# - Audit logging records events for business analysis. A user’s transactions (such as a clickstream) can be extracted and combined with other user details (such as eventual purchases) for reports or to optimize a business goal.


'''
YAML config
'''
import logging.config 
import yml 
config_ict = yml.load(config)
logging.config.dictConfig(config_dict)

The logging.config.dictConfig() method has the default behavior of disabling any loggers created prior to configuration.


'''
specialized logging
'''
# Errors and Control: Basic error and control of an application leads to a
# main log that helps users confirm that the program really is doing what it's
# supposed to do. This would include enough error information with which
# the users can correct their problems and rerun the application. If a user
# enables verbose logging, it will amplify this main error and control the log
# with additional user-friendly details.

# Debugging: This is used by developers and maintainers; it can include
# rather complex implementation details. We'll rarely want to enable blanket
# debugging, but will often enable debugging for specific modules or classes

# Audit: This is a formal confirmation that tracks the transformations applied
# to data so we can be sure that processing was done correctly.

# Security: This can be used to show us who has been authenticated; it can
# help confirm that the authorization rules are being followed. It can also be
# used to detect some kinds of attacks that involve repeated password failures.

from collections import Counter 
class Main:
    def __init__(self):
        self.balance = Counter()
        self.log = logging.getLogger(self.__class__.__qualname__)
    def run(self):
        self.log.info("Start")

        # some processing
        self.balance['count'] += 1
        self.balance['balance'] += 3.14
        self.log.info( "Counts {0}".format(self.balance) )
        for k in self.balance:
            self.log.info( "{0:.<16s} {1:n}".format(k, self.balance[k]) )

# warnings module
# In the case of developers, we may use warnings to show you that an API has been deprecated. 
# In the case of users, we might want to show you that the results are questionable but not—strictly speaking—erroneous.

# example of warnings on api changes
import warnings 
class Player: 
    __version__ = "2.2"
    def bet(self):
        warnings.warn("bet is deprecated use place_bet", 
        DeprecationWarning, stacklevel=2)

# showing configuration problems with a warnings 
# try multiple import alternatives 
import warnings 
try: 
    import simulation_model_1 as model 
except ImportError as e:
    warnings.warn(e)
if 'model' not in globals():
    try: 
        import simulation_model_2 as model 
    except ImportError as e:
        warnings.warn(e)
if 'model' not in globals():
    raise ImportError("Missing simulation_model_1 and simulation_model_2")

# warnings vs log warning 
# If a timeout occurs, a warning message is written to the log and the program keeps
# running. The content of the resource will be set to an empty list. The log message will
# be written every time, vs. A warnings module warning is ordinarily shown only once
# from a given location in the program and is suppressed after that.

