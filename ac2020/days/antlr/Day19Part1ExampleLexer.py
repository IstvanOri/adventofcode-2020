# Generated from Day19Part1Example.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\13\b\1\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\2\2\4\3\3\5\4")
        buf.write("\3\2\2\2\n\2\3\3\2\2\2\2\5\3\2\2\2\3\7\3\2\2\2\5\t\3\2")
        buf.write("\2\2\7\b\7c\2\2\b\4\3\2\2\2\t\n\7d\2\2\n\6\3\2\2\2\3\2")
        buf.write("\2")
        return buf.getvalue()


class Day19Part1ExampleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'a'", "'b'" ]

    symbolicNames = [ "<INVALID>",
 ]

    ruleNames = [ "T__0", "T__1" ]

    grammarFileName = "Day19Part1Example.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


