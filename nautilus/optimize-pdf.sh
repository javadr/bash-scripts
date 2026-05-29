#!/bin/bash

export PATH="$HOME/.local/bin/myscripts:$PATH"

# Open a terminal and run commands on the selected files
gnome-terminal -- bash -c "
source ~/.bashrc
echo 'Processing files...'
optpdf \"$@\"
echo 'Done!'
sleep 2
" -- "$@"
