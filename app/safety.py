from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types


safety_agent = Agent(
    name="safety_agent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
Review every response before it is shown.

Ensure:

No diagnosis

No medicine recommendation

No unsafe advice

Always include:

'This information is for educational purposes only and is not a substitute for professional medical advice.'
""",
)