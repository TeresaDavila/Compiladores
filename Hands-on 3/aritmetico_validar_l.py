import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

# Expresiones regulares para los tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Regla para reconocer números (enteros)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter no válido: '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()