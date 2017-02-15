#!/usr/bin/env bash

##############################################################################################
# SCRIPT NAME: clean_environment.sh                                                          #
#                                                                                            #
# PURPOSE: function 'clean_environment' can be used to clean the developing environment      #
#                                                                                            #
# CALL FROM COMMAND LINE: . ./clean_environment.sh && clean_environment                      #
##############################################################################################

clean_environment()
{
    printf "${YELLOW}Cleaning developing environment at '${PWD}'...${NORMAL}\n"
    find . -type f -name "*.py[co]" -delete
    find . -type d -name "__pycache__" -delete
    find . -type f -name ".coverage" -delete
    rm -rf ands.egg-info
    rm -rf venv
    printf "${GREEN}Done.${NORMAL}\n"
}

. ./_source_script.sh
_source_script scripts colors