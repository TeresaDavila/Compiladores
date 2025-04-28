import ply.lex as lex

# Definición de tokens
tokens = ('KEYWORD', 'ID', 'NUMBER', 'OPERATOR', 'DELIMITER')

t_ignore = ' \t'
t_KEYWORD = r'int|return'
t_OPERATOR = r'[+\-*/=<>]'
t_DELIMITER = r'[(){};]'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inesperado: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def contar_tokens(codigo):
    lexer.input(codigo)
    conteo = {token: 0 for token in tokens}
    for tok in lexer:
        conteo[tok.type] += 1
    return conteo

# Prueba del analizador
codigo_fuente = """
int x = 2*y;
int res = (x+2)*y;
if (res > 20) {
    return res;
}
"""

resultado = contar_tokens(codigo_fuente)
print(resultado)

