import ply.lex as lex

# Definición de tokens
tokens = ('INT', 'RETURN', 'ID', 'NUMBER')

# Reglas de tokens
t_ignore = ' \t'
t_INT = r'int'
t_RETURN = r'return'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inesperado: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Prueba del analizador
codigo = "int res = x/10;\t return res;"
lexer.input(codigo)
for tok in lexer:
    print(tok)

