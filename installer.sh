#!/bin/bash

# PROMPT USER
echo ">> This installer will require you to authenticate..."
sudo clear

# ENSURE THERE IS A VOCCS_PATH ALIAS
if [[ `alias voccs_path 2>/dev/null >/dev/null && echo 1` ]]; then
    echo ">> An alias already exists in your .bashrc called 'voccs_path'..."
    echo ">> Not creating a new alias..."
else
    echo ">> Adding an alias to your .bashrc called 'voccs_path'..."
    echo "alias 'voccs_path'='$PWD'" >> $HOME/.bashrc 
fi

# MAKE A SYMBOLIC LINK TO RUN FILE 
if [[ -z /usr/bin/voccs ]]; then
    echo ">> 'A symbolic link, '/usr/bin/voccs', already exists..." 
    echo ">> Not creating a new symbolic link..."
else
    echo ">> Creating a symbolic link, '/usr/bin/voccs'..."
    sudo ln -s $PWD/run.sh /usr/bin/voccs
fi
