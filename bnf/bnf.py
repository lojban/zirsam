# -*- coding: utf-8 -*-

# generated on Sun Sep 13 14:29:06 2009 by poseidon@skami

from bnfgen import *

rules = (
Statement(Rule('sumti-2'), Concat(Rule('sumti-3'), Repeated(Optional(Rule('joik-ek'), Rule('sumti-3'))))), \
Statement(Rule('sentence'), Concat(Optional(Rule('terms'), Optional(Terminal(CU), Optional(Repeated(Rule('free'))))), Rule('bridi-tail'))), \
Statement(Rule('text'), Concat(Optional(Repeated(Terminal(NAI))), Or(Optional(Repeated(Terminal(CMENE)), Optional(Repeated(Rule('free')))), Concat(Paren(AndOr(Rule('indicators'), Repeated(Rule('free')))))), Optional(Rule('joik-jek')), Rule('text-1'))), \
Statement(Rule('tense-modal'), Or(Concat(Rule('simple-tense-modal'), Optional(Repeated(Rule('free')))), Concat(Terminal(FIhO), Optional(Repeated(Rule('free'))), Rule('selbri'), Elidable(Terminal(FEhU), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('gek-sentence'), Or(Or(Concat(Rule('gek'), Rule('subsentence'), Rule('gik'), Rule('subsentence'), Rule('tail-terms')), Concat(Optional(Rule('tag')), Terminal(KE), Optional(Repeated(Rule('free'))), Rule('gek-sentence'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free')))))), Concat(Terminal(NA), Optional(Repeated(Rule('free'))), Rule('gek-sentence')))), \
Statement(Rule('lerfu-string'), Concat(Rule('lerfu-word'), Or(Optional(Terminal(PA)), Repeated(Concat(Rule('lerfu-word')))))), \
Statement(Rule('interval-property'), Or(Or(Concat(Rule('number'), Terminal(ROI), Optional(Terminal(NAI))), Concat(Terminal(TAhE), Optional(Terminal(NAI)))), Concat(Terminal(ZAhO), Optional(Terminal(NAI))))), \
Statement(Rule('indicator'), Or(Or(Or(Concat(Or(Paren(Terminal(UI)), Concat(Terminal(CAI))), Optional(Terminal(NAI))), Concat(Terminal(Y))), Concat(Terminal(DAhO))), Concat(Terminal(FUhO)))), \
Statement(Rule('space-interval'), Concat(AndOr(Paren(Paren(AndOr(Terminal(VEhA), Terminal(VIhA))), Optional(Terminal(FAhA), Optional(Terminal(NAI)))), Rule('space-int-props')))), \
Statement(Rule('termset'), Or(Concat(Terminal(NUhI), Optional(Repeated(Rule('free'))), Rule('gek'), Rule('terms'), Elidable(Terminal(NUhU), Optional(Repeated(Rule('free')))), Rule('gik'), Rule('terms'), Elidable(Terminal(NUhU), Optional(Repeated(Rule('free'))))), Concat(Terminal(NUhI), Optional(Repeated(Rule('free'))), Rule('terms'), Elidable(Terminal(NUhU), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('fragment'), Or(Or(Or(Or(Or(Or(Or(Or(Concat(Rule('ek'), Optional(Repeated(Rule('free')))), Concat(Rule('gihek'), Optional(Repeated(Rule('free'))))), Concat(Rule('quantifier'))), Concat(Terminal(NA), Optional(Repeated(Rule('free'))))), Concat(Rule('terms'), Elidable(Terminal(VAU), Optional(Repeated(Rule('free')))))), Concat(Rule('prenex'))), Concat(Rule('relative-clauses'))), Concat(Rule('links'))), Concat(Rule('linkargs')))), \
Statement(Rule('selbri'), Concat(Optional(Rule('tag')), Rule('selbri-1'))), \
Statement(Rule('space-int-props'), Concat(Repeated(Paren(Terminal(FEhE), Rule('interval-property'))))), \
Statement(Rule('sumti-4'), Or(Concat(Rule('sumti-5')), Concat(Rule('gek'), Rule('sumti'), Rule('gik'), Rule('sumti-4')))), \
Statement(Rule('mex-1'), Concat(Rule('mex-2'), Optional(Terminal(BIhE), Optional(Repeated(Rule('free'))), Rule('operator'), Rule('mex-1')))), \
Statement(Rule('mex-2'), Or(Concat(Rule('operand')), Concat(Optional(Terminal(PEhO), Optional(Repeated(Rule('free')))), Rule('operator'), Repeated(Rule('mex-2')), Elidable(Terminal(KUhE), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('sumti-1'), Concat(Rule('sumti-2'), Optional(Or(Paren(Rule('ek')), Concat(Rule('joik'))), Optional(Rule('stag')), Terminal(KE), Optional(Repeated(Rule('free'))), Rule('sumti'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('space-offset'), Concat(Terminal(FAhA), Optional(Terminal(NAI)), Optional(Terminal(VA)))), \
Statement(Rule('sumti-3'), Concat(Rule('sumti-4'), Optional(Or(Paren(Rule('ek')), Concat(Rule('joik'))), Optional(Rule('stag')), Terminal(BO), Optional(Repeated(Rule('free'))), Rule('sumti-3')))), \
Statement(Rule('gek'), Or(Or(Concat(Optional(Terminal(SE)), Terminal(GA), Optional(Terminal(NAI)), Optional(Repeated(Rule('free')))), Concat(Rule('joik'), Terminal(GI), Optional(Repeated(Rule('free'))))), Concat(Rule('stag'), Rule('gik')))), \
Statement(Rule('quantifier'), Or(Concat(Rule('number'), Elidable(Terminal(BOI), Optional(Repeated(Rule('free'))))), Concat(Terminal(VEI), Optional(Repeated(Rule('free'))), Rule('mex'), Elidable(Terminal(VEhO), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('term'), Or(Or(Or(Concat(Rule('sumti')), Concat(Or(Paren(Rule('tag')), Concat(Terminal(FA), Optional(Repeated(Rule('free'))))), Or(Paren(Rule('sumti')), Concat(Elidable(Terminal(KU), Optional(Repeated(Rule('free')))))))), Concat(Rule('termset'))), Concat(Terminal(NA), Terminal(KU), Optional(Repeated(Rule('free')))))), \
Statement(Rule('text-1'), Concat(Or(Optional(Repeated(Paren(Terminal(I), Or(Optional(Rule('jek')), Concat(Rule('joik'))), Optional(Optional(Rule('stag')), Terminal(BO)), Optional(Repeated(Rule('free')))))), Concat(Repeated(Terminal(NIhO)), Optional(Repeated(Rule('free'))))), Optional(Rule('paragraphs')))), \
Statement(Rule('bridi-tail'), Concat(Rule('bridi-tail-1'), Optional(Rule('gihek'), Optional(Rule('stag')), Terminal(KE), Optional(Repeated(Rule('free'))), Rule('bridi-tail'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free')))), Rule('tail-terms')))), \
Statement(Rule('sumti-tail-1'), Or(Concat(Optional(Rule('quantifier')), Rule('selbri'), Optional(Rule('relative-clauses'))), Concat(Rule('quantifier'), Rule('sumti')))), \
Statement(Rule('sumti-tail'), Or(Concat(Optional(Rule('sumti-6'), Optional(Rule('relative-clauses'))), Rule('sumti-tail-1')), Concat(Rule('relative-clauses'), Rule('sumti-tail-1')))), \
Statement(Rule('ek'), Concat(Optional(Terminal(NA)), Optional(Terminal(SE)), Terminal(A), Optional(Terminal(NAI)))), \
Statement(Rule('mex-operator'), Or(Or(Or(Or(Concat(Terminal(SE), Optional(Repeated(Rule('free'))), Rule('mex-operator')), Concat(Terminal(NAhE), Optional(Repeated(Rule('free'))), Rule('mex-operator'))), Concat(Terminal(MAhO), Optional(Repeated(Rule('free'))), Rule('mex'), Elidable(Terminal(TEhU), Optional(Repeated(Rule('free')))))), Concat(Terminal(NAhU), Optional(Repeated(Rule('free'))), Rule('selbri'), Elidable(Terminal(TEhU), Optional(Repeated(Rule('free')))))), Concat(Terminal(VUhU), Optional(Repeated(Rule('free')))))), \
Statement(Rule('paragraphs'), Concat(Rule('paragraph'), Optional(Repeated(Terminal(NIhO)), Optional(Repeated(Rule('free'))), Rule('paragraphs')))), \
Statement(Rule('operand'), Concat(Rule('operand-1'), Optional(Or(Paren(Rule('ek')), Concat(Rule('joik'))), Optional(Rule('stag')), Terminal(KE), Optional(Repeated(Rule('free'))), Rule('operand'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('selbri-6'), Or(Concat(Rule('tanru-unit'), Optional(Terminal(BO), Optional(Repeated(Rule('free'))), Rule('selbri-6'))), Concat(Optional(Terminal(NAhE), Optional(Repeated(Rule('free')))), Rule('guhek'), Rule('selbri'), Rule('gik'), Rule('selbri-6')))), \
Statement(Rule('selbri-4'), Concat(Rule('selbri-5'), Or(Optional(Rule('joik-jek'), Rule('selbri-5')), Repeated(Concat(Rule('joik'), Optional(Rule('stag')), Terminal(KE), Optional(Repeated(Rule('free'))), Rule('selbri-3'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free'))))))))), \
Statement(Rule('selbri-5'), Concat(Rule('selbri-6'), Optional(Or(Paren(Rule('jek')), Concat(Rule('joik'))), Optional(Rule('stag')), Terminal(BO), Optional(Repeated(Rule('free'))), Rule('selbri-5')))), \
Statement(Rule('selbri-2'), Concat(Rule('selbri-3'), Optional(Terminal(CO), Optional(Repeated(Rule('free'))), Rule('selbri-2')))), \
Statement(Rule('selbri-3'), Concat(Repeated(Rule('selbri-4')))), \
Statement(Rule('selbri-1'), Or(Concat(Rule('selbri-2')), Concat(Terminal(NA), Optional(Repeated(Rule('free'))), Rule('selbri')))), \
Statement(Rule('operator-1'), Or(Or(Concat(Rule('operator-2')), Concat(Rule('guhek'), Rule('operator-1'), Rule('gik'), Rule('operator-2'))), Concat(Rule('operator-2'), Or(Paren(Rule('jek')), Concat(Rule('joik'))), Optional(Rule('stag')), Terminal(BO), Optional(Repeated(Rule('free'))), Rule('operator-1')))), \
Statement(Rule('operator-2'), Or(Concat(Rule('mex-operator')), Concat(Terminal(KE), Optional(Repeated(Rule('free'))), Rule('operator'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('bridi-tail-1'), Concat(Rule('bridi-tail-2'), Repeated(Optional(Rule('gihek'), Optional(Repeated(Rule('free'))), Rule('bridi-tail-2'), Rule('tail-terms'))))), \
Statement(Rule('bridi-tail-2'), Concat(Rule('bridi-tail-3'), Optional(Rule('gihek'), Optional(Rule('stag')), Terminal(BO), Optional(Repeated(Rule('free'))), Rule('bridi-tail-2'), Rule('tail-terms')))), \
Statement(Rule('bridi-tail-3'), Or(Concat(Rule('selbri'), Rule('tail-terms')), Concat(Rule('gek-sentence')))), \
Statement(Rule('lerfu-word'), Or(Or(Or(Concat(Terminal(BY)), Concat(Rule('any-word'), Terminal(BU))), Concat(Terminal(LAU), Rule('lerfu-word'))), Concat(Terminal(TEI), Rule('lerfu-string'), Terminal(FOI)))), \
Statement(Rule('sumti'), Concat(Rule('sumti-1'), Optional(Terminal(VUhO), Optional(Repeated(Rule('free'))), Rule('relative-clauses')))), \
Statement(Rule('terms'), Concat(Repeated(Rule('terms-1')))), \
Statement(Rule('free'), Or(Or(Or(Or(Or(Or(Or(Or(Concat(Terminal(SEI), Optional(Repeated(Rule('free'))), Optional(Rule('terms'), Optional(Terminal(CU), Optional(Repeated(Rule('free'))))), Rule('selbri'), Elidable(Terminal(SEhU))), Concat(Terminal(SOI), Optional(Repeated(Rule('free'))), Rule('sumti'), Optional(Rule('sumti')), Elidable(Terminal(SEhU)))), Concat(Rule('vocative'), Optional(Rule('relative-clauses')), Rule('selbri'), Optional(Rule('relative-clauses')), Elidable(Terminal(DOhU)))), Concat(Rule('vocative'), Optional(Rule('relative-clauses')), Repeated(Terminal(CMENE)), Optional(Repeated(Rule('free'))), Optional(Rule('relative-clauses')), Elidable(Terminal(DOhU)))), Concat(Rule('vocative'), Optional(Rule('sumti')), Elidable(Terminal(DOhU)))), Concat(Or(Paren(Rule('number')), Concat(Rule('lerfu-string'))), Terminal(MAI))), Concat(Terminal(TO), Rule('text'), Elidable(Terminal(TOI)))), Concat(Terminal(XI), Optional(Repeated(Rule('free'))), Or(Paren(Rule('number')), Concat(Rule('lerfu-string'))), Elidable(Terminal(BOI)))), Concat(Terminal(XI), Optional(Repeated(Rule('free'))), Terminal(VEI), Optional(Repeated(Rule('free'))), Rule('mex'), Elidable(Terminal(VEhO))))), \
Statement(Rule('gihek'), Concat(Optional(Terminal(NA)), Optional(Terminal(SE)), Terminal(GIhA), Optional(Terminal(NAI)))), \
Statement(Rule('simple-tense-modal'), Or(Or(Or(Concat(Optional(Terminal(NAhE)), Optional(Terminal(SE)), Terminal(BAI), Optional(Terminal(NAI)), Optional(Terminal(KI))), Concat(Optional(Terminal(NAhE)), Or(Paren(Rule('time'), Optional(Rule('space'))), AndOr(Concat(Rule('space'), Optional(Rule('time'))), Terminal(CAhA))), Optional(Terminal(KI)))), Concat(Terminal(KI))), Concat(Terminal(CUhE)))), \
Statement(Rule('relative-clause'), Or(Concat(Terminal(GOI), Optional(Repeated(Rule('free'))), Rule('term'), Elidable(Terminal(GEhU), Optional(Repeated(Rule('free'))))), Concat(Terminal(NOI), Optional(Repeated(Rule('free'))), Rule('subsentence'), Elidable(Terminal(KUhO), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('space'), Concat(AndOr(AndOr(AndOr(Terminal(VA), Repeated(Rule('space-offset'))), Rule('space-interval')), Paren(Terminal(MOhI), Rule('space-offset'))))), \
Statement(Rule('number'), Concat(Terminal(PA), Or(Optional(Terminal(PA)), Repeated(Concat(Rule('lerfu-word')))))), \
Statement(Rule('operator'), Concat(Rule('operator-1'), Or(Optional(Rule('joik-jek'), Rule('operator-1')), Repeated(Concat(Rule('joik'), Optional(Rule('stag')), Terminal(KE), Optional(Repeated(Rule('free'))), Rule('operator'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free'))))))))), \
Statement(Rule('operand-1'), Concat(Rule('operand-2'), Repeated(Optional(Rule('joik-ek'), Rule('operand-2'))))), \
Statement(Rule('operand-3'), Or(Or(Or(Or(Or(Or(Concat(Rule('quantifier')), Concat(Rule('lerfu-string'), Elidable(Terminal(BOI), Optional(Repeated(Rule('free')))))), Concat(Terminal(NIhE), Optional(Repeated(Rule('free'))), Rule('selbri'), Elidable(Terminal(TEhU), Optional(Repeated(Rule('free')))))), Concat(Terminal(MOhE), Optional(Repeated(Rule('free'))), Rule('sumti'), Elidable(Terminal(TEhU), Optional(Repeated(Rule('free')))))), Concat(Terminal(JOhI), Optional(Repeated(Rule('free'))), Repeated(Rule('mex-2')), Elidable(Terminal(TEhU), Optional(Repeated(Rule('free')))))), Concat(Rule('gek'), Rule('operand'), Rule('gik'), Rule('operand-3'))), Concat(Or(Paren(Terminal(LAhE), Optional(Repeated(Rule('free')))), Concat(Terminal(NAhE), Terminal(BO), Optional(Repeated(Rule('free'))))), Rule('operand'), Elidable(Terminal(LUhU), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('operand-2'), Concat(Rule('operand-3'), Optional(Or(Paren(Rule('ek')), Concat(Rule('joik'))), Optional(Rule('stag')), Terminal(BO), Optional(Repeated(Rule('free'))), Rule('operand-2')))), \
Statement(Rule('mex'), Or(Concat(Rule('mex-1'), Repeated(Optional(Rule('operator'), Rule('mex-1')))), Concat(Terminal(FUhA), Optional(Repeated(Rule('free'))), Rule('rp-expression')))), \
Statement(Rule('statement'), Or(Concat(Rule('statement-1')), Concat(Rule('prenex'), Rule('statement')))), \
Statement(Rule('indicators'), Concat(Optional(Terminal(FUhE)), Repeated(Rule('indicator')))), \
Statement(Rule('jek'), Concat(Optional(Terminal(NA)), Optional(Terminal(SE)), Terminal(JA), Optional(Terminal(NAI)))), \
Statement(Rule('gik'), Concat(Terminal(GI), Optional(Terminal(NAI)), Optional(Repeated(Rule('free'))))), \
Statement(Rule('joik-ek'), Or(Concat(Rule('joik'), Optional(Repeated(Rule('free')))), Concat(Rule('ek'), Optional(Repeated(Rule('free')))))), \
Statement(Rule('rp-operand'), Or(Concat(Rule('operand')), Concat(Rule('rp-expression')))), \
Statement(Rule('guhek'), Concat(Optional(Terminal(SE)), Terminal(GUhA), Optional(Terminal(NAI)), Optional(Repeated(Rule('free'))))), \
Statement(Rule('joik'), Or(Or(Concat(Optional(Terminal(SE)), Terminal(JOI), Optional(Terminal(NAI))), Concat(Rule('interval'))), Concat(Terminal(GAhO), Rule('interval'), Terminal(GAhO)))), \
Statement(Rule('tanru-unit'), Concat(Rule('tanru-unit-1'), Repeated(Optional(Terminal(CEI), Optional(Repeated(Rule('free'))), Rule('tanru-unit-1'))))), \
Statement(Rule('rp-expression'), Concat(Rule('rp-operand'), Rule('rp-operand'), Rule('operator'))), \
Statement(Rule('paragraph'), Concat(Or(Paren(Rule('statement')), Concat(Rule('fragment'))), Repeated(Optional(Terminal(I), Optional(Repeated(Rule('free'))), Or(Optional(Rule('statement')), Concat(Rule('fragment'))))))), \
Statement(Rule('tail-terms'), Concat(Optional(Rule('terms')), Elidable(Terminal(VAU), Optional(Repeated(Rule('free')))))), \
Statement(Rule('relative-clauses'), Concat(Rule('relative-clause'), Repeated(Optional(Terminal(ZIhE), Optional(Repeated(Rule('free'))), Rule('relative-clause'))))), \
Statement(Rule('joik-jek'), Or(Concat(Rule('joik'), Optional(Repeated(Rule('free')))), Concat(Rule('jek'), Optional(Repeated(Rule('free')))))), \
Statement(Rule('links'), Concat(Terminal(BEI), Optional(Repeated(Rule('free'))), Rule('term'), Optional(Rule('links')))), \
Statement(Rule('prenex'), Concat(Rule('terms'), Terminal(ZOhU), Optional(Repeated(Rule('free'))))), \
Statement(Rule('tag'), Concat(Rule('tense-modal'), Repeated(Optional(Rule('joik-jek'), Rule('tense-modal'))))), \
Statement(Rule('linkargs'), Concat(Terminal(BE), Optional(Repeated(Rule('free'))), Rule('term'), Optional(Rule('links')), Elidable(Terminal(BEhO), Optional(Repeated(Rule('free')))))), \
Statement(Rule('vocative'), Concat(AndOr(Repeated(Paren(Terminal(COI), Optional(Terminal(NAI)))), Terminal(DOI)))), \
Statement(Rule('subsentence'), Or(Concat(Rule('sentence')), Concat(Rule('prenex'), Rule('subsentence')))), \
Statement(Rule('time-offset'), Concat(Terminal(PU), Optional(Terminal(NAI)), Optional(Terminal(ZI)))), \
Statement(Rule('terms-1'), Concat(Rule('terms-2'), Repeated(Optional(Terminal(PEhE), Optional(Repeated(Rule('free'))), Rule('joik-jek'), Rule('terms-2'))))), \
Statement(Rule('terms-2'), Concat(Rule('term'), Repeated(Optional(Terminal(CEhE), Optional(Repeated(Rule('free'))), Rule('term'))))), \
Statement(Rule('tanru-unit-2'), Or(Or(Or(Or(Or(Or(Or(Or(Or(Or(Concat(Terminal(SELBRI), Optional(Repeated(Rule('free')))), Concat(Terminal(GOhA), Optional(Terminal(RAhO)), Optional(Repeated(Rule('free'))))), Concat(Terminal(KE), Optional(Repeated(Rule('free'))), Rule('selbri-3'), Elidable(Terminal(KEhE), Optional(Repeated(Rule('free')))))), Concat(Terminal(ME), Optional(Repeated(Rule('free'))), Rule('sumti'), Elidable(Terminal(MEhU), Optional(Repeated(Rule('free')))), Optional(Terminal(MOI), Optional(Repeated(Rule('free')))))), Concat(Or(Paren(Rule('number')), Concat(Rule('lerfu-string'))), Terminal(MOI), Optional(Repeated(Rule('free'))))), Concat(Terminal(NUhA), Optional(Repeated(Rule('free'))), Rule('mex-operator'))), Concat(Terminal(SE), Optional(Repeated(Rule('free'))), Rule('tanru-unit-2'))), Concat(Terminal(JAI), Optional(Repeated(Rule('free'))), Optional(Rule('tag')), Rule('tanru-unit-2'))), Concat(Rule('any-word'), Repeated(Paren(Terminal(ZEI), Rule('any-word'))))), Concat(Terminal(NAhE), Optional(Repeated(Rule('free'))), Rule('tanru-unit-2'))), Concat(Terminal(NU), Optional(Terminal(NAI)), Optional(Repeated(Rule('free'))), Repeated(Optional(Rule('joik-jek'), Terminal(NU), Optional(Terminal(NAI)), Optional(Repeated(Rule('free'))))), Rule('subsentence'), Elidable(Terminal(KEI), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('tanru-unit-1'), Concat(Rule('tanru-unit-2'), Optional(Rule('linkargs')))), \
Statement(Rule('statement-3'), Or(Concat(Rule('sentence')), Concat(Optional(Rule('tag')), Terminal(TUhE), Optional(Repeated(Rule('free'))), Rule('text-1'), Elidable(Terminal(TUhU), Optional(Repeated(Rule('free'))))))), \
Statement(Rule('statement-2'), Concat(Rule('statement-3'), Optional(Terminal(I), Or(Optional(Rule('jek')), Concat(Rule('joik'))), Optional(Rule('stag')), Terminal(BO), Optional(Repeated(Rule('free'))), Optional(Rule('statement-2'))))), \
Statement(Rule('statement-1'), Concat(Rule('statement-2'), Repeated(Optional(Terminal(I), Rule('joik-jek'), Optional(Rule('statement-2')))))), \
Statement(Rule('stag'), Concat(Rule('simple-tense-modal'), Repeated(Optional(Or(Paren(Rule('jek')), Concat(Rule('joik'))), Rule('simple-tense-modal'))))), \
Statement(Rule('sumti-5'), Or(Concat(Optional(Rule('quantifier')), Rule('sumti-6'), Optional(Rule('relative-clauses'))), Concat(Rule('quantifier'), Rule('selbri'), Elidable(Terminal(KU), Optional(Repeated(Rule('free')))), Optional(Rule('relative-clauses'))))), \
Statement(Rule('interval'), Concat(Optional(Terminal(SE)), Terminal(BIhI), Optional(Terminal(NAI)))), \
Statement(Rule('sumti-6'), Or(Or(Or(Or(Or(Or(Or(Or(Or(Concat(Or(Paren(Terminal(LAhE), Optional(Repeated(Rule('free')))), Concat(Terminal(NAhE), Terminal(BO), Optional(Repeated(Rule('free'))))), Optional(Rule('relative-clauses')), Rule('sumti'), Elidable(Terminal(LUhU), Optional(Repeated(Rule('free'))))), Concat(Terminal(KOhA), Optional(Repeated(Rule('free'))))), Concat(Rule('lerfu-string'), Elidable(Terminal(BOI), Optional(Repeated(Rule('free')))))), Concat(Terminal(LA), Optional(Repeated(Rule('free'))), Optional(Rule('relative-clauses')), Repeated(Terminal(CMENE)), Optional(Repeated(Rule('free'))))), Concat(Or(Paren(Terminal(LA)), Concat(Terminal(LE))), Optional(Repeated(Rule('free'))), Rule('sumti-tail'), Elidable(Terminal(KU), Optional(Repeated(Rule('free')))))), Concat(Terminal(LI), Optional(Repeated(Rule('free'))), Rule('mex'), Elidable(Terminal(LOhO), Optional(Repeated(Rule('free')))))), Concat(Terminal(ZO), Rule('any-word'), Optional(Repeated(Rule('free'))))), Concat(Terminal(LU), Rule('text'), Elidable(Terminal(LIhU), Optional(Repeated(Rule('free')))))), Concat(Terminal(LOhU), Repeated(Rule('any-word')), Terminal(LEhU), Optional(Repeated(Rule('free'))))), Concat(Terminal(ZOI), Rule('any-word'), Rule('anything'), Rule('any-word'), Optional(Repeated(Rule('free')))))), \
Statement(Rule('time'), Concat(AndOr(AndOr(Terminal(ZI), Repeated(Rule('time-offset'))), Terminal(ZEhA)), AndOr(Optional(Terminal(PU), Optional(Terminal(NAI))), Repeated(Rule('interval-property'))))), \
)