#!/usr/bin/env python
# Author: Emmanuel Odeke <odeke@ualberta.ca>
# Utilities to do some dirty work like file globing, 
# pyVersion handling etc

import os
import sys
import stat
import glob
import json
from optparse import OptionParser

getDefaultUserName = lambda : os.environ.get('USER', 'Anonymous')
pathExists = lambda p : p and os.path.exists(p)
isDir = lambda p : pathExists(p) and stat.S_ISDIR(getStatDict(p).st_mode)
isReg = lambda p : pathExists(p) and stat.S_ISREG(getStatDict(p).st_mode)

def getPathsLike(regexList, srcDir=None):
  originalPath = None
  if isDir(srcDir): # Must change current path to the target source and revert after the desired matching
    originalPath = os.path.abspath('.')
    os.chdir(srcDir)

  # Don't want to recomputation in matching paths of duplicate regexs
  _regexsAsSet = set(regexList)
  matches = dict()

  curFullPath = os.path.abspath('.')
  for regex in _regexsAsSet:
    pathMatches = glob.glob(regex) 
    # perform an abspath preprocessing
    fullPaths = map(lambda p : os.path.join(curFullPath, p), pathMatches)
    matches[regex] = list(fullPaths)
    
  if originalPath: # Revert back to original path
    os.chdir(originalPath)

  return matches

class DynaItem:
  def __init__(self, initArgs):
    __slots__ = (arg for arg in initArgs)
    for arg in initArgs:
      setattr(self, arg, initArgs[arg])

  def __iter__(self):
    return self.__dict__.__iter__()
    
  def __str__(self): 
    return self.__dict__.__str__()

  def __repr__(self):
    return self.__str__()

def cliParser():
    parser = OptionParser()
    parser.add_option('-i', '--ip', default='127.0.0.1', help='IP on which the server is accessible', dest='ip')
    parser.add_option('-p', '--port', default='8000', help='IP address db connects to', dest='port')
    parser.add_option('-s', '--secure', default=True, help='Set to False to use http instead of https', action='store_false', dest='secure')

    return parser.parse_args()

def makeDBHandler(srcUrl, objProtoType):
    chatAddr = '%s/chatServer'%(srcUrl.strip('/'))
    print('Connecting via: \033[92m', chatAddr, '\033[00m')
    return objProtoType(chatAddr)
