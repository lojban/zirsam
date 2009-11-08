# -*- coding: utf-8 -*-

"""
Which is the REAL zirsam.py file? Perhaps I'll just make a seperate file to handle it

"""

import sys

import common
import alphabets



def format_arg(w):
  return '--'+w.strip().replace(' ', '-')


class Configuration:
  __help_header = """The Purple Parser, by purpleposeidon

Jbobau to parse is read from standard input. Parsed text is sent to stdout, errors and messages are sent to stderr.
If an error prevents the text from being fully parsed, a non-zero value is returned.

Arguments:"""
  __help = {'help':"Shows this message", \
  'quiet':"Don't print warnings", \
  'err2out':"Write what would normally go to stderr to stdout", \
  'no readline':"Don't use GNU Readline for input", \
  
  'alphabet':"Select alphabet. --alphabet=? lists available values. The default is 'latin'", \
  
  'no dotside':"Don't require a pause following cmene-markers (XXX CHECKME)", \
  'forbid warn':"Treat warnings as errors", \
  'strict':"Count warnings as errors", \
  'no zoi filter':"Don't use the chosen alphabet to convert the contents of the zoi. Latin deliminators must be used.", \
  
  'debug':"(DEBUG OPTION) Print information from parsing", \
  'token error':"(DEBUG OPTION) Raise an Exception when the first token is made, which prints a backtrace", \
  'hate token':"(DEBUG OPTION) Raise an exception when that text is encountered", \
  'do exit':"(DEBUG OPTION) Exit without parsing", \
  'print tokens':"(DEBUG OPTION) Print out a tokens as they are created", \
  
  'no space':"(NOT IMPLEMENTED) Convert input to not use spaces", \
  
  }
  __help_order = 'help, quiet, err2out, no readline, alphabet, no zoi filter, no dotside, forbid warn, strict, debug, token error, hate token, do exit, print tokens, no space'.split(', ') #Help, Parsing configuration, Debug, unimplemented
  for val in __help:
    if val not in __help_order:
      raise Exception("Command option %r is not present in Configuration.__help_order"%val)
  def __check_options(self, argv):
    argv = list(argv) #Use a copy
    possible_args = list(Configuration.__help.keys())

    def valued_arg(name, val_dict=None):
      if name not in Configuration.__help:
        raise Exception("No help defined for argument {0!r}".format(name))
      index = 0
      r = None
      possible_args.pop(possible_args.index(name))
      for arg in argv:
        if arg.find(format_arg(name)+'=') == 0:
          val = arg[len(name)+3:].strip()
          argv.pop(index)
          if not val_dict:
            if val == '?' or val == '':
              raise SystemExit("{1}\n{0} accepts most any string.".format(name, Configuration.__help[name]))
            return val
          if val in val_dict:
            r = val
          elif val == '?' or val == '':
            r = 'Usage for --{0}=VALUE\n  Possible values for {0} are:\n'.format(name)
            for v in val_dict:
              r += '\t{0}\n'.format(v)
            raise SystemExit(r)
          else:
            raise Exception("{0} is an invalid value for --{1}".format(repr(val), name))
        elif arg.find('--'+name) == 0:
          r = 'Usage for --{0}=VALUE\n  Possible values for {0} are:\n'.format(name)
          for v in val_dict:
            r += '\t{0}\n'.format(v)
          raise SystemExit(r)
        index += 1
      if r:
        return val_dict[r]

    def arg(what):
      #Returns True if the argument is present. Must be called exactly once.
      #XXX A thought: Make this function do all the work with __setattr__ and such
      if what not in Configuration.__help:
        raise Exception("No help given for argument {0}".format(what))
      while what in possible_args:
        possible_args.pop(possible_args.index(what))
      what = format_arg(what)
      
      
      while what in argv:
        argv.pop(argv.index(what))
        return True
      
    if arg('help'):
      print(Configuration.__help_header, file=self.stderr)
      #for cmd in Configuration.__help:
      for cmd in Configuration.__help_order:
        print("    {0}:\n\t{1}".format(format_arg(cmd), Configuration.__help[cmd]), file=self.stderr)
      self.do_exit = True
    if arg('strict'):
      self._strict = True
      self.forbid_warn = True
      self.ascii_only = True
    if arg("quiet"):
      self._quiet = True
    if arg("debug"):
      self._debug = True
      self.print_tokens = True
    if arg("print tokens"): #Print tokens as they are parsed
      self.print_tokens = True
    if arg("token error"): #Error on first token
      self.token_error = True
    if arg("no dotside"):
      self.dotside = False
    if arg("do exit"):
      self.do_exit = True
    if arg("forbid warn"):
      self.forbid_warn = True
    if arg("err2out"):
      self.stderr = self.stdout # XXX Make this Configuration's output
    if arg("no space"):
      self.output_no_space = True
    if arg("no readline"):
      self.permit_readline = False
    if arg("no zoi filter"):
      self.filter_zoi = False
    _ = valued_arg("alphabet", alphabets.GlyphTable.tables)
    if _: self.glyph_table = _
    _ = valued_arg("hate token")
    if _: self.hate_token = _
    if possible_args:
      print("The following arguments have documentation, but no implementation:", file=self.stderr)
      for p in possible_args:
        print('\t', format_arg(p), file=self.stderr)
    
    self.debug("\n\nCurrent settings:\n{0}".format(self))
    
    if argv:
      self.message("Could not handle these arguments:")
      for a in argv:
        self.message('\t{0}'.format(a))
      
      raise SystemExit
    
  def __str__(self):
    r = ''
    for i in dir(self):
      if not '__' in i:
        d = self.__getattribute__(i)
        if not hasattr(d, '__call__'):
          r += "\t{0}: {1}\n".format(i, d)
    return r
  
  
  def error(self, msg, position):
    print('ERROR: ', position, ': ', msg, sep='', file=self.stderr)
    if self._debug:
      raise Exception
    raise SystemExit(1)
  
  def warn(self, msg, position):
    self.has_warnings = True
    if not self._quiet or self.forbid_warn:
      print('WARN: ', position, ': ', msg, sep='', file=self.stderr)
    
    if self.forbid_warn:
      raise SystemExit(1)
  
  def message(self, msg, position=None):
    #Discussion: Should position be required?
    if not self._quiet:
      if position:
        print(position, ': ', msg, sep='', file=self.stderr)
      else:
        print(msg, file=self.stderr)
  
  def debug(self, msg, position=None, end='\n'):
    if self._debug:
      if position:
        print('DEBUG: ', position, ': ', msg, sep='', file=self.stderr, end=end)
      else:
        print('DEBUG:', msg, file=self.stderr, end=end)
  
  def strict(self, msg, position=None):
    if self._strict:
      if position:
        print('STRICT:', position, ': ', msg, sep='', file=self.stderr)
      else:
        print('STRICT: ', msg, file=self.stderr)
  
  def __init__(self, args=None, stdin=None, stdout=None, stderr=None):
    """
    Configuration options to permeate the entire parser

    Different levels of messaging.
    ERRORS, which are always fatal
    WARNINGS, which are fatal only if strict
    DEBUG is non-fatal and only printed if debug mode is on
    MESSAGE is informational and is never fatal
    STRICT is shown only if strict. It is fatal
    """
    if args == None:
      args = sys.argv[1:]
    self._strict = False
    self._quiet = False
    self._debug = False
    if stdin == None:
      stdin = sys.stdin
    if stdout == None:
      stdout = sys.stdout
    if stderr == None:
      stderr = sys.stderr
    self.stdin = stdin
    self.stdout = stdout
    self.stderr = stderr
    
    #XXX TODO - organize these variables by parsing layer
    self.print_tokens = False
    self.dotside = True
    self.ascii_only = False
    self.token_error = False
    self.do_exit = False
    self.glyph_table = alphabets.GlyphTable.tables['latin']
    self.forbid_warn = False
    self.output_no_space = False
    self.hate_token = None #If we see this token, raise Exception
    self.permit_readline = True
    
    self.__check_options(args)
    self.has_warnings = False
    self.parsing_unit = 'sumti' #'term' #"sentence" #'quantifier' #"sentence" #'subsentence' #"sumti" #terms
    self.parsing_unit = self.parsing_unit.replace('-', '_')

    #magic-words stuff
    self.allow_erasure = True
    self.si_depth = 5 #Store always at least 5 words for si erasure
    self.handle_su = True #Don't flush until EOT in case we find a su
    self.handle_sa = True #Don't flush for a sentence?
    self.flush_on = None #I or NIhO?
    self.filter_zoi = True 
    self.end_on_faho = True #Treat FAhO as EOT, or uhm... don't yield it...?
    self.position = common.Position()
    
    if self.do_exit:
      raise SystemExit

