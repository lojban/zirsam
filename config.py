# -*- coding: utf-8 -*-

"""
Which is the REAL zirsam.py file? Perhaps I'll just make a seperate file to handle it

"""

import sys





class GlyphTable(dict):
  tables = {}
  """A map of funny characters to latin ones. Its capabilities are:
    * Multiple foreign characters can be linked to a single latin character
    * Multiple foreign characters can be linked to a string of latin characters
  It can not map a string of foreign characters to latin characters. """
  latin_lower = "b c d f g h j k l m n p r s t v x z a e i o u y ' . ,".split(' ')
  latin_upper = 'B C D F G H J K L M N P R S T V X Z A E I O U Y " . ,'.split(' ')
  def __repr__(self):
    return "<{0}>".format(self.name)
  def get_char(self, fd, pos):
    #Uses the file-like object fd to return a single latin character.
    c = fd.read(1)
    if c == '': return ''
    if 'EOF' in self and c in self["EOF"]: return ''
    accent_next = False
    unaccent_next = False
    while 1:
      if c in self and self[c] == '\n':
        pos.pushline()
      else:
        pos.pushcol()
      
      if self.ignore and c in self.ignore:
        continue
      elif self.accentmark and c in self.accentmark:
        accent_next = True
      elif self.unaccentmark and c in self.unaccentmark:
        unaccent_next = False
      elif self.accenton and c in self.accenton:
        self.accent_locked_on = True
      elif self.accentoff and c in self.accentoff:
        self.accent_locked_on = False
      else:
        if c in self:
          l = self[c] #This is a latin letter
          if accent_next or self.accent_locked_on:
            return l.upper()
          elif unaccent_next:
            return l.lower()
          else:
            return l
        else:
          return c #Possibly garbage. Or zoi-quote'd
      accent_next = False
      unaccent_next = False
    
    
  def __init__(self, name, foreign_lower, foreign_upper, accentmark=None, unaccentmark=None, accenton=None, accentoff=None, extra={}, newline='\n', ignore='\r', eof=['','\0','\x0c','\x06']):
    """
    name is the name of the alphabet
    foreign_lower is a string of lower case characters, seperated by spaces. They do not imply accent. If multiple foreign letters map to a single latin letter, do not seperate them with a space
    foreign_upper is in a similiar format, except that these letters imply accent. You may specify None, but you'll want to define some kind of accent marking.
    accentmark is a string of characters that mean, "The next character is accented"
    unaccentmark is similiar
    accenton is a string of characters that mean, "Everything following is accented"
    accentoff is a string of characters that mean, "Everything following is unaccented"
    accenton/accentoff characters are not matched. For example, if you have "<^" as accenton and ">v" as accentoff, "<ava" will be translated to "Aa"
    extra is a dictionary in form {latin_character:list_of_foreign_characters}. For example, you could map chinese numeral characters to equivalent latin ones. (The latin_character key doesn't have to be a single character)
    """
    dict.__init__(self)
    self.name = name
    GlyphTable.tables[self.name] = self
    self.accentmark = accentmark #This means the next character is accented
    self.unaccentmark = unaccentmark #This means the next character is not accented
    self.accenton = accenton #This means everything following is accented
    self.accentoff = accentoff #This means everything following is not accented
    
    self.accent_locked_on = False
    
    if type(foreign_lower) == str:
      foreign_lower = foreign_lower.split()
    if type(foreign_upper) == str:
      foreign_upper = foreign_upper.split()
    
    
    for latin, foreign in zip(GlyphTable.latin_lower, foreign_lower):
      for c in foreign:
        self[c] = latin
    if foreign_upper:
      for latin, foreign in zip(GlyphTable.latin_upper, foreign_upper):
        for c in foreign:
          self[c] = latin
    
    for foreign in extra:
      self[foreign] = extra[foreign]
    self[newline] = '\n'
    self.ignore = ignore





#Character classes
_whitespace = ' \t\n\r'
_low_vowel = 'aeiou'

#Only warrior-types use macrons
#I think somebody mentioned that {ä} goes to {'a}?
_A = "AáÁàÀ" #āĀ
_E = "EéÉèÈ" #ēĒ
_I = "IíÍìÌ" #īĪ
_O = "OóÓòÒ" #ōŌ
_U = "UúÚùÙ" #ūŪ
_accent_vowel = _A+_E+_I+_O+_U
_con = 'bcdfgjklmnprstvxz'
_y = 'yY'
_h = "'h\"H"
_comma = ','
_period = "."
_eof = ['', '\00', '\x0c', '\x06'] #Empty string, null character, ^L, ^F. Maybe ^L could be turned into ni'o?








