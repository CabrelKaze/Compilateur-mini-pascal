import ply.yacc as yacc
from lexer import tokens, lexer

# ----------------------
# Table des symboles
# ----------------------
symbol_table = {}

# ----------------------
# AST Node
# ----------------------
class ASTNode:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children or []

    def pretty(self, level=0):
        ret = "    "*level + f"{self.type}"
        if self.value is not None:
            ret += f": {self.value}"
        ret += "\n"
        for child in self.children:
            ret += child.pretty(level+1)
        return ret

    def __repr__(self):
        return self.pretty()

# ----------------------
# Grammaire
# ----------------------
def p_program(p):
    'program : PROGRAM ID SEMI block DOT'
    p[0] = ASTNode('program', p[2], [p[4]])
    print("Programme correct (syntaxe + sémantique)")
    print("AST du programme :")
    print(p[0])

def p_block(p):
    'block : VAR declarations BEGIN statements END'
    p[0] = ASTNode('block', None, [p[2], p[4]])

def p_declarations(p):
    '''declarations : declarations declaration
                    | declaration'''
    if len(p) == 2:
        p[0] = ASTNode('declarations', children=[p[1]])
    else:
        p[0] = ASTNode('declarations', children=p[1].children + [p[2]])

def p_declaration(p):
    'declaration : ID COLON INTEGER SEMI'
    var_name = p[1]
    if var_name in symbol_table:
        raise Exception(f"Erreur sémantique : variable '{var_name}' déjà déclarée")
    else:
        symbol_table[var_name] = None
    p[0] = ASTNode('declaration', var_name)

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 2:
        p[0] = ASTNode('statements', children=[p[1]])
    else:
        p[0] = ASTNode('statements', children=p[1].children + [p[2]])

def p_statement(p):
    '''statement : ID ASSIGN expression SEMI
                 | WRITE LPAREN expression RPAREN SEMI'''
    if p[1] == 'WRITE':
        p[0] = ASTNode('write', None, [p[3]])
        print("WRITE:", p[3].value)
    else:
        var_name = p[1]
        if var_name not in symbol_table:
            raise Exception(f"Erreur sémantique : variable '{var_name}' non déclarée")
        p[0] = ASTNode('assign', var_name, [p[3]])
        symbol_table[var_name] = p[3].value

# ----------------------
# Expressions
# ----------------------
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ASTNode('binop', p[2], [p[1], p[3]])
    # Calcul si possible
    if all(isinstance(c.value, int) for c in p[0].children):
        if p[2] == '+': p[0].value = p[1].value + p[3].value
        elif p[2] == '-': p[0].value = p[1].value - p[3].value
        elif p[2] == '*': p[0].value = p[1].value * p[3].value
        elif p[2] == '/': p[0].value = p[1].value // p[3].value

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ASTNode('number', p[1])

def p_expression_var(p):
    'expression : ID'
    var_name = p[1]
    if var_name not in symbol_table:
        raise Exception(f"Erreur sémantique : variable '{var_name}' non déclarée")
    p[0] = ASTNode('number', symbol_table[var_name])

# ----------------------
# Gestion des erreurs syntaxiques
# ----------------------
def p_error(p):
    if p:
        print(f"Erreur syntaxique près de '{p.value}'")
    else:
        print("Erreur syntaxique à la fin du fichier")

parser = yacc.yacc()
