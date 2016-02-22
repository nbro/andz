#!/usr/bin/env python3

print("__file__ =", __file__)
print("__name__ =", __name__)
print("__package__ =", __package__)
print("-" * 40)

import b
from subpkg import a, b
