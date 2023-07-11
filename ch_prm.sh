#!/bin/bash
! "
this script deletes emacs temp files,
changes python files permissions,
toggle unix and dos file formats
"

find . -type f -name "*.py" -exec chmod u+x {} \;
find . -type f -name "*~" -delete
#find . -type f -exec dos2unix {} \;
#find . -type f -exec unix2dos {} \;
