# Dictionnaire contenant tous les programmes tests
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
    "Test 2 – Calcul simple": """
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
    "Test 3 – Variable non déclarée (erreur)": """
PROGRAM test_err1;
VAR
    x : INTEGER;
BEGIN
    x := 5;
    y := 10;  // y n'est pas déclarée
END.
""",
    "Test 4 – Double déclaration (erreur)": """
PROGRAM test_err2;
VAR
    x : INTEGER;
    x : INTEGER;  // double déclaration
BEGIN
    x := 5;
END.
""",
    "Test 5 – WRITE simple": """
PROGRAM test3;
VAR
    num : INTEGER;
BEGIN
    num := 42;
    WRITE(num);
END.
"""
}

# Fonction pour accéder aux programmes depuis le compilateur
def get_tests():
    return programs
