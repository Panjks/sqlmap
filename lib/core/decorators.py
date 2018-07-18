#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import hashlib

from lib.core.threads import getCurrentThreadData

def cachedmethod(f, cache={}):
    """
    Method with a cached content
    # 缓冲内容方法 避免多次执行完全相同的命令
    Reference: http://code.activestate.com/recipes/325205-cache-decorator-in-python-24/
    """
    # 临时方法 修饰方法的传参
    def _(*args, **kwargs):
        # 将f args kwargs 字符串化后用|分割后md5加密 hexdigest()以16位形式返回 并限制长度
        key = int(hashlib.md5("|".join(str(_) for _ in (f, args, kwargs))).hexdigest(), 16) & 0x7fffffffffffffff
        # 如果cache字典中没有这个标记过的唯一的key 则添加并运行f
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        # 如果有，则直接返回
        return cache[key]

    # 返回方法
    return _

def stackedmethod(f):
    def _(*args, **kwargs):
        threadData = getCurrentThreadData()
        originalLevel = len(threadData.valueStack)

        try:
            result = f(*args, **kwargs)
        finally:
            if len(threadData.valueStack) > originalLevel:
                threadData.valueStack = threadData.valueStack[:originalLevel]

        return result

    return _
