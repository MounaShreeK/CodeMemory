class CodeSummarizer:
    def summarize(self, code: str, parsed_data: dict):
        functions = parsed_data.get("functions", [])
        classes = parsed_data.get("classes", [])
        imports = parsed_data.get("imports", [])

        return {
            "summary": (
                f"The code contains {len(classes)} classes, "
                f"{len(functions)} functions, and "
                f"{len(imports)} imports."
            ),
            "classes": classes,
            "functions": functions,
            "imports": imports
        }