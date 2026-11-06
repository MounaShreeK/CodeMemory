class DecisionAgent:

    async def analyze(self, question: str, context: list):
        if not context:
            return {
                "decision": "insufficient_context",
                "reason": "No relevant repository history was found."
            }

        return {
            "decision": "use_context",
            "reason": "Relevant repository history is available.",
            "context_count": len(context)
        }