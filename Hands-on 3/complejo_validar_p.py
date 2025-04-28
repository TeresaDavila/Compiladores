import ply.yacc as yacc
from complejo_validar_l import tokens

class SintaxisInvalida(Exception):
    pass

# BNF

def p_expr_binop(p):
    '''expr : expr PLUS term
            | expr MINUS term'''
    pass

def p_expr_term(p):
    'expr : term'
    pass

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    pass

def p_term_factor(p):
    'term : factor'
    pass

def p_factor_expr(p):
    'factor : LPAREN expr RPAREN'
    pass

def p_factor_logical(p):
    'factor : logical'
    pass

def p_logical_binop(p):
    '''logical : logical AND logical
               | logical OR logical'''
    pass

def p_logical_not(p):
    'logical : NOT logical'
    pass

def p_logical_group_expr(p):
    'logical : LPAREN expr RPAREN'
    pass

def p_logical_number(p):
    'logical : NUMBER'
    pass

def p_error(p):
    raise SintaxisInvalida()

parser = yacc.yacc()

# Entrada
while True:
    try:
        s = input('exp > ')
        if not s:
            continue
        try:
            parser.parse(s)
            print("Expresión válida.")
        except SintaxisInvalida:
            print("Expresión inválida.")
    except EOFError:
        break