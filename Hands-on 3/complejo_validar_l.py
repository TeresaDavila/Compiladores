import ply.lex as lex

tokens = (
    'AND', 'OR', 'NOT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'NUMBER'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_AND(t):
    r'AND'
    return t

def t_OR(t):
    r'OR'
    return t

def t_NOT(t):
    r'NOT'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    raise ValueError("Expresión inválida.")

lexer = lex.lex()