#The default, strict alphabet
strict_alphabet = GlyphTable("strict", GlyphTable.latin_lower, GlyphTable.latin_upper) #Doesn't convert capitalized consonants
latin_alphabet = GlyphTable("latin", GlyphTable.latin_lower, GlyphTable.latin_upper, extra={'B':'b', 'C':'c', 'D':'d', 'F':'f', 'G':'g', 'J':'j', 'K':'k', 'L':'l', 'M':'m', 'N':'n', 'P':'p', 'R':'r', 'S':'s', 'T':'t', 'V':'v', 'X':'x', 'Z':'z'}) #'
# XXX NOTE: This is from Wikipedia. I can not verify if it is correct. All the CLL I've seen seem to have display issues. Can somebody verify this?
ipa_alphabet = GlyphTable("ipa", "b ʃʂ d fɸ g ʒʐ k lɭ mɱ nɳɲŋ p rɾɹʀ s t vβ x z aɑ eɛ i oɔ u ə hθ .ʔ ,".split(), None, accentmark='^')
#As this is also from Wikipedia, maybe it could also use some verification from a Cyrillic-user
cyrillic_alphabet = GlyphTable("cyrillic", "б ш д ф г ж к л м н  п р  с т в х з а е и о у ъ ' . ,".split(),  'Б Ш Д Ф Г Ж К Л М Н  П Р  С Т В Х З А Е И О У Ъ " . ,'.split())
_s = "bb S d f g Z k l mnN p rR s t uvB x z aA Ee I oO u @ h ?".split(' ')
sampa_alphabet = GlyphTable("sampa", _s, _s)
del _s



#And now, for the fun stuff! :D

#P3rm1t teh 1337s
_PA_map = {'1':'pa', '2':'re', '3':'ci', '4':'vo', '5':'mu', '6':'xa', '7':'ze', '8':'bi', '9':'so', '0':'no'}
leet_alphabet = GlyphTable("leet", GlyphTable.latin_lower, GlyphTable.latin_upper, extra=_PA_map)

#Permíts all mannèr of áccents
#(But first, do a bit of voodoo on those character lists)
accent_extra = {}
_v = {'A':_A, 'E':_E, "I":_I, "O":_O, "U":_U}
for vowel in _v:
  for extra in _v[vowel]:
    accent_extra[extra] = vowel

accent_alphabet = GlyphTable("latin+accent", GlyphTable.latin_lower, GlyphTable.latin_upper, extra=accent_extra)


leet_accent_extra = dict(accent_extra, **_PA_map) #(I love that dict trick. It merges two dictionaries)
leet_accent_alphabet = GlyphTable("leet+accent", GlyphTable.latin_lower, GlyphTable.latin_upper, extra=leet_accent_extra)


#And now, for the best one:
liberal_extra = dict(leet_accent_extra, **{"Y":'y', "h":"'", "H":"'", '!':'sai'})
liberal_alphabet = GlyphTable("liberal", GlyphTable.latin_lower, GlyphTable.latin_upper, extra=liberal_extra)

microblog_alphabet = GlyphTable("microblog", GlyphTable.latin_lower, GlyphTable.latin_upper, ignore='@!#\r')


def format_arg(w):
  return '--'+w.strip().replace(' ', '-')


