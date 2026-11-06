import difflib


class ChangeAnalyzer:
    def analyze(self, old_code: str, new_code: str):
        old_lines = old_code.splitlines()
        new_lines = new_code.splitlines()

        diff = list(
            difflib.unified_diff(
                old_lines,
                new_lines,
                lineterm=""
            )
        )

        added = []
        removed = []

        for line in diff:
            if line.startswith("+") and not line.startswith("+++"):
                added.append(line[1:])

            elif line.startswith("-") and not line.startswith("---"):
                removed.append(line[1:])

        return {
            "added": added,
            "removed": removed,
            "changes": diff
        }