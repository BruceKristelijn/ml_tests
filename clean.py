from os import listdir, getcwd
from os.path import isfile, join

import csv, string, os

# Cleans all csv's to make sure they are working.
print("[Clean] Getting all files.")

# Get all files
path = getcwd() + "/workspace/src/"
files = onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# Loop over files and check files.
for file in files:
    if '{' in open(path + file, "r").read():
        os.remove(path + file)