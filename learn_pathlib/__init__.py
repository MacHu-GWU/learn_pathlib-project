#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

__version__ = "0.0.1"
__short_description__ = "Learn pathlib pythonic way."
__license__ = "MIT"

from pathlib import Path

p_file = Path(__file__) # /learn_pathlib/__init__.py
p_dir = p_file.parent # /learn_pathlib