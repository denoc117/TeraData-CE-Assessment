#!/bin/bash

du -sh /* > dir_space.txt

df -h > fs_space.txt

while read line
do
    percentage=$(echo $line | awk '{print $1}' | tr -d '%')
    if [ $percentage -gt 80 ]; then
        echo "Adding a new disk..."
        directory=$(echo $line | awk '{print $2}')
        echo "Mounting $directory..."
    fi
done < dir_space.txt

while read line
do
    percentage=$(echo $line | awk '{print $5}' | tr -d '%')
    if [ $percentage -gt 80 ]; then
        echo "Adding a new disk..."
        filesystem=$(echo $line | awk '{print $1}')
        echo "Mounting $filesystem..."
    fi
done < fs_space.txt

rm dir_space.txt
rm fs_space.txt
