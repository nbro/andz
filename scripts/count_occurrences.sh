#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: count_occurrences.sh                                             #
#                                                                               #
# PURPOSE: the function 'count_occurrences' counts the number of occurrences    #
# of first parameter (to the same function), which should be a character        #
# in the second parameter, which should be a string                             #
#################################################################################

count_occurrences()
{
    # First parameter should be the character.
    # Second should be the string.

    # Based on: http://stackoverflow.com/a/16679459/3924118.
    if [ "$#" -ne  "2" ]
    then
        return -1
    fi

    return $(grep -o "$1" <<< "$2" | wc -l)
}