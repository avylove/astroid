# Licensed under the LGPL: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html
# For details: https://github.com/PyCQA/astroid/blob/main/LICENSE
# Copyright (c) https://github.com/PyCQA/astroid/blob/main/CONTRIBUTORS.txt

"""
Shim to support Python versions < 3.10 that don't have sys.stdlib_module_names

These values were created by cherry-picking the commits from
https://bugs.python.org/issue42955 into each version, but may be updated
manually if changes are needed.
"""

import sys

# TODO: Remove this file when Python 3.9 is no longer supported

# Standard library modules common to 3.7 - 3.9
_COMMON = frozenset(
    {
        "__future__",
        "_abc",
        "_ast",
        "_asyncio",
        "_bisect",
        "_blake2",
        "_bootlocale",
        "_bz2",
        "_codecs",
        "_codecs_cn",
        "_codecs_hk",
        "_codecs_iso2022",
        "_codecs_jp",
        "_codecs_kr",
        "_codecs_tw",
        "_collections",
        "_collections_abc",
        "_compat_pickle",
        "_compression",
        "_contextvars",
        "_crypt",
        "_csv",
        "_ctypes",
        "_curses",
        "_curses_panel",
        "_datetime",
        "_dbm",
        "_decimal",
        "_elementtree",
        "_functools",
        "_gdbm",
        "_hashlib",
        "_heapq",
        "_imp",
        "_io",
        "_json",
        "_locale",
        "_lsprof",
        "_lzma",
        "_markupbase",
        "_md5",
        "_msi",
        "_multibytecodec",
        "_multiprocessing",
        "_opcode",
        "_operator",
        "_osx_support",
        "_pickle",
        "_posixsubprocess",
        "_py_abc",
        "_pydecimal",
        "_pyio",
        "_queue",
        "_random",
        "_sha1",
        "_sha256",
        "_sha3",
        "_sha512",
        "_signal",
        "_sitebuiltins",
        "_socket",
        "_sqlite3",
        "_sre",
        "_ssl",
        "_stat",
        "_string",
        "_strptime",
        "_struct",
        "_symtable",
        "_thread",
        "_threading_local",
        "_tkinter",
        "_tracemalloc",
        "_uuid",
        "_warnings",
        "_weakref",
        "_weakrefset",
        "_winapi",
        "abc",
        "aifc",
        "antigravity",
        "argparse",
        "array",
        "ast",
        "asynchat",
        "asyncio",
        "asyncore",
        "atexit",
        "audioop",
        "base64",
        "bdb",
        "binascii",
        "binhex",
        "bisect",
        "builtins",
        "bz2",
        "cProfile",
        "calendar",
        "cgi",
        "cgitb",
        "chunk",
        "cmath",
        "cmd",
        "code",
        "codecs",
        "codeop",
        "collections",
        "colorsys",
        "compileall",
        "concurrent",
        "configparser",
        "contextlib",
        "contextvars",
        "copy",
        "copyreg",
        "crypt",
        "csv",
        "ctypes",
        "curses",
        "dataclasses",
        "datetime",
        "dbm",
        "decimal",
        "difflib",
        "dis",
        "distutils",
        "doctest",
        "email",
        "encodings",
        "ensurepip",
        "enum",
        "errno",
        "faulthandler",
        "fcntl",
        "filecmp",
        "fileinput",
        "fnmatch",
        "formatter",
        "fractions",
        "ftplib",
        "functools",
        "gc",
        "genericpath",
        "getopt",
        "getpass",
        "gettext",
        "glob",
        "grp",
        "gzip",
        "hashlib",
        "heapq",
        "hmac",
        "html",
        "http",
        "idlelib",
        "imaplib",
        "imghdr",
        "imp",
        "importlib",
        "inspect",
        "io",
        "ipaddress",
        "itertools",
        "json",
        "keyword",
        "lib2to3",
        "linecache",
        "locale",
        "logging",
        "lzma",
        "mailbox",
        "mailcap",
        "marshal",
        "math",
        "mimetypes",
        "mmap",
        "modulefinder",
        "msilib",
        "msvcrt",
        "multiprocessing",
        "netrc",
        "nis",
        "nntplib",
        "nt",
        "ntpath",
        "nturl2path",
        "numbers",
        "opcode",
        "operator",
        "optparse",
        "os",
        "ossaudiodev",
        "parser",
        "pathlib",
        "pdb",
        "pickle",
        "pickletools",
        "pipes",
        "pkgutil",
        "platform",
        "plistlib",
        "poplib",
        "posix",
        "posixpath",
        "pprint",
        "profile",
        "pstats",
        "pty",
        "pwd",
        "py_compile",
        "pyclbr",
        "pydoc",
        "pydoc_data",
        "pyexpat",
        "queue",
        "quopri",
        "random",
        "re",
        "readline",
        "reprlib",
        "resource",
        "rlcompleter",
        "runpy",
        "sched",
        "secrets",
        "select",
        "selectors",
        "shelve",
        "shlex",
        "shutil",
        "signal",
        "site",
        "smtpd",
        "smtplib",
        "sndhdr",
        "socket",
        "socketserver",
        "spwd",
        "sqlite3",
        "sre_compile",
        "sre_constants",
        "sre_parse",
        "ssl",
        "stat",
        "statistics",
        "string",
        "stringprep",
        "struct",
        "subprocess",
        "sunau",
        "symbol",
        "symtable",
        "sys",
        "sysconfig",
        "syslog",
        "tabnanny",
        "tarfile",
        "telnetlib",
        "tempfile",
        "termios",
        "textwrap",
        "this",
        "threading",
        "time",
        "timeit",
        "tkinter",
        "token",
        "tokenize",
        "trace",
        "traceback",
        "tracemalloc",
        "tty",
        "turtle",
        "turtledemo",
        "types",
        "typing",
        "unicodedata",
        "unittest",
        "urllib",
        "uu",
        "uuid",
        "venv",
        "warnings",
        "wave",
        "weakref",
        "webbrowser",
        "winreg",
        "winsound",
        "wsgiref",
        "xdrlib",
        "xml",
        "xmlrpc",
        "zipapp",
        "zipfile",
        "zipimport",
        "zlib",
    }
)

PY_3_7 = frozenset(
    _COMMON
    | {
        "_dummy_thread",
        "dummy_threading",
        "macpath",
    }
)

PY_3_8 = frozenset(
    _COMMON
    | {
        "_dummy_thread",
        "_posixshmem",
        "_statistics",
        "_xxsubinterpreters",
        "dummy_threading",
    }
)

PY_3_9 = frozenset(
    _COMMON
    | {
        "_aix_support",
        "_bootsubprocess",
        "_peg_parser",
        "_posixshmem",
        "_statistics",
        "_xxsubinterpreters",
        "_zoneinfo",
        "graphlib",
        "zoneinfo",
    }
)

if sys.version_info[:2] == (3, 7):
    stdlib_module_names = PY_3_7
elif sys.version_info[:2] == (3, 8):
    stdlib_module_names = PY_3_8
elif sys.version_info[:2] == (3, 9):
    stdlib_module_names = PY_3_9
else:
    stdlib_module_names = sys.stdlib_module_names  # pragma: no cover
