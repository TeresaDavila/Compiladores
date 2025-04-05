import ply.lex as lex

# Definición de tokens
tokens = ('INT', 'RETURN', 'ID', 'NUMBER', 'COMMENT', 'STRING')

t_ignore = ' \t'
t_INT = r'int'
t_RETURN = r'return'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_STRING = r'".*?"'
t_COMMENT = r'\#.*'

def t_multiline_comment(t):
    r'(\'\'\'.*?\'\'\')|(""".*?""")'
    pass  # Ignorar comentarios multilínea

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inesperado: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Prueba del analizador
codigo = """
int x = 2*y; # x vale 2 multiplicado por y
"x es el doble de y"
#    y 
#    = 
#    x/2  
"""
lexer.input(codigo)
for tok in lexer:
    print(tok)

