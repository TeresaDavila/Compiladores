import ply.yacc as yacc
from logico_validar_l import tokens

class SintaxisInvalida(Exception):
    pass

# Definición BNF

def p_expression_binop(p):
    '''expression : expression AND term
                  | expression OR term'''
    pass

def p_expression_term(p):
    'expression : term'
    pass

def p_term_not(p):
    'term : NOT factor'
    pass

def p_term_factor(p):
    'term : factor'
    pass

def p_factor_group(p):
    'factor : LPAREN expression RPAREN'
    pass

def p_factor_boolean(p):
    'factor : BOOLEAN'
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