import iya_lexer
import iya_parser
import iya_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = iya_lexer.BasicLexer()
    parser = iya_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('plus62 > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            basic_interpreter.BasicExecute(tree, env)
