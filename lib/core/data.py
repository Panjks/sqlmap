#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.datatype import AttribDict
from lib.core.log import LOGGER

# sqlmap paths sqlmap文件路径字典
paths = AttribDict()

# object to store original command line options
# 命令行选项字典
cmdLineOptions = AttribDict()

# object to store merged options (command line, configuration file and default options)
mergedOptions = AttribDict()

# object to share within function and classes command
# line options and settings
# sqlmap配置文件的字典对象
conf = AttribDict()

# object to share within function and classes results
# 存储函数和类结果的字典对象
kb = AttribDict()

# object with each database management system specific queries
queries = {}

# logger
logger = LOGGER
