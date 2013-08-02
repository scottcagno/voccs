#!/bin/bash

# ENSURE THERE IS A VOCCS_PATH ALIAS
if [[ -ne `alias VOCCS_PATH 2>/dev/null >/dev/null && echo 1` ]]
    echo "alias VOCCS_PATH='$PWD'"; 
fi

# MAKE A SYMBOLIC LINK TO RUN FILE 
ls -s $PWD/run.sh /usr/bin/voccs

# CHANGE INSTALLER TO INSTALLED
mv installer.sh installed.sh
