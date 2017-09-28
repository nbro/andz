#!/usr/bin/env bash

export ALREADY_SOURCED__SOURCE_SCRIPT

if [ -z "${ALREADY_SOURCED__SOURCE_SCRIPT}" ]
then

    # Tries to source the scripts whose names are passed as parameters.
    _source_script()
    {
        # Define a few colors for the possible error messages below.
        RED=$(tput setaf 1)
        NORMAL=$(tput sgr0)

        EXPECTED_DIR="scripts"

        if [ "$#" -ge  "1" ]
        then
            EXPECTED_DIR=$1
        fi

        CURRENT_DIR=${PWD##*/}

        if [ "$CURRENT_DIR" = "$EXPECTED_DIR" ]
        then
            for (( arg = 2; arg <= $#; arg++ ))
            do
                # Try to load script ${!arg}.sh
                # shellcheck source=/dev/null
                . ./${!arg}.sh

                # If it was not loaded successfully, exit with status 1.
                if [ $? -ne 0 ]
                then
                    printf "%sScript '${!arg}.sh' not loaded successfully. Exiting...%s\n" "${RED}" "${NORMAL}"
                    exit 1
                fi
            done
        else
            printf "No script loaded: %s != %s.\n" "$CURRENT_DIR" "$EXPECTED_DIR"
            exit 1
        fi
    }

    ALREADY_SOURCED__SOURCE_SCRIPT="true"
fi