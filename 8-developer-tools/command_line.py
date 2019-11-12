##################################################
#  Command Line 
##################################################


'''
os interface
'''
# the shell starts applications with several information that constitute the OS API 
# - collection of environment variables accessd via os.environ
# - standard files: sys.stdin, sys.stdout, sys.stderr
# - command line is parsed by the shell into words. Available in sys.argv
# - the OS also maintains context settings such as current working directory

# The file named on the first word of a command must have execute (x) permission.
# The shell command, chmod +x somefile.py, marks a file as executable. A filename
# that matches but isn't executable gets an OS Permission Denied error.



# #!/usr/bin/env python3.3
# If a Python file has permission to execute, and has this as the first line, then the shell
# will run the env program. The env program's argument (python3.3) will cause it to
# set up an environment and run the Python3.3 program with the Python file as the
# first positional argument.


'''
arguments and options
'''
# options come first, preceded by - or --
# example of option without arguments -v or --v
# example of option with arguments -m module 


'''
argparse
'''

# Steps 
# - create ArgumentParser 
# - define command line options and arguments. Done by adding arguments with the ArgumentParser.add_argument() method
# - parse the sys.argv command line to create a namespace object that detaisls the options, option arguments and overall command line arguments
# - use the resulting namespace object ot configure the application and process the arguments

parser = argparse.ArgumentParser( description="Simulate Blackjack" )

# Once the arguments have been defined, we can parse them and use them. Here's
# how we parse them:
config= parser.parse_args()

# default to False, sometimes can do default to None
parser.add_argument('-v', '--verbose', action='store_true', default=False)

# use action of 'store_const' with additional const= arguments. This allows us to store values beyond simple True/False
parser.add_argument('--debug', action='store_const', const=logging.DEBUG, default=logging.INFO, dest="logging_level")
# we can thne use config.logging_level without any further mapping


# an option with an argument 
# a string value must follow the action and must be from the available choices
# the destination name betting_rule will receive the option's argument string 
parser.add_argument( "-b", "--bet", action="store", default="Flat",
                choices=["Flat", "Martingale", "OneThreeTwoSix"], dest='betting_rule')

# store an integer value that follows the option, the long name stake will be the value in the options object
parser.add_argument( "-s", "--stake", action="store", default=50, type=int )

# positional arguments 
# We define positional arguments using a name with no "-" decoration. In the
# case where we have a fixed number of positional arguments, we'll add them appropriately to the parser:
parser.add_argument( "input_filename", action="store" )
parser.add_argument( "output_filename", action="store" )


'''
integrating command line options and environment variables
'''

# explicitly setting the value when defining command line options
parser.add_argument( "--samples", action="store",
                    default=int(os.environ.get("SIM_SAMPLES",100)),
                    type=int, help="Samples to generate" )

# implicitly setting the value as part of the parsing process 


# overriding configuration settings with environment variables 
# step 1: build default settings from the environment variables
# this rewrites external environment variable names into internal configuration names ("attribute_name")
import os 
env_values = [
    ("attribute_name", os.environ.get( "SOMEAPP_VARNAME", None )),
    ("another_name", os.environ.get( "SOMEAPP_OTHER", None )), 
]

# step 2: parse a hierarchy of configuration files 
# We built a list of locations, in priority order from the most important (owned by the
# user) to the least important (part of the installation.) For each file that actually exists,
# we parsed the content to create a mapping from names to values.

config_name= "someapp.yaml"
config_locations = (
    os.path.curdir,
    os.path.expanduser("~/"),
    "/etc",
    os.path.expanduser("~thisapp/"), # or thisapp.__file__,
)
candidates = ( os.path.join(dir,config_name)
            for dir in config_locations )
config_names = ( name for name in candidates if os.path.exists(name) )
files_values = [yaml.load(file) for file in config_names]

# create a ChainMap to group multiple dicts in to one. Looks up each underlying mapping successively until a key is found
defaults= ChainMap( dict( (k,v) for k,v in env_values if v is not None), *files_values )

# step 3 we can use the following code to parse the command-line arguments and update these defaults:
config= parser.parse_args( namespace=argparse.Namespace( **defaults ))
# We transformed our ChainMap of configuration file settings into an argparse. Namespace object. Then, we parsed the command-line options to update that
# namespace object. As the environment variables are first in ChainMap, they override any configuration files.


# overriding environment variables with configuration files 
# We can put env_config in defaults.maps last to make it the final fallback:
defaults= ChainMap( *files_values )
defaults.maps.append( dict( (k,v) for k,v in env_values if v is not None ) )

