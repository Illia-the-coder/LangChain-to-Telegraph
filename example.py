from langchain_telegraph import LangChainTelegraph
from langchain.tools import Tool
from langchain.agents import AgentType

def dummy_tool_func(prompt):
    """
    A dummy tool function for the example.
    """
    return prompt

def main():
    # Initialize the LangChainTelegraph object
    lct = LangChainTelegraph()

    # Define some tools
    tools = [
        Tool(
            name="Example tool",
            func=dummy_tool_func,  
            description="Example tool description",
        ),
        # Add more tools as needed
    ]

    # Define a prompt
    prompt = "This is a test prompt."

    # Get the LangChain answer and create a Telegraph page
    page_link = lct.langchain_answer(prompt, tools)

    print(page_link)

if __name__ == "__main__":
    main()
