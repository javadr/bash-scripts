#!/bin/bash

export PATH=~/.local/bin/myscripts:$PATH

# Open a terminal and run commands on the selected files
gnome-terminal -- bash -c "
source ~/.bashrc;
echo 'cleansing auxilaries files';
mclean ;
echo 'Done!';
sleep 1;
exit" &
