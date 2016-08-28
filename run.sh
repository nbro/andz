#!/usr/bin/env bash


run() {

# Cleans a little bit everything, including previously created virtual environments
./clean.sh
printf "./clean.sh TERMINATED EXECUTING.\n\n"


# Format the code under ./ands/ and ./tests/
printf "FORMATTING CODE UNDER './ands' AND './tests' AGGRESSIVELY AND RECURSIVELY...\n"
autopep8 --in-place --aggressive --recursive --max-line-length 110 ./ands
autopep8 --in-place --aggressive --recursive --max-line-length 110 ./tests
printf "DONE.\n\n"


# Creates and switches to the new virtual environment
printf "CREATING NEW VIRTUAL ENVIRONMENT...\n"
virtualenv venv
printf "DONE.\n\n"

source venv/bin/activate
printf "USING THE NEWLY CREATED VIRTUAL ENVIRONMENT...\n\n"

printf "INSTALLING REQUIRED DEPENDENCIES...\n"
pip install coveralls
pip install -e .
printf "DONE.\n\n"


# To deactivate the virtual environment, just type:
# deactivate
printf "EXECUTING TESTS UNDER './tests/'...\n"

cd tests
coverage run -m unittest discover . -v

cd ..
cp tests/.coverage ./.coverage
coverage report

# Creating new documentation
printf "\nCREATING NEW DOCUMENTATION UNDER './docs'...\n"
rm -rf ./docs
mkdir docs
pdoc --html --overwrite --html-dir docs ands
printf "DONE.\n\n"

deactivate

printf "DONE.\n\n"

./clean.sh
printf "./clean.sh TERMINATED EXECUTING.\n"

}

run