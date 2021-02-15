import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens

tokens = tokens  # forcing import


def p_exp(p):
    """exp      : IF_KEYWORD exp THEN_KEYWORD exp ELSE_KEYWORD exp
                | LET_KEYWORD defplus IN_KEYWORD exp
                | MAP_KEYWORD idList TO_KEYWORD exp
                | term binop exp
                | term
        defplus : def
                | def defplus
    """
    pass


def p_term(p):
    """term : unop term
            | factor
            | factor LEFT_PAREN expList RIGHT_PAREN
            | empty
            | int
            | bool
    """
    pass


def p_factor(p):
    """factor : LEFT_PAREN exp RIGHT_PAREN
              | prim
              | id
    """
    pass


def p_expList(p):
    '''expList : propExpList
              |
    '''
    pass


def p_propExpList(p):
    '''propExpList : exp
                  | exp COMMA propExpList
    '''
    pass


def p_idList(p):
    '''idList : propIdList
              |
    '''
    pass


def p_propIdList(p):
    '''propIdList : id
                  | id COMMA propIdList
    '''
    pass


def p_def(p):
    'def : id ASSIGNMENT_OP exp DEF_END'
    pass


def p_empty(p):
    'empty : EMPTY'
    pass


def p_bool(p):
    'bool : BOOL'
    pass


def p_unop(p):
    '''unop : sign
            | TILDE '''
    pass


def p_sign(p):
    'sign : SIGN'
    pass


def p_binop(p):
    '''binop : SIGN
            | OPERATOR'''
    pass


def p_prim(p):
    'prim : PRIM'
    pass


def p_id(p):
    '''id : CHARACTER
          | id CHARACTER
          | id DIGIT
    '''
    pass


def p_int(p):
    '''int  : DIGIT
            | DIGIT int'''
    pass


# Error rule for syntax errors
def p_error(p):
    print("ERROR: Syntax error in input!")


# Build the parser
parser = yacc.yacc()
