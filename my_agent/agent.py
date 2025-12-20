from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='<FILL_IN_MODEL>',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
.