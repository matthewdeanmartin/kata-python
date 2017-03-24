#!/usr/bin/env bash

# this will pull in changes from the original fork
git remote add upstream https://github.com/matthewdeanmartin/kata-python.git
git fetch upstream
git pull upstream master
