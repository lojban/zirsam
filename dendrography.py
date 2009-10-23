#!/usr/bin/python3.0
# -*- coding: utf-8 -*-
"""
Use the BNF data to assemble a parse tree


A thought:
  When there is an error parsing (and we are not strict), don't start crying! Fold that garbage into the parent node! lo nu mi tavla xfyweflkglez do cu se nelci do
  nelci
    (se)
    lo
      nu
        tavla
          mi
          ERROR(xfwerflzdf)
          do
    do
"""

import sys

from config import Configuration
from common import Buffer
import thaumatology
from bnf import BNF

REVERSE_BNF = {}
for key in BNF:
  rule = BNF[key]
  REVERSE_BNF[rule] = key

ROOT_TOKEN = "sentence" #Todo: Put this in the Configuration



class Node:
  def __init__(self):
    pass


def match_bnf(tokens, start=None):
  #Returns a list of every rule that tokens matches
  #So, what about excluding items?
  if start is None:
    start = BNF.keys()
  matches = []
  for test in start:
    if BNF[test].match(tokens):
      matches.append(test)
  return matches

class GrammarParser:
  def __init__(self, token_iter, config):
    self.valsi = token_iter
    self.config = config


  def parse_to(self, top_rule):
    """When the rule "top_rule" has been fullfilled, return the value."""

  def __iter__(self):
    """
    yield ROOT_TOKENs
    """
    valsi_index = 0
    root = BNF[self.config.parsing_unit]
    yield root.match(self.valsi)
    
    ...


def Stream(conf=None):
  if conf == None:
    conf = Configuration()
  valsibuff = thaumatology.Stream(conf)
  treebuff = GrammarParser(valsibuff, conf)
  return Buffer(treebuff, conf)

if __name__ == '__main__':
  p = Stream()
  for i in p:
    print(i)
'''
So...
we get the rule with the longest match! Okay, so then we have that 'rule'. Now we have to match 'rule'+following token.

Except that there shouldn't be a 'longest match', it should be the only match!


well, anyways. What's the easiest? What seems obvious to me, I suppose.  So, the bottom-up approach?

Well, Top-Down would make it easier to break at sentences or something...
How about this: "seperating values"
Ah! I like that! Okay, so, when we reach a ROOT_TOKEN, we don't go up any farther. So, for now, ROOT_TOKEN = "sentence"
'''


"""

Rule := Grammar Expressions /terminators/
SO, uh, how to handle the Terminators? From the EBNF?

If this token matches a terminator:
  end the rule
else:
  continue...?


"""
