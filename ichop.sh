#!/bin/bash

IFS=$'\n'

# Default values
c_value="40"
files=()

# Usage function
usage() {
    echo "Usage: $0 [-c|--chop <value>] <file1> <file2> ... <fileN>"
    echo "Chop the images from the location specified in x axis"
    echo
    echo "Options:"
    echo "  -c, --chop     default 40%"
    echo "  <file1> <file2> ... <fileN>  Specify one or more files"
    exit 1
}

# Parse command-line options
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -c|--chop)
            c_value="$2"
            shift 2
            ;;
        *)
            files+=("$1")
            shift
            ;;
    esac
done
# Check if mandatory argument is provided
if [[ ${#files[@]} -eq 0 ]]; then
    usage
fi

echo "Selected File(s) ..."
#for file in "${files[@]}"; do
#    echo -e "\t$file"
#done
for ((i=0; i<${#files[@]}; i++)); do
    printf  "  %2d) %s\n" $((i+1)) ${files[i]}
done

# Rest of the script...
r_value=$((100-c_value))

for i in `ls ${files[@]}`; do 
    echo  "Chopping file $i ..."
    convert "$i" -gravity West -chop $c_value%x0 "${i/.png/-right.png}"
    convert "$i" -gravity East -chop $r_value%x0 "${i/.png/-left.png}"    
done 
