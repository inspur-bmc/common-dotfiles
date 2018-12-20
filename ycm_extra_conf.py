import os
import os.path
import fnmatch
import logging
import ycm_core
import re

C_BASE_FLAGS = [
        '-Wall',
        '-Wextra',
        '-Werror',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-fexceptions',
        '-ferror-limit=10000',
        '-DNDEBUG',
        '-std=c11',
        ]

CPP_BASE_FLAGS = [
        '-Wall',
        '-Wextra',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-fexceptions',
        '-ferror-limit=10000',
        '-DNDEBUG',
        '-std=c++1z',
        '-xc++',
        ]

C_SOURCE_EXTENSIONS = [
        '.c'
        ]

CPP_SOURCE_EXTENSIONS = [
        '.cpp',
        '.cxx',
        '.cc',
        '.m',
        '.mm'
        ]

C_HEADER_EXTENSIONS = [
        '.h',
        '.hxx',
        '.hpp',
        '.hh'
        ]

CPP_HEADER_EXTENSIONS = [
        '.hxx',
        '.hpp',
        '.hh'
        ]

def GetOeWorkdirSysRoot():
    return '/oe-workdir/recipe-sysroot/'

def FlagsForC(root):
    flags = C_BASE_FLAGS
    return flags

def FlagsForCpp(root):
    flags = CPP_BASE_FLAGS
    flags = flags + ['-isystem' + root + GetOeWorkdirSysRoot() + '/usr/include/']
    flags = flags + ['-isystem' + root + GetOeWorkdirSysRoot() + '/usr/include/c++/7.3.0']

    return flags
          

def IsCFile(filename):
    extension = os.path.splitext(filename)[1]
    return extension in C_SOURCE_EXTENSIONS + C_HEADER_EXTENSIONS

def IsCPPFile(filename):
    extension = os.path.splitext(filename)[1]
    return extension in CPP_SOURCE_EXTENSIONS + CPP_HEADER_EXTENSIONS


def FlagsForFile(filename):
    root = os.path.split(os.path.realpath(__file__))[0]
    if IsCFile(filename):
        final_flags = FlagsForC(root)
    if IsCPPFile(filename):
        final_flags = FlagsForCpp(root)

    return {
            'flags': final_flags,
            'do_cache': True
            }
