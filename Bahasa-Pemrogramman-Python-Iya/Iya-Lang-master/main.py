import iya_lexer
import iya_parser
import iya_interpreter

from sys import *

#DENGAN MASUKAN BAHASAKU.RHS
lexer = iya_lexer.BasicLexer()
parser = iya_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    iya_interpreter.BasicExecute(tree, env)
