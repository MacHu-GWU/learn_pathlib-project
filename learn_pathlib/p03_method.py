#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pathlib import Path
import pathlib
import os


p_file = Path(__file__)
p_dir = p_file.parent

def is_exist():
    assert p_file.exists() is True
    assert p_dir.exists() is True
    
    p = Path("file_not_exist.py")
    assert p.exists() is False


def is_dir():
    assert p_file.is_dir() is False
    assert p_dir.is_dir() is True


def is_file():
    assert p_file.is_file() is True
    assert p_dir.is_file() is False
    

def iterdir():
    """
    
    **中文文档**
    
    遍历目录下的子目录和子文件。**不会包含子目录下的文件**。
    """
    assert len(list(p_dir.iterdir())) == len(os.listdir(p_dir.__str__()))
    

def glob():
    """
    
    **中文文档**
    
    返回某个目录下所有匹配某种模式的文件。
    """
#     print(sorted(p_dir.glob("*.py"))) # 按照文件名排序
    
#     print(list(Path(".").glob("*.py"))) # 默认输出顺序未知
    
    
    # 所有当前文件夹下的文件或文件夹, non-recursively
    for p in p_dir.glob("*"):
        if p.parent.name != "learn_pathlib":
            raise Exception("Not a non-recursive iterate.")
        
    # 所有当前文件夹下的文件或文件夹, recursively
    recursive_flag = False
    for p in p_dir.glob("**/*"):
        if p.parent.name != "learn_pathlib":
            recursive_flag = True
    if recursive_flag is False:
        raise Exception("Not a recursive iterate.")
    
    # suoy
    
    for p in p_dir.glob("**/"):
        print(p)

if __name__ == "__main__":
    is_exist()
    is_dir()
    is_file()
    iterdir()
    glob()