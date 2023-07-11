#!/bin/bash
# validates the diction/syntax using pycodestyle

find . -type f -name "*.py" -exec pycodestyle {} \;
