from langchain_community.chat_models import ChatOllama
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain.chains import LLMChain
from langchain_core.runnables.history import RunnableWithMessageHistory
from .prompts import react_prompt, offline_prompt
from .utils import has_internet


def run_agent(task, chat_history):
    """Run the smart agent, switching between online and offline modes."""

    llm = ChatOllama(model="gemma3:4b")

    if has_internet():
        tools = load_tools(["wikipedia", "ddg-search"])
        agent = create_react_agent(llm, tools, react_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

        chain = RunnableWithMessageHistory(
            agent_executor,
            lambda session_id: chat_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )

        response = chain.invoke(
            {"input": task},
            config={"configurable": {"session_id": "chat"}},
        )
        return response.get("output", "No response."), True

    else:
        offline_chain = LLMChain(llm=llm, prompt=offline_prompt)

        chain = RunnableWithMessageHistory(
            offline_chain,
            lambda session_id: chat_history,
            input_messages_key="input",
            history_messages_key="chat_history",
        )

        response = chain.invoke(
            {"input": task},
            config={"configurable": {"session_id": "chat"}},
        )
        return response.get("text", "No response."), False
