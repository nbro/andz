# How can you contribute to this project?

You can support this project in the following ways.

1. Report a bug or suggest an improvement (after reading the source code, the documentation and/or the doc strings).You do this by [opening an issue](https://github.com/nbro/ands/issues/new).

2. Directly fix the problem/bug you spotted or introduce new algorithms and data structures. Clearly, in this case you write the code yourself.
 

## Open an issue

The _issue tracker_ should be used to report 

- issues regarding existing code, or 
- possible improvements of existing code

The _issue tracker_ should **not** be used to report:

- possible future features (which have nothing to do with the existing code), or 
- report issues of code that is no more part of this project

 
## Fix the problem directly

### Notes

- Below you find my recommended methodology for you to adopt when you're willing to fix a problem directly.

- This description and commands are for unix-like systems (but similar commands may be used for other systems).

- I'm currently using **Python 3.9** to develop.

### Fork, clone and install `ands` in a virtual environment

1. Fork the [`ands`](https://github.com/nelson-brochado/ands) repository (from my Github's account to your own). 

2. Clone your forked repository to your local machine. 

3. Open a terminal. Let's enter inside the `ands` main folder:

        cd ands

4. Install the `ands` module in _editable_ mode in a virtual environment:

    1. Install Python's `virtualenv` module (if you are using e.g. PyCharm, you might not need to do this manually, but you can create the virtual environment, even in Conda, directly from PyCharm):

            pip install virtualenv
    
    2. Create a virtual environment named `venv`:
    
            virtualenv venv
    
    3. Install `ands` on the virtual environment `venv` (note that this command should be executed from the root folder of the project that contains the file [`setup.py`](../setup.py)):
    
            pip install -e .

### Develop

When writing code, please, follow and take into consideration respectively the conventions and the questions regarding these last ones specified in [CONVENTIONS.md](CONVENTIONS.md).

When developing your new algorithm or data structure or simply fixing a bug in the existing code, you should write unit tests that reflect these modifications. No pull request is accepted if unit tests for those changes are not provided.

### Testing

Write your tests under the folder [`tests`](../tests) (by mirroring the file system's layout under the `ands` subfolder).

#### Run tests manually 

To test _all_ algorithms and data structures,

1. install the package `coveralls` in order to see also the code coverage: `pip install coveralls`
2. from the root of this project, execute the command: `coverage run --source=. -m unittest discover -s tests/ -v`

If you only want to test specific algorithms, for example, if you want to execute only the tests in `tests/algorithms/sorting`, you can run the following command

    coverage run --source=. -m unittest discover -s tests/algorithms/sorting -v

Then, to see the code coverage, run (from inside the folder that contains the `.coverage` file)

    coverage report

### Commit, push and create a pull request
        
3. Once you finish developing, you need to 

    1. commit your changes to your local repository, 

    2. push your local changes (as per the last commit) to your remote (forked) repository, and then 

    3. create a pull request