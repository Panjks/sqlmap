#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import copy
import types

class AttribDict(dict):
    """
    This class defines the sqlmap object, inheriting from Python data
    type dictionary.
    继承自python的字典数据结构，定义了sqlmap的对象
    很简单但经典，可以像访问属性一样访问dict中的键值对
    >>> foo = AttribDict()
    >>> foo.bar = 1
    >>> foo.bar
    1
    """

    def __init__(self, indict=None, attribute=None):
        if indict is None:
            indict = {}
        # 初始化字典
        # Set any attributes here - before initialisation # 在初始化之前设置属性
        # these remain as normal attributes
        self.attribute = attribute
        dict.__init__(self, indict)
        self.__initialised = True

        # After initialisation, setting attributes
        # is the same as setting an item

    def __getattr__(self, item):
        """

        Maps values to attributes
        Only called if there *is NOT* an attribute with this name
        动态返回一个属性的值。动态创建对象
        重写了__getattr__方法 实现 值->属性的映射 只有在名字不是个属性时调用
        """

        try:
            return self.__getitem__(item)
        # """ x.__getitem__(y) <==> x[y] """
        # 当键值错误时
        except KeyError:
            raise AttributeError("unable to access item '%s'" % item)

    def __setattr__(self, item, value):
        """
        Maps attributes to values
        Only if we are initialised
        实现属性->值的映射
        初始化后执行
        """

        # This test allows attributes to be set in the __init__ method
        # 如果没有初始化过，以父类dict的类型添加
        if "_AttribDict__initialised" not in self.__dict__:
            return dict.__setattr__(self, item, value)

        # Any normal attributes are handled normally
        # __dict__ 用于存放对象及对象值的键值对
        # 当已经有item对象时
        elif item in self.__dict__:
            dict.__setattr__(self, item, value)
        # 当没有item对象时
        else:
            self.__setitem__(item, value)

    # __getstate__和__setstate__方法不是很理解 大概是更好pickle序列化？
    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, dict):
        self.__dict__ = dict

    def __deepcopy__(self, memo):
        # 不懂什么用
        retVal = self.__class__()
        memo[id(self)] = retVal

        for attr in dir(self):
            if not attr.startswith('_'):
                value = getattr(self, attr)
                if not isinstance(value, (types.BuiltinFunctionType, types.FunctionType, types.MethodType)):
                    setattr(retVal, attr, copy.deepcopy(value, memo))

        for key, value in self.items():
            retVal.__setitem__(key, copy.deepcopy(value, memo))

        return retVal

class InjectionDict(AttribDict):
    def __init__(self):
        AttribDict.__init__(self)

        self.place = None
        self.parameter = None
        self.ptype = None
        self.prefix = None
        self.suffix = None
        self.clause = None
        self.notes = []  # Note: https://github.com/sqlmapproject/sqlmap/issues/1888

        # data is a dict with various stype, each which is a dict with
        # all the information specific for that stype
        self.data = AttribDict()

        # conf is a dict which stores current snapshot of important
        # options used during detection
        self.conf = AttribDict()

        self.dbms = None
        self.dbms_version = None
        self.os = None
