from lexer import lexer
import parser

# ----------------------
# Liste de programmes tests
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
    "Test 3 – Parenthèses": """
PROGRAM test3;
VAR
    x : INTEGER;
    y : INTEGER;
BEGIN
    x := 2;
    y := (x + 5) * 3;
    WRITE(y);
END.
""",
    "Test 4 – Variable non déclarée (erreur)": """
PROGRAM test_err1;
VAR
    x : INTEGER;
BEGIN
    x := 5;
    y := 10;  // y n'est pas déclaré
END.
""",
    "Test 5 – Double déclaration (erreur)": """
PROGRAM test_err2;
VAR
    x : INTEGER;
    x : INTEGER;  // double déclaration
BEGIN
    x := 5;
END.
"""
}

# ----------------------
# Exécution des tests
# ----------------------
for title, code in programs.items():
    print("\n" + "="*50)
    print(f"{title}")
    print("="*50 + "\n")
    
    try:
        # Affichage des tokens
        lexer.input(code)
        print("=== TOKENS ===")
        tok = lexer.token()
        while tok:
            print(tok)
            tok = lexer.token()
        
        # Parsing et AST
        print("\n=== PARSING ===")
        parser.parser.parse(code)
        
        # Table des symboles finale
        print("\n=== TABLE DES SYMBOLES ===")
        for var, val in parser.symbol_table.items():
            print(f"{var} = {val}")
        
        # Réinitialiser table des symboles entre programmes
        parser.symbol_table.clear()
        
    except Exception as e:
        print("\n*** ERREUR DÉTECTÉE ***")
        print(e)
        parser.symbol_table.clear()
