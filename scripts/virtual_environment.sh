#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: virtual_environment.sh                                           #
#                                                                               #
# PURPOSE: some functions useful to create, switch to, install in,              #
# and deactivate virtual environments                                           #
#################################################################################

create_virtual_environment()
{
    printf "${YELLOW}Creating new virtual environment called 'venv'...${NORMAL}\n"
    assert_python_module_installed virtualenv
    virtualenv venv
    printf "${GREEN}Done.${NORMAL}\n\n"
}

switch_to_virtual_environment()
{
    printf "${YELLOW}Entering virtual environment 'venv'...${NORMAL}\n"
    source venv/bin/activate
    printf "${GREEN}Done.${NORMAL}\n\n"
}

install_dependencies_in_virtual_environment()
{
    printf "${YELLOW}Installing required dependencies...${NORMAL}\n"
    for dependency in "$@"
    do
        pip3.5 install ${dependency}
    done
    printf "${GREEN}Done.${NORMAL}\n\n"
}

exit_from_virtual_environment()
{
    printf "${YELLOW}Exiting from virtual environment...${NORMAL}\n"
    deactivate
    printf "${GREEN}Done.${NORMAL}\n\n"
}

. ./_source_script.sh
_source_script scripts colors
_source_script scripts asserts