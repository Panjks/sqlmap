#!/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

# 自定义异常类 继承于Exception类

class SqlmapBaseException(Exception):
    pass

class SqlmapCompressionException(SqlmapBaseException):
    pass

class SqlmapConnectionException(SqlmapBaseException):
    pass

class SqlmapDataException(SqlmapBaseException):
    pass

class SqlmapFilePathException(SqlmapBaseException):
    pass

class SqlmapGenericException(SqlmapBaseException):
    pass

class SqlmapInstallationException(SqlmapBaseException):
    pass

class SqlmapMissingDependence(SqlmapBaseException):
    pass

class SqlmapMissingMandatoryOptionException(SqlmapBaseException):
    pass

class SqlmapMissingPrivileges(SqlmapBaseException):
    pass

class SqlmapNoneDataException(SqlmapBaseException):
    pass

class SqlmapNotVulnerableException(SqlmapBaseException):
    pass

class SqlmapSilentQuitException(SqlmapBaseException):
    pass

class SqlmapUserQuitException(SqlmapBaseException):
    pass

class SqlmapShellQuitException(SqlmapBaseException):
    pass

class SqlmapSkipTargetException(SqlmapBaseException):
    pass

class SqlmapSyntaxException(SqlmapBaseException):
    pass

class SqlmapSystemException(SqlmapBaseException):
    pass

class SqlmapThreadException(SqlmapBaseException):
    pass

class SqlmapTokenException(SqlmapBaseException):
    pass

class SqlmapUndefinedMethod(SqlmapBaseException):
    pass

class SqlmapUnsupportedDBMSException(SqlmapBaseException):
    pass

class SqlmapUnsupportedFeatureException(SqlmapBaseException):
    pass

class SqlmapValueException(SqlmapBaseException):
    pass
