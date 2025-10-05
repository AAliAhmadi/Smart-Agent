from langchain.prompts import PromptTemplate

# ReAct prompt for online mode
react_prompt = PromptTemplate.from_template(
    """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat as needed)
Thought: I now know the final answer
Final Answer: the final answer to the original question

Begin!

Question: {input}
{agent_scratchpad}"""
)

# Offline prompt for Gemma-only mode
offline_prompt = PromptTemplate.from_template(
    """You are an offline answering assistant using your internal knowledge (Gemma3:4b).
If the answer involves time-sensitive information (like current events, population, or political figures),
warn the user that the information may be outdated.

Question: {input}"""
)
