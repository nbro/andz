# How can you contribute to this project?

You can support this project in the following ways.

1. Report a bug or suggest an improvement (after reading the source code, the documentation and/or the doc strings).
 You do this by [opening an issue](https://github.com/nbro/ands/issues/new).

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

- I'm currently using Python 3.5 (and `pip3.5`) to develop.

### Fork, clone and install `ands` in a virtual environment

1. Fork the [`ands`](https://github.com/nelson-brochado/ands) repository (from my Github's account to your own). 

2. Clone your forked repository to your local machine. 

3. Open a terminal. Let's enter inside the `ands` main folder:

        cd ands

4. Install the `ands` module in _editable_ mode in a virtual environment:

    1. Install Python's `virtualenv` module:

            pip3.5 install virtualenv


    2. Create a virtual environment named `venv`:
    
            virtualenv venv
    
    
    3. Install `ands` on the virtual environment `venv`:
    
            pip3.5 install -e .

### Develop

When writing code, please, follow and take into consideration respectively the conventions and the questions regarding these last ones specified in [CONVENTIONS.md](./CONVENTIONS.md).

When developing your new algorithm or data structure or simply fixing a bug in the existing code, I encourage you to write tests that reflect these modifications. _I don't accept pull requests without tests that reflect those changes_.

### Testing

Write your tests under the folder [`tests`](tests) (by mirroring the file system's layout under the `ands` subfolder).

#### Run tests automatically

The script [`./run_tests.sh`](./scripts/run_tests.sh) was created to automate the tasks of 

1. creating a virtual environment for testing, 
2. installing required dependencies to run the tests, 
3. running the tests, and 
4. reporting its results, which includes reporting code coverage. 

You can make the script run all tests or just the tests in a specific file.

The following commands are assumed to be executed from inside the `scripts` folder.

##### Run all tests

If you want to run all tests, which I encourage you to do before pushing your changes to your remote repository (to avoid pushing broken code), do

    ./run_tests.sh
    
This command may take some time.

##### Run tests inside one file

If you want to run just the tests inside a file, the general syntax is as follows 

    ./run_tests.sh -st <relative_folder_path_inside_folder_tests> <test_name.py>

For example, if you want to run the tests under [`tests/ds/test_DisjointSetsForest.py`](./tests/ds/test_DisjointSetsForest.py), execute

    ./run_tests.sh -st ds test_DisjointSetsForest.py
    
where `<relative_folder_path_inside_folder_tests>` in this case is `ds` and `<test_name.py>` is `test_DisjointSetsForest.py`.

#### Run tests manually (discouraged)

From inside the folder containing the file with the tests, you can do

    python -m unittest discover . -v

If you install the package `coveralls` (with `pip3.5`), you can also run tests and see the code coverage afterwards. Run the tests as follows

    coverage run -m unittest discover . -v

Then, to see the code coverage, run

    coverage report

### Commit, push and create a pull request
        
3. Once you finish developing, you need to 

    1. commit your changes to your local repository, 

    2. push your local changes (as per the last commit) to your remote (forked) repository, and then 

    3. create a pull request