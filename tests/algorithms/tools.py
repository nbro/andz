#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main(g, exporter, script_name):
    import os
    import traceback
    from tabulate import tabulate
    
    print("__file__ =", os.path.abspath(script_name))
    
    function = type(lambda: None)
    c = 0
    tests_names = []

    # Identifying tests
    for name, obj in g.items():
        if (isinstance(obj, function) and
            obj.__module__ == exporter and
            name.startswith("test_")):
            c += 1
            tests_names.append(name)

    # Running tests
    finished = 0
    tests_passed = []
    tests_failed = []
    
    for i, test_name in enumerate(tests_names):
        try:
            g[test_name]()
            print(test_name, "finished.")
            finished += 1
            tests_passed.append([i + 1, test_name])
        except AssertionError as e:
            traceback.print_exc()
            break

    # Result of tests
    failed = 1
    for test_name in tests_names:
        found = False
        for p in tests_passed:
            if p[1] == test_name:
                found = True
                break
        if not found:
            tests_failed.append([failed, test_name])
            failed +=1

    # Printing results
    print(tabulate(tests_passed, headers=["#", "Tests Passed".upper()], tablefmt="fancy_grid"))
    print("# of tests passed:", finished)
    print(tabulate(tests_failed, headers=["#", "Tests failed".upper()], tablefmt="fancy_grid"))
    print("# of tests failed:", c - finished)
