from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tools_calls=True,
    markdown=True,
)

app = Playground(agents=[finance_agent, web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
