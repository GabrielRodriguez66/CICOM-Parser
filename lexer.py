import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'CHARACTER',
    'DIGIT',
    'OPERATOR',
    'SIGN',
    'TILDE',
    'PRIM',
    'ASSIGNMENT_OP',
    'BOOL',
    'EMPTY',
    'COMMA',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'DEF_END',
    'IF_KEYWORD',
    'THEN_KEYWORD',
    'ELSE_KEYWORD',
    'LET_KEYWORD',
    'IN_KEYWORD',
    'MAP_KEYWORD',
    'TO_KEYWORD'
)

# Regular expression rules for simple tokens
t_DIGIT = r'[0-9]'
t_COMMA = r','
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_DEF_END = r';'
t_SIGN = r'\+|-'
t_TILDE = r'~'
t_ASSIGNMENT_OP = r':='
t_OPERATOR = r'!=|<=|>=|[\*\/=<>&|]'
t_CHARACTER = r'[a-zA-Z_]|\?'


def t_PRIM(t):
    r'(number|function|list|empty|cons)\?|cons|first|rest|arity'
    return t


def t_BOOL(t):
    r'true|false'
    return t


def t_EMPTY(t):
    r'empty'
    return t


def t_IF_KEYWORD(t):
    r'if'
    return t


def t_THEN_KEYWORD(t):
    r'then'
    return t


def t_ELSE_KEYWORD(t):
    r'else'
    return t


def t_IN_KEYWORD(t):
    r'in'
    return t


def t_MAP_KEYWORD(t):
    r'map'
    return t


def t_TO_KEYWORD(t):
    r'to'
    return t


def t_LET_KEYWORD(t):
    r'let'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
