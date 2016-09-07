#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from datetime import datetime
from learn_pathlib import Path, p_file, p_dir


def path_parts():
    """get, absolute path, dir path, dirname, basename, fname, extension.
    """
    # absolute path
    assert p_file.__str__().endswith(os.path.join("learn_pathlib", "__init__.py"))
    
    # dir path
    assert p_file.parent.__str__().endswith("learn_pathlib")
    
    # dirname
    assert p_file.parent.name == "learn_pathlib"
    
    # basename
    assert p_file.name == "__init__.py"
    
    # fname
    assert p_file.stem == "__init__"
    
    # extension, if any
    assert p_file.suffix == ".py"
    
    
if __name__ == "__main__":
    #
    path_parts()


def stat():
    """get Modify Time, Access Time, Create Time, Size。
    """
    stat_result = p_file.stat()

    dt = datetime(2016, 9, 1)
    assert datetime.fromtimestamp(stat_result.st_mtime) >= dt # Moidfy Time
    assert datetime.fromtimestamp(stat_result.st_atime) >= dt # Access Time
    assert datetime.fromtimestamp(stat_result.st_ctime) >= dt # Create Time
    assert stat_result.st_size >= 283 # File Size

    
if __name__ == "__main__":
    #
    stat()
    
    

#--- Dir ---
def dir_stat():
    """对于dir来说, stat() 方法的功能我还未知。
    """
    total_size = 0
    for p in p_dir.glob("**/*"):
        total_size += p.stat().st_size
    
    assert total_size != p_dir.stat().st_size
    
    
if __name__ == "__main__":
    #
    dir_stat()