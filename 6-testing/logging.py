################################################
# Logging 
################################################

# https://www.loggly.com/ultimate-guide/python-logging-basics/
# https://docs.python.org/3/howto/logging-cookbook.html
# https://docs.python-guide.org/writing/logging/
# https://www.machinelearningplus.com/python/python-logging-guide/
# https://www.pylenin.com/blogs/python-logging-guide/


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
# names; our application's hierarchy of component definitions will have a parallel hierarchy of loggers.


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
logging in applications / modules
'''

# Logging hierarchy
# https://docs.python.org/3/howto/logging-cookbook.html
# https://stackoverflow.com/questions/4150148/logging-hierarchy-vs-root-logger
# Application code can define and configure a parent logger in one module and create (but not configure) a child logger in a separate module, and all logger calls to the child will pass up to the parent. Here is a main module

# Here is a main module:

import logging
import auxiliary_module

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = auxiliary_module.Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
auxiliary_module.some_function()
logger.info('done with auxiliary_module.some_function()')


# Here is the auxiliary module:

import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')

class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')


'''
logging examples for applications
'''

# Example 1
# Configure logging 
# https://github.com/CryptoSignal/Crypto-Signal/blob/7ea9255ed5c3dd9b3212a43bd489e85271792670/app/logs.py#L10-L40



# Example 2
# configure logging in the main entrypoint file 
# https://github.com/Diaoul/subliminal/blob/a4113adb745dc5cd2da7254ee14802077237bb15/subliminal/cli.py#L263-L268
if debug:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
    logging.getLogger('subliminal').addHandler(handler)
    logging.getLogger('subliminal').setLevel(logging.DEBUG)
# in other places (submodules of subliminal) just use getLogger(__name__) which is child of that logger
# https://github.com/Diaoul/subliminal/blob/a4113adb745dc5cd2da7254ee14802077237bb15/subliminal/providers/shooter.py#L12


# Example 3
# configure logging in basicConfig in the __main__.py entry file https://github.com/0xHJK/music-dl/blob/883b643d62c63496572f5b883f76359324a5c853/music_dl/__main__.py#L142-L147
def main(...):
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)-8s | %(name)s: %(msg)s ",
        datefmt="%H:%M:%S",
    )
# use the logging in specific files https://github.com/0xHJK/music-dl/blob/69ca4ded11a0318e700d3bb0de0ed19bdc9fb798/music_dl/source.py#L30

class MusicSource:
    """
        Music source proxy object
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

'''
logging for flask
'''

# Example 1 Flask application
# configure the logger
# https://github.com/cookiecutter-flask/cookiecutter-flask/blob/3e53bdb824c057a64331e6fa034cae54dc7d3b0d/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/app.py#L87-L91
def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
# using the logger
# https://github.com/cookiecutter-flask/cookiecutter-flask/blob/a3e168e3facf2304bd2b4b6e5e868dfd95e8df94/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/public/views.py#L33
from flask import current_app
current_app.logger.info("Hello from the home page!")


# Example 2 Flask application
# configure logger https://github.com/lufficc/flask_ishuhui/blob/a3444b3679c45d5ba94c5c9a66551207eff1a646/ishuhui/logger/__init__.py#L1-L11
import logging
from logging.handlers import RotatingFileHandler

def init_logger(app):
    handler = RotatingFileHandler('logs/ishuhui.log', maxBytes=1024 * 1024 * 2, backupCount=2)
    logging_format = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)


def create_app(config, should_register_blueprints=True):
    app = Flask(__name__)
    app.config.from_object(config)
    from ishuhui.logger import init_logger
    init_logger(app)


# using the logger
# https://github.com/lufficc/flask_ishuhui/blob/a3444b3679c45d5ba94c5c9a66551207eff1a646/ishuhui/tasks/task.py#L33
def refresh_comics():
    page = 0
    comics = load_comics(page)
    current_app.logger.info('get {} comics of page {}'.format(len(comics), page))
    result = []




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

