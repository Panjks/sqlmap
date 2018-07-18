#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import codecs
import httplib

from lib.core.settings import IS_WIN

def dirtyPatches():
    """
    Place for "dirty" Python related patches
    """
    # 糟糕的代码相关补丁的存放区域
    # accept overly long result lines (e.g. SQLi results in HTTP header responses)
    # 处理过长的http报文
    httplib._MAXLINE = 1 * 1024 * 1024

    # add support for inet_pton() on Windows OS
    if IS_WIN:
        from thirdparty.wininetpton import win_inet_pton

    # Reference: https://github.com/nodejs/node/issues/12786#issuecomment-298652440
    # 编码问题的解决
    codecs.register(lambda name: codecs.lookup("utf-8") if name == "cp65001" else None)
