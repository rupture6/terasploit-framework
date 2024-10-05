#!/usr/bin/env python3

import sys; sys.dont_write_bytecode = True
import os

directory_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(directory_path, os.pardir)))


# Used for advance importing and dependencies checking.

from libs.terasploit.framework.module.dependencies import *