import ast


class DependencyAnalyzer:
    def analyze(self, code: str):
        try:
            tree = ast.parse(code)

            dependencies = []

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):
                    for name in node.names:
                        dependencies.append(name.name)

                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        dependencies.append(node.module)

            return {
                "dependencies": list(set(dependencies))
            }

        except SyntaxError:
            return {
                "dependencies": [],
                "error": "Invalid Python code"
            }