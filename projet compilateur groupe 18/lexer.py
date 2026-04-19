import ply.lex as lex

# Tokens
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN', 'SEMI', 'COLON', 'DOT',
    'LPAREN', 'RPAREN'
]

# Mots réservés
reserved = {
    'PROGRAM':'PROGRAM',
    'VAR':'VAR',
    'BEGIN':'BEGIN',
    'END':'END',
    'INTEGER':'INTEGER',
    'WRITE':'WRITE'
}

tokens += list(reserved.values())

# Opérateurs et ponctuations
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r':='
t_SEMI = r';'
t_COLON = r':'
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Identifiants
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.upper(),'ID')
    return t

# Nombres
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractère illégal '{t.value[0]}' à la ligne {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