class Configuration:
  __help_header = """The Purple Parser, by purpleposeidon

Jbobau to parse is read from standard input. Parsed text is sent to stdout, errors and messages are sent to stderr.
If an error prevents the text from being fully parsed, a non-zero value is returned.

Arguments (In no particular order):"""
  __help = {'help':"Shows this help", \
  'quiet':"Don't print warnings", \
  'err2out':"Write what would normally go to stderr to the output", \
  
  'alphabet':"Select alphabet. --alphabet=? lists available values. The default is 'latin'", \
  
  'no dotside':"Don't require a pause following cmene-markers", \
  'forbid warn':"Treat warnings as errors", \
  'strict':"Count warnings as errors", \
  
  'debug':"(DEBUG OPTION) Print information from parsing", \
  'token error':"(DEBUG OPTION) Raise an Exception when the first token is made, which prints a backtrace", \
  'hate token':"(DEBUG OPTION) Raise an exception when that text is encountered", \
  'do exit':"(DEBUG OPTION) Exit without parsing", \
  'print tokens':"(DEBUG OPTION) Print out a tokens as they are created", \
  
  'no space':"(NOT IMPLEMENTED) Convert input to not use spaces", \
  
  }
  __help_order = 'help, quiet, err2out, alphabet, no dotside, forbid warn, strict, debug, token error, hate token, do exit, print tokens, no space'.split(', ') #Help, Parsing configuration, Debug, unimplemented
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
            r = 'Usage: --{0}=VALUE. Possible values for {0} are:\n'.format(name)
            for v in val_dict:
              r += '\t{0}\n'.format(v)
            raise SystemExit(r)
          else:
            raise Exception("{0} is an invalid value for --{1}".format(repr(val), name))
        elif arg.find('--'+name) == 0:
          r = 'Usage: --{0}=VALUE. Possible values for {0} are:\n'.format(name)
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
      print(Configuration.__help_header, file=sys.stderr)
      #for cmd in Configuration.__help:
      for cmd in Configuration.__help_order:
        print("    {0}: {1}".format(format_arg(cmd), Configuration.__help[cmd]), file=sys.stderr)
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
    #if arg("latin"):
      #self.glyph_table = latin_alphabet
    #if arg("ipa"):
      #self.glyph_table = ipa_alphabet
    #if arg("cyrillic"):
      #self.glyph_table = cyrillic_alphabet
    if arg("forbid warn"):
      self.forbid_warn = True
    #if arg("1337"):
      #if self.glyph_table == accent_alphabet:
        #self.glyph_table = leet_accent_alphabet
      #else:
        #self.glyph_table = leet_alphabet
    #if arg("accent"):
      #if self.glyph_table == leet_alphabet:
        #self.glyph_table = leet_accent_alphabet
      #else:
        #self.glyph_table = accent_alphabet
    #if arg("microblog"):
      #self.glyph_table = microblog_alphabet
    #if arg("liberal"):
      #self.gyph_table = liberal_alphabet
    if arg("err2out"):
      sys.stderr = sys.stdout # XXX Make this Configuration's output
    if arg("no space"):
      self.output_no_space = True
    _ = valued_arg("alphabet", GlyphTable.tables)
    if _: self.glyph_table = _
    _ = valued_arg("hate token")
    if _: self.hate_token = _
    if possible_args:
      print("The following arguments have documentation, but no implementation:", file=sys.stderr)
      for p in possible_args:
        print('\t', format_arg(p), file=sys.stderr)
    
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
    print('ERROR: ', position, ': ', msg, sep='', file=sys.stderr)
    if self._debug:
      raise Exception
    raise SystemExit(1)
  
  def warn(self, msg, position):
    self.has_warnings = True
    if not self._quiet or self.forbid_warn:
      print('WARN: ', position, ': ', msg, sep='', file=sys.stderr)
    
    if self.forbid_warn:
      raise SystemExit(1)
  
  def message(self, msg, position=None):
    if not self._quiet:
      if position:
        print('MESSAGE: ', position, ': ', msg, sep='', file=sys.stderr)
      else:
        print('MESSAGE:', msg, file=sys.stderr)
  
  def debug(self, msg, position=None, end='\n'):
    if self._debug:
      if position:
        print('DEBUG: ', position, ': ', msg, sep='', file=sys.stderr, end=end)
      else:
        print('DEBUG:', msg, file=sys.stderr, end=end)
  
  def strict(self, msg, position=None):
    if self._strict:
      if position:
        print('STRICT:', position, ': ', msg, sep='', file=sys.stderr)
      else:
        print('STRICT: ', msg, file=sys.stderr)
  
  def __init__(self, args):
    """
    Configuration options to permeate the entire parser

    Different levels of messaging.
    ERRORS, which are always fatal
    WARNINGS, which are fatal only if strict
    DEBUG is non-fatal and only printed if debug mode is on
    MESSAGE is informational and is never fatal
    STRICT is shown only if strict. It is fatal
    """
    self._strict = False
    self._quiet = False
    self._debug = False
    self.print_tokens = False
    self.dotside = True
    self.ascii_only = False
    self.token_error = False
    self.do_exit = False
    self.glyph_table = latin_alphabet
    self.forbid_warn = False
    self.output_no_space = False
    self.hate_token = None #If we see this token, raise Exception
    
    
    self.__check_options(args)
    self.has_warnings = False
    
    
    
    if self.do_exit:
      raise SystemExit
