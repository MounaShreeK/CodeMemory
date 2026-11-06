import ast


class CodeParser:
    def parse(self, code: str):
        try:
            tree = ast.parse(code)

            functions = []
            classes = []
            imports = []

            for node in ast.walk(tree):

                if isinstance(node, ast.FunctionDef):
                    functions.append(node.name)

                elif isinstance(node, ast.ClassDef):
                    classes.append(node.name)

                elif isinstance(node, ast.Import):
                    for name in node.names:
                        imports.append(name.name)

                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)

            return {
                "functions": functions,
                "classes": classes,
                "imports": imports
            }

        except SyntaxError:
            return {
                "functions": [],
                "classes": [],
                "imports": [],
                "error": "Invalid Python code"
            }