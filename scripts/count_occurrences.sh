#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: count_occurrences.sh                                             #
#                                                                               #
# PURPOSE: the function 'count_occurrences' counts the number of occurrences    #
# of first parameter (to the same function), which should be a character        #
# in the second parameter, which should be a string                             #
#################################################################################

export ALREADY_SOURCED_COUNT_OCCURRENCES

if [ -z "${ALREADY_SOURCED_COUNT_OCCURRENCES}" ]
then
    count_occurrences()
    {
        # First parameter should be the character.
        # Second should be the string.

        # Based on: http://stackoverflow.com/a/16679459/3924118.
        if [ "$#" -ne  "2" ]
        then
            echo -1
        fi

        echo "$(grep -o "$1" <<< "$2" | wc -l)"
    }

    ALREADY_SOURCED_COUNT_OCCURRENCES="true"
fi