#!/bin/bash

export PATH=~/.local/bin/myscripts:$PATH

# Open a terminal and run commands on the selected files
gnome-terminal -- bash -c "
source ~/.bashrc;
echo 'Processing files...';
optpdf -r .;
echo 'Done!';
exec bash" # keep the shell open
