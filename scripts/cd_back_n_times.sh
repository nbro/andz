#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: cd_back_n_times.sh                                               #
#                                                                               #
# PURPOSE: the function 'cd_back_n_times' executes "cd .." the number of times  #
# corresponding to the value of the first parameter                             #
#################################################################################

export ALREADY_SOURCED_CD_BACK_N_TIMES

if [ -z "${ALREADY_SOURCED_CD_BACK_N_TIMES}" ]
then
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

    ALREADY_SOURCED_CD_BACK_N_TIMES="true"
fi