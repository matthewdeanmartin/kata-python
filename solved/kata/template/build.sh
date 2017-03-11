#!/usr/bin/env bash
MODULE=blanks.template
CODE_PATH=blanks
cd ..
cd ..
pwd
python -m compileall $CODE_PATH
COMPILE=$?

python -m unittest blanks.template.tests
TESTS=$?

if [[ $TESTS -ne 0 || $COMPILE -ne 0 ]]; then
    echo Failed && exit
fi
