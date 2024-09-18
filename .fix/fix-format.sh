#!/usr/bin/env bash

# Since files were created in windows, file format is not in 
# unix format, that's why it requires to be formatted in unix
# format so the linux terminal will read the shebangs properly
#  and won't have any other errors anymore.

find . -type f -print0 | xargs -0 dos2unix
