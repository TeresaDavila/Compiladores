import ply.yacc as yacc
from aritmetico_validar_l import tokens

class SintaxisInvalida(Exception):
    pass

# Definición BNF
def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    pass

def p_expression_term(p):
    'expression : term'
    pass

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    pass

def p_term_factor(p):
    'term : factor'
    pass

def p_factor_num(p):
    'factor : NUMBER'
    pass

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    pass

def p_error(p):
    raise SintaxisInvalida()

parser = yacc.yacc()

# Entrada interactiva
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