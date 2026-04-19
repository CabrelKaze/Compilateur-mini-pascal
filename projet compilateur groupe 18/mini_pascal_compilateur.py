from lexer import lexer
import parser

def run_compilateur(file_path):
    try:
        # Lecture du programme Mini-Pascal
        with open(file_path, "r") as f:
            code = f.read()

        # -----------------------
        # Analyse lexicale
        # -----------------------
        print("\n=== TOKENS ===")
        lexer.input(code)
        tok = lexer.token()
        while tok:
            print(tok)
            tok = lexer.token()

        # -----------------------
        # Analyse syntaxique et AST
        # -----------------------
        print("\n=== PARSING ===")
        ast_root = parser.parser.parse(code)
        print("AST complet :")
        print(ast_root)

        # -----------------------
        # Table des symboles
        # -----------------------
        print("\n=== TABLE DES SYMBOLES ===")
        for var, val in parser.symbol_table.items():
            print(f"{var} = {val}")

        # Nettoyage pour prochains fichiers
        parser.symbol_table.clear()

    except FileNotFoundError:
        print(f"Erreur : le fichier '{file_path}' est introuvable.")
    except Exception as e:
        print("\n*** ERREUR DETECTEE ***")
        print(e)
        parser.symbol_table.clear()


if __name__ == "__main__":
    print("=== Mini-Pascal Compilateur ===")
    while True:
        file_path = input("Chemin du fichier Mini-Pascal (ou 'quit' pour sortir) : ")
        if file_path.lower() == "quit":
            print("Fermeture du compilateur.")
            break
        run_compilateur(file_path)
        print("\n" + "="*60 + "\n")
