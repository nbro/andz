#!/usr/bin/env bash

#################################################################################
# SCRIPT NAME: virtual_environment.sh                                           #
#                                                                               #
# PURPOSE: some functions useful to create, switch to, install in,              #
# and deactivate virtual environments                                           #
#################################################################################

export ALREADY_SOURCED_VIRTUAL_ENVIRONMENT

if [ -z "${ALREADY_SOURCED_VIRTUAL_ENVIRONMENT}" ]
then
    create_virtual_environment()
    {
        printf "%sCreating new virtual environment called 'venv'...%s\n" "${YELLOW}" "${NORMAL}"
        assert_python_module_installed virtualenv
        virtualenv venv
        printf "%sDone.%s\n" "${GREEN}" "${NORMAL}"
    }

    switch_to_virtual_environment()
    {
        printf "%sEntering virtual environment 'venv'...%s" "${YELLOW}" "${NORMAL}"
        . venv/bin/activate
        printf "%s done.%s\n" "${GREEN}" "${NORMAL}"
    }

    install_dependencies_in_virtual_environment()
    {
        printf "%sInstalling required dependencies...%s\n" "${YELLOW}" "${NORMAL}"
        for dependency in "$@"
        do
            # Do NOT wrap the following variable with quotes,
            # since it seems to cause problems with the argument "-e ."!!
            pip3.5 install ${dependency}
        done
        printf "%sDone.%s\n" "${GREEN}" "${NORMAL}"
    }

    exit_from_virtual_environment()
    {
        printf "%sExiting from virtual environment...%s" "${YELLOW}" "${NORMAL}"
        deactivate
        printf "%s done.%s\n" "${GREEN}" "${NORMAL}"
    }

    . ./_source_script.sh
    _source_script scripts colors
    _source_script scripts asserts

    ALREADY_SOURCED_VIRTUAL_ENVIRONMENT="true"
fi