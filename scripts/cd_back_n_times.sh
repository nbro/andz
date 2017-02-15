#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: cd_back_n_times.sh                                               #
#                                                                               #
# PURPOSE: the function 'cd_back_n_times' executes "cd .." the number of times  #
# corresponding to the value of the first parameter                             #
#################################################################################

cd_back_n_times()
{
    if [ "$#" -ne  "1" ]
    then
        return 1
    fi

    for (( i = 0; i < $1; i++ ))
    do
        cd ..
    done
}