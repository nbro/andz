#!/usr/bin/env bash

##############################################################################################
# SCRIPT NAME: new_docs.sh                                                                   #
#                                                                                            #
# PURPOSE: create new documentation for the 'ands' module using the Python's 'pdoc' module   #
#                                                                                            #
# RUN FROM COMMAND LINE:  . ./new_docs.sh && new_docs                                        #
##############################################################################################

new_docs()
{
    printf "${YELLOW}Creating new documentation under '${PWD}/docs'...${NORMAL}\n"
    rm -rf ./docs
    mkdir docs
    pdoc --html --overwrite --html-dir docs ands
    printf "${GREEN}Done.${NORMAL}\n"
}

. ./_source_script.sh
_source_script scripts colors
