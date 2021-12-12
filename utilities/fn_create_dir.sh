#!/usr/bin/env bash

# Variables
PERSON_LIST='solutions'
UTILITY_PATH=/Users/scheuck/Desktop/DoNotBackup/advent-of-code-2021/utilities

# Creates the .gitignore and README.md

create_header_file() {
    echo "# 's advent of code" >> README.md
    echo 'Placeholder text' >> README.md
    cat $UTILITY_PATH/example_text >> README.md
    echo '# .gitignore to be filled up' >> .gitignore
}

# Creates the advent-of-code day folders in the sub-folder of the individual person

create_day_dirs() {
    create_header_file $1
    for j in {1..25} 
    do
        if (( $j < 10 )); then
            DAY_VAR='Day-0'$j
        else
            DAY_VAR='Day-'$j
        fi
        mkdir $DAY_VAR
        echo '# Placeholder' >> $DAY_VAR/.gitignore
    done
}

# Create a folder for every person in the list

create_person_dir() {
    # If in '/utilities' then 'cd ..' leads to the right directory for the folders
    cd ..
    for i in "$@"
    do
        mkdir $i; cd $i
        create_day_dirs $i; cd ..
    done
}

create_person_dir $PERSON_LIST
