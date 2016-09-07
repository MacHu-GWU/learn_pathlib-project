#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from learn_pathlib import Path, p_file, p_dir


def get_current_file():
    p = Path(__file__)
    assert p.name == "p01_basic.py"
        
    
if __name__ == "__main__":
    #
    get_current_file()


def get_current_dir():
    p = Path(".").absolute() # Current Directory
    assert p.name == "learn_pathlib"
    
    p = Path.cwd().absolute() # Current Directory
    assert p.name == "learn_pathlib"
    
    
if __name__ == "__main__":
    #
    get_current_dir()
    
    
def get_parent_dir():
    p = Path(".").absolute().parent
    assert p.name == "learn_pathlib-project"
    
    
if __name__ == "__main__":
    #
    get_parent_dir()
    

def initiate_path_by_parts():
    """
    
    **中文文档**
    
    Path支持将路径的多个部分组合起来的初始化模式。
    """
    p = Path(__file__)
    p_parent = p.parent
    p_basename = p.name
    
    assert isinstance(p_dirname, Path) # Path
    assert not isinstance(p_basename, Path) # str
    
    assert Path(p_parent, p_basename).__str__() == __file__
    
    
if __name__ == "__main__":
    #
    initiate_path_by_parts()