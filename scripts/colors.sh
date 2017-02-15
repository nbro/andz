#!/usr/bin/env bash

export ALREADY_SOURCED_COLORS

if [ -z "${ALREADY_SOURCED_COLORS}" ]
then
    # Colors used when printing.
    export NORMAL
    NORMAL=$(tput sgr0)

    export RED
    RED=$(tput setaf 1)

    export GREEN
    GREEN=$(tput setaf 2)

    export YELLOW
    YELLOW=$(tput setaf 3)

    ALREADY_SOURCED_COLORS="true"
fi