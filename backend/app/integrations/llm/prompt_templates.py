CODE_SUMMARY_PROMPT = """
You are a code archaeology assistant.

Analyze the following code and explain:
1. What the code does
2. Important functions and classes
3. Main dependencies
4. The likely purpose of the code

Code:
{code}
"""


CHANGE_ANALYSIS_PROMPT = """
You are a code archaeology assistant.

Analyze the following code change.

Explain:
1. What was added
2. What was removed
3. Why the change may have been made
4. What part of the system could be affected

Old code:
{old_code}

New code:
{new_code}
"""


MEMORY_QUESTION_PROMPT = """
You are a code archaeology assistant.

Use the repository history and memories provided below to answer the question.

Repository memories:
{memories}

Question:
{question}

Give a clear explanation based on the available history.
"""