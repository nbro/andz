#!/usr/bin/env bash


# Colors used when printing.
GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
NORMAL=$(tput sgr0)
YELLOW=$(tput setaf 3)

new_docs()
{
    printf "\n${YELLOW}Creating new documentation under './docs'...${NORMAL}\n"
    rm -rf ./docs
    mkdir docs
    pdoc --html --overwrite --html-dir docs ands
    printf "${GREEN}Done.${NORMAL}\n\n"
}