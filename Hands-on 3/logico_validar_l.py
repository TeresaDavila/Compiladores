import ply.lex as lex

# Lista de tokens
tokens = (
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN',
    'BOOLEAN'
)

# Expresiones regulares
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

def t_BOOLEAN(t):
    r'0|1'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

# Manejo de errores léxicos
def t_error(t):
    raise ValueError("Expresión inválida.")

# Crear el analizador léxico
lexer = lex.lex()