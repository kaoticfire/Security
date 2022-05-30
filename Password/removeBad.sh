#!/bin/bash
# shellcheck disable=SC2063

echo "Remove non-ASCii characters"
echo ""
read -rp "Enter the starting file: " file
read -rp "Enter the ending file: " master
echo ""
echo "Removing bad characters, please wait..."
cat $file | grep -ax '.*' > "$master"
echo "Operation Completed"
