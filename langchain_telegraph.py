from telegraph import Telegraph
from langchain.llms import *
from langchain.agents import  *
import os

class LangChainTelegraph:
    def __init__(self, max_tokens=3000, temperature=0.7, top_p=1.0, max_title_words=8):
        self.telegraph = Telegraph()
        self.telegraph.create_account(short_name=os.getenv('SHORT_NAME'))

        self.llm = OpenAI(max_tokens=max_tokens, temperature=temperature, top_p=top_p)
        
        self.max_title_words = max_title_words

        # Load API keys from environment variables
        os.environ['SERPAPI_API_KEY'] = os.getenv('SERPAPI_API_KEY')
        os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
        os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
        os.environ['WOLFRAM_ALPHA_APPID'] = os.getenv('WOLFRAM_ALPHA_APPID')

    def create_telegraph_page(self, title, text):
        """
        Create a page on Telegraph with a given title and text.
        """
        title = ' '.join(title.split()[:self.max_title_words])
        response = self.telegraph.create_page(
            title,
            html_content=text.replace('\n', '<br>').replace('h1', 'h3').replace('h2', 'h4')
        )
        link = f'<a href = "{response["url"]}">{title}</a>'
        return link

    def generate_html(self, text):
        """
        Generate HTML from text.
        """
        return self.llm(f'(render in html only with tags h1,h2,h3,p,a): {text}')

    def format_prompt(self, text):
        """
        Format a prompt for GPT-3.
        """
        return self.llm(f'Write a prompt for GPT-3 that will be easily understood by the AI and generate an accurate response: {text}')

    def langchain_answer(self, prompt, tools):
        """
        Generate a Langchain answer.
        """
        tools = [
            Tool(
                name="Prompt-to-nice-prompt-formatting",
                func=self.format_prompt,
                description="Used always at start to write a prompt for GPT that will be easily understood by the AI and generate an accurate response.",
            ),
            *tools
        ]
        agent = initialize_agent(tools, self.llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

        answer = agent.run(prompt)
        answer = self.generate_html(answer)
        return self.create_telegraph_page(prompt, answer)
