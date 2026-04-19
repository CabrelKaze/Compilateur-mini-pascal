from lexer import lexer
import parser

# ----------------------
# Programmes tests
# ----------------------
programs = {
    "Test 1 – Assignation simple": """
PROGRAM test1;
VAR
    x : INTEGER;
    y : INTEGER;
BEGIN
    x := 5;
    y := 10;
    WRITE(x);
    WRITE(y);
END.
""",
    "Test 2 – Expressions": """
PROGRAM test2;
VAR
    a : INTEGER;
    b : INTEGER;
    c : INTEGER;
BEGIN
    a := 3;
    b := 4;
    c := a + b * 2;
    WRITE(c);
END.
""",
    "Test 3 – Variable non declaree (erreur)": """
PROGRAM test_err1;
VAR
    x : INTEGER;
BEGIN
    x := 5;
    y := 10;  // y n'est pas declare
END.
""",
    "Test 4 – Double declaration (erreur)": """
PROGRAM test_err2;
VAR
    x : INTEGER;
    x : INTEGER;  // double declaration
BEGIN
    x := 5;
END.
"""
}

# ----------------------
# Fonction pour executer un programme
# ----------------------
def run_program(code, title):
    print("\n" + "="*60)
    print(f"{title}")
    print("="*60 + "\n")
    try:
        # Tokens
        lexer.input(code)
        print("=== TOKENS ===")
        tok = lexer.token()
        while tok:
            print(tok)
            tok = lexer.token()

        # Parsing et AST
        print("\n=== PARSING ===")
        ast_root = parser.parser.parse(code)
        print("AST complet :")
        print(ast_root)

        # Table des symboles
        print("\n=== TABLE DES SYMBOLES ===")
        for var, val in parser.symbol_table.items():
            print(f"{var} = {val}")

        # Nettoyage pour le prochain programme
        parser.symbol_table.clear()

    except Exception as e:
        print("\n*** ERREUR DETECTEE ***")
        print(e)
        parser.symbol_table.clear()

# ----------------------
# Execution de tous les tests
# ----------------------
for title, code in programs.items():
    run_program(code, title)
