#!/usr/bin/env bash

##############################################################################################
# SCRIPT NAME: new_docs.sh                                                                   #
#                                                                                            #
# PURPOSE: create new documentation for the 'ands' module using the Python's 'pdoc' module   #
#                                                                                            #
# RUN FROM COMMAND LINE:  . ./new_docs.sh && new_docs                                        #
##############################################################################################

export ALREADY_SOURCED_NEW_DOCS

if [ -z "${ALREADY_SOURCED_NEW_DOCS}" ]
then
    new_docs()
    {
        printf "%sCreating new documentation under '%s/docs'...%s\n" "${YELLOW}" "${PWD}" "${NORMAL}"
        rm -rf ./docs
        mkdir docs
        pdoc --html --overwrite --html-dir docs ands
        printf "%sDone.%s\n" "${GREEN}" "${NORMAL}"
    }

    . ./_source_script.sh
    _source_script scripts colors

    ALREADY_SOURCED_NEW_DOCS="true"
fi