# LangChain Telegraph

This Python module uses the Telegraph API, OpenAI's API, and Langchain's API to generate a response from OpenAI's GPT-3 model based on a provided prompt, format the response in HTML, and then publish it as a new Telegraph page.

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/langchain-telegraph.git
```

Change into the cloned directory:

```bash
cd langchain-telegraph
```

It is recommended to create a virtual environment and install the required packages there:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Environment Variables

The module requires the following environment variables:

- `SERPAPI_API_KEY`: Your SerpApi key
- `OPENAI_API_KEY`: Your OpenAI key
- `SERPER_API_KEY`: Your Serper key
- `WOLFRAM_ALPHA_APPID`: Your Wolfram Alpha App ID
- `SHORT_NAME`: Short name for the Telegraph account

## Usage

Here's an example of how you can use this module:

```python
from main import LangChainTelegraph
from langchain.tools import Tool
from langchain.agents import AgentType

# Initialize the LangChainTelegraph object
lct = LangChainTelegraph()

# Define some tools
tools = [
    Tool(
        name="Some tool",
        func=lambda x: x,  # Replace with an actual function
        description="Some tool description",
    ),
    # Add more tools as needed
]

# Define a prompt
prompt = "This is a test prompt."

# Get the LangChain answer and create a Telegraph page
page_link = lct.langchain_answer(prompt, tools)

print(page_link)
```

Replace `my_module` with the actual name of your Python module.

## Contributing

If you want to contribute to this project, please feel free to fork the repository, make your changes, and open a pull request.

## License

This project is licensed under the terms of the MIT license.

Please replace the placeholders with the actual values where necessary. You might also want to add more information about the specific tools you are using, the structure of the project, and how to test the code.
