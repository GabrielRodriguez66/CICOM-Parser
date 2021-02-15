import sys
from lexer import lexer
from cicom_parser import parser


def parse():
    with open("Test", 'r') as file:
        try:
            parser.parse(file.read())
            print("NOTE: If nothing was printed above, parsing was successful")
        except:
            print("ERROR: Unsuccessful Parsing")


def test_lexer():
    # Give the lexer some input
    with open("Test", 'r') as file:
        lexer.input(file.read())

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


if __name__ == '__main__':
    if '--testLexer' in sys.argv:
        test_lexer()
    else:
        parse()
